import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import warnings
import ctypes
import pymem
from Offsets import *
warnings.simplefilter("ignore")

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor(0,255,0,255))                
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))


    def paintEvent(self, event):
        ws = self.ws
        d = 6
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        # painter.drawLine( x1,y1, x2,y2    )
        painter.drawLine(   ws/2, 0,               ws/2, ws/2 - ws/d   )   # Top
        painter.drawLine(   ws/2, ws/2 + ws/d,     ws/2, ws            )   # Bottom
        painter.drawLine(   0, ws/2,               ws/2 - ws/d, ws/2   )   # Left
        painter.drawLine(   ws/2 + ws/d, ws/2,     ws, ws/2            )   # Right

def main() :
    app = QtWidgets.QApplication(sys.argv) 

    widget = Crosshair(windowSize=24, penWidth=1)
    widget.show()

    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
        return
    
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

    awp = 9
    ssg = 40
    scar = 38
    g3sg1 = 11
    snipers = [awp, ssg, scar, g3sg1]


    while True :
        app.processEvents()
        player = pm.read_int(client + dwLocalPlayer)
        scoped = pm.read_int(player + m_bIsScoped)

        weapon = pm.read_int(player + m_hActiveWeapon)
        weapon_entity = pm.read_int(client + dwEntityList + ((weapon & 0xFFF) - 1) * 0x10)
        try :
            weapon_id = str(pm.read_short(weapon_entity + m_iItemDefinitionIndex))
        except :
            pass

        if weapon:
            if int(weapon_id) in snipers and scoped == 0 :
                widget.show()
            else :
                widget.hide()

if __name__ == '__main__':
    main()