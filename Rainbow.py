import sys
sys.path.insert(1, 'utils/')
from wallhack import main as wh
from bhop import main as a_bhop
from triggerbot import main as tg
from noflash import main as nf
from rcs import main as rcs_p
from radar import main as radar
from money import main as money
from aimbot import main as ai
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from PIL import ImageTk,Image
from multiprocessing import *
import threading
import multiprocessing
import ctypes
import os
import pymem
import pymem.process
import keyboard

window = Tk()
first = 1
delay_tg = 0.1
key_tg = "shift"
delay_mh = 1
smooth_ai = 4
key_ai = "f"
fov_ai = 10

def config_loader() :

    #Création de la fenêtre
    conf_loader = Tk()
    w = 300
    h = 115
    ws = conf_loader.winfo_screenwidth()
    hs = conf_loader.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    conf_loader.geometry('%dx%d+%d+%d' % (w, h, x, y))
    conf_loader.title('Config Loader')
    conf_loader.iconbitmap("images/rainbow.ico")
    conf_loader.config(background='#f0f0f0')

    #Création du texte
    conf_text = StringVar()
    label1 = Label(conf_loader, text = 'Load a config :', font=(40))  #Load a config (titre)
    label1.place(relx=1, x=-190, y=0, anchor=NE)                      #Load a config (titre)
    
    #Création de la liste déroulante pour les fichiers
    folder = "configs/"
    filelist = [fname for fname in os.listdir(folder) if fname.endswith('.cfg')]
    optmenu = ttk.Combobox(conf_loader, values=filelist, state='readonly')
    global optmenu
    optmenu.place(relx=1, x=-155, y=25, anchor=NE)

    #Création du texte
    bouton2 = Button(conf_loader, text="Load", font=(40), command= lambda: path_writer())     #Load (path writer boutton)
    bouton2.place(relx=1, x=-100, y=20, anchor=NE)                                            #Load (path writer boutton)
    label2 = Label(conf_loader, text = 'Export current config :', font=(40))       #Export the config (titre)
    label2.place(relx=1, x=-145, y=60, anchor=NE)                                  #Export the config (titre)
    label3 = Label(conf_loader, text = 'Export as :', font=(40))                   #Export the config as (titre)
    label3.place(relx=1, x=-221, y=82, anchor=NE)                                  #Export the config as (titre)
    conf_entry = Entry(conf_loader, textvariable = conf_text, width=15)            #Nom de la config (entrée)
    conf_entry.place(relx=1, x=-125, y=85, anchor=NE)                              #Nom de la config (entrée)
    label4 = Label(conf_loader, text = '.cfg', font=(40))                          #.cfg (titre)
    label4.place(relx=1, x=-100, y=82, anchor=NE)                                  #.cfg (titre)
    bouton3 = Button(conf_loader, text="Export", font=(40), command= lambda: export())          #Export (boutton)
    bouton3.place(relx=1, x=-25, y=79, anchor=NE)                                               #Export (boutton)

    def path_writer() :                 #Sous programme qui note le chemin d'accès dans configs/path.txt
        config = optmenu.get()
        global config
        f = open("configs/path.txt", "w")
        f.write(config)
        f.close()

        #On met à jour les valeurs en les changeants par celles de la config choisie
        with open("configs/"+config) as config_file :
            line_nmb = 1
            for line in config_file :
                if line_nmb == 2 :
                    delay_tg = line
                    global delay_tg
                if line_nmb == 3 :
                    key_tg = line[0:-1]
                    global key_tg
                if line_nmb == 5 :
                    delay_mh = line
                    global delay_mh
                if line_nmb == 7 :
                    key_ai = line
                    global key_ai
                if line_nmb == 8 :
                    smooth_ai = line
                    global smooth_ai
                if line_nmb == 9 :
                    fov_ai = line
                    global fov_ai
                if line_nmb >= 10 :
                    config_file.close()
                    break
                line_nmb = line_nmb + 1
        
        #On met à jour dans les configs
        delay_mh_print = delay_mh
        delay_tg_print = delay_tg
        key_tg_print = key_tg
        key_ai_print = key_ai
        smooth_ai_print = smooth_ai
        fov_ai_print = fov_ai
        global fov_ai_print
        global smooth_ai_print
        global key_ai_print
        global delay_mh_print
        global delay_tg_print
        global key_tg_print

        #On met une message box
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Config Loaded !', 'Success', 0)

    def export() :                      #Sous programme qui exporte la configuration actuelle
        conf_name = conf_entry.get()
        os.system("echo #Triggerbot >> configs/"+conf_name+".cfg")
        os.system("echo "+str(delay_tg)+" >> configs/"+conf_name+".cfg")
        os.system("echo "+key_tg+" >> configs/"+conf_name+".cfg")
        os.system("echo #Money Hack >> configs/"+conf_name+".cfg")
        os.system("echo "+str(delay_mh)+" >> configs/"+conf_name+".cfg")
        os.system("echo #Aimbot >> configs/"+conf_name+".cfg")
        os.system("echo "+str(key_ai)+" >> configs/"+conf_name+".cfg")
        os.system("echo "+str(smooth_ai)+" >> configs/"+conf_name+".cfg")
        os.system("echo "+str(fov_ai)+" >> configs/"+conf_name+".cfg")
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Config exported in configs/'+conf_name+'.cfg !', 'Success', 0)

    conf_loader.mainloop()


def aimbot_conf() :

    #Création de la fenêtre
    aimbot_conf = Tk()
    w = 400
    h = 180
    ws = aimbot_conf.winfo_screenwidth()
    hs = aimbot_conf.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    aimbot_conf.geometry('%dx%d+%d+%d' % (w, h, x, y))
    aimbot_conf.title('Aimbot Configuration')
    aimbot_conf.iconbitmap("images/rainbow.ico")
    aimbot_conf.config(background='#f0f0f0')

    #On cherche le nom de la config actuelle
    with open("configs/path.txt") as path_txt :
        path = path_txt.readline()
        path_txt.close()

    #On met à jour les valeurs en les changeants par celles de la config choisie si c'est la première fois dans le programme
    try :
        str(key_ai_print)
    except Exception as e:
        with open("configs/"+path) as config_file :
            line_nmb = 1
            for line in config_file :
                if line_nmb == 7 :
                    key_ai_print = line[0:-1]
                    global key_ai_print
                if line_nmb == 8 :
                    smooth_ai = line[0:-1]
                    smooth_ai_print = str(smooth_ai)
                    global smooth_ai_print
                if line_nmb == 9 :
                    fov_ai = line[0:-1]
                    fov_ai_print = str(fov_ai)
                    global fov_ai_print
                if line_nmb >= 10 :
                    config_file.close()
                    break
                line_nmb = line_nmb + 1
    
    #Création du texte	
    smooth_ai = " "
    key_ai = "a"
    fov_ai = "b"
    label1 = Label(aimbot_conf, text = 'Smooth value :', font=(40))               #Smooth (titre)
    label1.place(relx=1, x=-290, y=0, anchor=NE)                                  #Smooth (titre)
    label3 = Label(aimbot_conf, text = 'Current value : '+str(smooth_ai_print), font=(40))     #Smooth (current)
    label3.place(relx=1, x=-63, y=0, anchor=NE)                                                #Smooth (current)
    ai_entry = Entry(aimbot_conf, textvariable = smooth_ai, width=25)             #Smooth (entrée)
    ai_entry.place(relx=1, x=-243, y=25, anchor=NE)                               #Smooth (entrée)
    bouton = Button(aimbot_conf, text="Submit", font=(40), command= lambda: aimbot_conf_save_delay(ai_entry, aimbot_conf))              #Smooth (boutton)
    bouton.place(relx=1, x=-173, y=20, anchor=NE)                                                                                       #Smooth (boutton)
    label2 = Label(aimbot_conf, text = 'Keybind :', font=(40))                #Keybind (titre)
    label2.place(relx=1, x=-330, y=60, anchor=NE)                             #Keybind (titre)
    ai_entry2 = Entry(aimbot_conf, textvariable = key_ai, width=25)           #Keybind (entrée)
    ai_entry2.place(relx=1, x=-243, y=90, anchor=NE)                          #Keybind (entrée)
    label4 = Label(aimbot_conf, text = 'Current value : '+str(key_ai_print), font=(40))                                      #Keybind (current)
    label4.place(relx=1, x=-67, y=65, anchor=NE)                                                                             #Keybind (current)
    bouton2 = Button(aimbot_conf, text="Submit", font=(40), command= lambda: aimbot_conf_save_key(ai_entry2, aimbot_conf))   #Keybind (bouton)
    bouton2.place(relx=1, x=-173, y=85, anchor=NE)                                                                           #Keybind (bouton)
    label5 = Label(aimbot_conf, text = 'FOV :', font=(40))                    #Fov (titre)
    label5.place(relx=1, x=-353, y=125, anchor=NE)                            #Fov (titre)
    ai_entry3 = Entry(aimbot_conf, textvariable = fov_ai, width=25)           #Fov (entrée)
    ai_entry3.place(relx=1, x=-243, y=150, anchor=NE)                         #Fov (entrée)
    label6 = Label(aimbot_conf, text = 'Current value : '+str(fov_ai_print), font=(40))                                      #Fov (current)
    label6.place(relx=1, x=-55, y=125, anchor=NE)                                                                             #Fov (current)
    bouton3 = Button(aimbot_conf, text="Submit", font=(40), command= lambda: aimbot_conf_save_fov(ai_entry3, aimbot_conf))   #Fov (bouton)
    bouton3.place(relx=1, x=-173, y=145, anchor=NE)                                                                          #Fov (bouton)
    

    def aimbot_conf_save_fov(ai_entry3, aimbot_conf) :     #On récupère le texte et on fait apparaître une fenêtre
        fov_ai = ai_entry3.get()
        fov_ai_print = fov_ai
        global fov_ai_print
        print("fov")
        print(fov_ai)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du aimbot
        global fov_ai

    def aimbot_conf_save_delay(ai_entry, aimbot_conf) :    #On récupère le texte et on fait apparaître une fenêtre
        smooth_ai = ai_entry.get()
        smooth_ai_print = smooth_ai
        global smooth_ai_print
        print("smooth")
        print(smooth_ai)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du aimbot
        global smooth_ai

    def aimbot_conf_save_key(ai_entry2, aimbot_conf) :    #On récupère le texte et on fait apparaître une fenêtre
        key_ai = ai_entry2.get()
        key_ai_print = key_ai
        global key_ai_print
        print("key aimbot")
        print(key_ai)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du aimbot
        global key_ai

    aimbot_conf.mainloop()

def wallhack_conf() :

    #Création de la fenêtre
    wallhack_conf = Tk()
    w = 300
    h = 125
    ws = wallhack_conf.winfo_screenwidth()
    hs = wallhack_conf.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    wallhack_conf.geometry('%dx%d+%d+%d' % (w, h, x, y))
    wallhack_conf.title('Wallhack Configuration')
    wallhack_conf.iconbitmap("images/rainbow.ico")
    wallhack_conf.config(background='#fcfefc')
    wallhack_conf.mainloop()

    #Création du texte

def triggerbot_conf() :

    #Création de la fenêtre
    triggerbot_conf = Tk()
    w = 400
    h = 125
    ws = triggerbot_conf.winfo_screenwidth()
    hs = triggerbot_conf.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    triggerbot_conf.geometry('%dx%d+%d+%d' % (w, h, x, y))
    triggerbot_conf.title('Triggerbot Configuration')
    triggerbot_conf.iconbitmap("images/rainbow.ico")
    triggerbot_conf.config(background='#f0f0f0')

    #On cherche le nom de la config actuelle
    with open("configs/path.txt") as path_txt :
        path = path_txt.readline()
        path_txt.close()

    #On met à jour les valeurs en les changeants par celles de la config choisie si c'est la première fois dans le programme
    try :
        str(key_tg_print)
    except Exception as e:
        with open("configs/"+path) as config_file :
            line_nmb = 1
            for line in config_file :
                if line_nmb == 2 :
                    delay_tg = line[0:-1]
                    delay_tg_print = str(delay_tg)
                    global delay_tg_print
                if line_nmb == 3 :
                    key_tg_print = line[0:-1]
                    global key_tg_print
                if line_nmb >= 4 :
                    config_file.close()
                    break
                line_nmb = line_nmb + 1
    
    #Création du texte	
    delay_tg = " "
    delay_tg2 = "a"
    label1 = Label(triggerbot_conf, text = 'Delay : (default = 0.1)', font=(40))  #Délai (titre)
    label1.place(relx=1, x=-247, y=0, anchor=NE)                                  #Délai (titre)
    label3 = Label(triggerbot_conf, text = 'Current value : '+str(delay_tg_print), font=(40)) #Délai (current)
    label3.place(relx=1, x=-53, y=0, anchor=NE)                                                #Délai (current)
    tg_entry = Entry(triggerbot_conf, textvariable = delay_tg, width=25)          #Délai (entrée)
    tg_entry.place(relx=1, x=-243, y=25, anchor=NE)                               #Délai (entrée)
    bouton = Button(triggerbot_conf, text="Submit", font=(40), command= lambda: triggerbot_conf_save_delay(tg_entry, triggerbot_conf))  #Délai (boutton)
    bouton.place(relx=1, x=-173, y=20, anchor=NE)                                                                                       #Délai (boutton)
    label2 = Label(triggerbot_conf, text = 'Keybind :', font=(40))                #Keybind (titre)
    label2.place(relx=1, x=-330, y=60, anchor=NE)                                 #Keybind (titre)
    tg_entry2 = Entry(triggerbot_conf, textvariable = delay_tg2, width=25)        #Keybind (entrée)
    tg_entry2.place(relx=1, x=-243, y=90, anchor=NE)                              #Keybind (entrée)
    label4 = Label(triggerbot_conf, text = 'Current value : '+str(key_tg_print), font=(40)) #Keybind (current)
    label4.place(relx=1, x=-48, y=65, anchor=NE)                                            #Keybind (current)
    bouton2 = Button(triggerbot_conf, text="Submit", font=(40), command= lambda: triggerbot_conf_save_key(tg_entry2, triggerbot_conf))   #Keybind (bouton)
    bouton2.place(relx=1, x=-173, y=85, anchor=NE)                                                                                       #Keybind (bouton)
    

    def triggerbot_conf_save_delay(tg_entry, triggerbot_conf) :    #On récupère le texte et on fait apparaître une fenêtre
        delay_tg = tg_entry.get()
        delay_tg_print = delay_tg
        global delay_tg_print
        print("delay")
        print(delay_tg)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du Triggerbot
        global delay_tg

    def triggerbot_conf_save_key(tg_entry2, triggerbot_conf) :    #On récupère le texte et on fait apparaître une fenêtre
        key_tg = tg_entry2.get()
        key_tg_print = key_tg
        global key_tg_print
        print("key")
        print(key_tg)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du Triggerbot
        global key_tg

    triggerbot_conf.mainloop()

def moneyhack_conf() :

    #Création de la fenêtre
    moneyhack_conf = Tk()
    w = 400
    h = 60
    ws = moneyhack_conf.winfo_screenwidth()
    hs = moneyhack_conf.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    moneyhack_conf.geometry('%dx%d+%d+%d' % (w, h, x, y))
    moneyhack_conf.title('Money Hack Configuration')
    moneyhack_conf.iconbitmap("images/rainbow.ico")
    moneyhack_conf.config(background='#f0f0f0')

    #On cherche le nom de la config actuelle
    with open("configs/path.txt") as path_txt :
        path = path_txt.readline()
        path_txt.close()

    #On met à jour les valeurs en les changeants par celles de la config choisie si c'est la première fois dans le programme
    try :
        str(delay_mh_print)
    except Exception as e:
        with open("configs/"+path) as config_file :
            line_nmb = 1
            for line in config_file :
                if line_nmb == 5 :
                    delay_mh = line[0:-1]
                    delay_mh_print = str(delay_mh)
                    global delay_mh_print
                if line_nmb >= 6 :
                    config_file.close()
                    break
                line_nmb = line_nmb + 1
    
    #Création du texte	
    delay_mh = " "
    label1 = Label(moneyhack_conf, text = 'Refresh delay : (default = 1)', font=(40))  #Délai (titre)
    label1.place(relx=1, x=-205, y=0, anchor=NE)                                        #Délai (titre)
    label3 = Label(moneyhack_conf, text = 'Current value : '+str(delay_mh_print), font=(40)) #Délai (current)
    label3.place(relx=1, x=-53, y=0, anchor=NE)                                                #Délai (current)
    mh_entry = Entry(moneyhack_conf, textvariable = delay_mh, width=25)          #Délai (entrée)
    mh_entry.place(relx=1, x=-243, y=25, anchor=NE)                               #Délai (entrée)
    bouton = Button(moneyhack_conf, text="Submit", font=(40), command= lambda: moneyhack_conf_save_delay(mh_entry, moneyhack_conf))  #Délai (boutton)
    bouton.place(relx=1, x=-173, y=20, anchor=NE)                                                                                       #Délai (boutton)

    def moneyhack_conf_save_delay(mh_entry, moneyhack_conf) :    #On récupère le texte et on fait apparaître une fenêtre
        delay_mh = mh_entry.get()
        delay_mh_print = delay_mh
        global delay_mh_print
        print("mh delay")
        print(delay_mh)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Value updated !', 'Success', 0)

        #On met à jour la variable de délai du moneyhack
        global delay_mh

    moneyhack_conf.mainloop()

def aimbot(window, green, red, Aimbot) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = Aimbot.cget('bg')
    if curent_cl == red :
        #On appelle le aimbot
        multiprocessing.freeze_support()
        t_ai = Process(target = ai)
        global t_ai
        t_ai.start()
        return green
    elif curent_cl == green :
        t_ai.terminate()
        return red

    buttons(window)

def wallhack(window, green, red, Wallhack) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = Wallhack.cget('bg')
    if curent_cl == red :
        #On appelle le wallhack
        multiprocessing.freeze_support()
        t_wh = Process(target = wh)
        global t_wh
        t_wh.start()
        return green
    elif curent_cl == green :
        t_wh.terminate()
        return red

    buttons(window)

def bhop(window, green, red, Bhop) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = Bhop.cget('bg')
    if curent_cl == red :
        #On appelle le bhop
        multiprocessing.freeze_support()
        t_bhop = Process(target = a_bhop)
        global t_bhop
        t_bhop.start()
        return green
    elif curent_cl == green :
        t_bhop.terminate()
        return red

    buttons(window)

def triggerbot(window, green, red, Triggerbot) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = Triggerbot.cget('bg')
    if curent_cl == red :
        #On appelle le triggerbot
        multiprocessing.freeze_support()
        t_triggerbot = Process(target = tg)
        global t_triggerbot
        t_triggerbot.start()
        return green
    elif curent_cl == green :
        t_triggerbot.terminate()
        return red

    buttons(window)

def noflash(window, green, red, Noflash) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = Noflash.cget('bg')
    if curent_cl == red :
        #On appelle le noflash
        multiprocessing.freeze_support()
        t_noflash = Process(target = nf)
        global t_noflash
        t_noflash.start()
        return green
    elif curent_cl == green :
        t_noflash.terminate()
        return red

    buttons(window)

def rcs(window, green, red, RCS) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = RCS.cget('bg')
    if curent_cl == red :
        #On appelle le rcs
        multiprocessing.freeze_support()
        t_rcs = Process(target = rcs_p)
        global t_rcs
        t_rcs.start()
        return green
    elif curent_cl == green :
        t_rcs.terminate()
        return red

    buttons(window)

def radarhack(window, green, red, RadarHack) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = RadarHack.cget('bg')
    if curent_cl == red :
        #On appelle le radar hack
        multiprocessing.freeze_support()
        t_radar = Process(target = radar)
        global t_radar
        t_radar.start()
        return green
    elif curent_cl == green :
        t_radar.terminate()
        return red

    buttons(window)

def moneyhack(window, green, red, MoneyHack) :

    #Si la couleur du boutton == rouge alors on la change en vert
    #Et vice-versa
    curent_cl = MoneyHack.cget('bg')
    if curent_cl == red :
        #On appelle le Money hack
        multiprocessing.freeze_support()
        t_money = Process(target = money)
        global t_money
        t_money.start()
        return green
    elif curent_cl == green :
        t_money.terminate()
        return red

    buttons(window)



def mainmenu(window, first) :

    #On essaye de trouver le processus csgo.exe
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
        sys.exit()
    
    #On supprimme l'ancien fichier utils/txt/offsets.txt
    #os.system('cd utils/txt/ && del offsets.txt && cd .. && cd ..')

    #On fait appel à utils/offsets.py pour créer le fichier utils/txt/offsets.txt
    #os.system('cd utils/ && offsets.exe && cd ..')

    #On crée les variables locales
    green = '#0BFF14'
    red = 'FF0B0B'

    #On paramètre la fenêtre
    w = 600
    h = 400
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.title('Rainbow Cheat V2.01 by ALittlePatate')
    window.iconbitmap("images/rainbow.ico")
    window.config(background='#fcfefc')

    #On met le nom du menu en haut
    if first == 1 :
        label_title = Label(window, text=("Rainbow Cheat"), bg='#fcfefc', fg='#000000', font=(40)) 
        label_title.pack()
    else :
        pass

    #On met le fond d'écran
    if first == 1 :
        canvas=Canvas(window,width=300,height=300,highlightthickness=0)
        image=ImageTk.PhotoImage(Image.open("images/bg.gif"))
        canvas.create_image(0,0, anchor=NW, image=image)
        canvas.place(x=20, y=20)
    else :
        pass
    
    buttons(window)

def buttons(window) :
    
    #On définit les couleurs utilisées
    green = '#0BFF14'
    red = '#FF0B0B'

    #On place les bouttons

    #Aimbot
    Aimbot = Button(window, text="Aimbot", bg=red, fg='#000000', font=(40), command= lambda: Aimbot.configure(background = aimbot(window, green, red, Aimbot)))
    Aimbot.place(relx=1, x=-200, y=100, anchor=NE)
    #Config du Aimbot
    Aimbot_conf = Button(window, text="Config", fg='#000000', font=(40), command= lambda: aimbot_conf())
    Aimbot_conf.place(relx=1, x=-260, y=100, anchor=NE)

    #Wallhack
    Wallhack = Button(window, text="Wallhack", bg=red, fg='#000000', font=(40), command= lambda: Wallhack.configure(background = wallhack(window, green, red, Wallhack)))
    Wallhack.place(relx=1, x=-80, y=100, anchor=NE)
    #Config du Wallhack
    Wallhack_conf = Button(window, text="Config", fg='#000000', font=(40), command= lambda: wallhack_conf())
    Wallhack_conf.place(relx=1, x=-26, y=100, anchor=NE)

    #Bhop
    Bhop = Button(window, text="Auto Bhop", bg=red, fg='#000000', font=(40), command= lambda: Bhop.configure(background = bhop(window, green, red, Bhop)))
    Bhop.place(relx=1, x=-200, y=150, anchor=NE)

    #Triggerbot
    Triggerbot = Button(window, text="Triggerbot", bg=red, fg='#000000', font=(40), command= lambda: Triggerbot.configure(background = triggerbot(window, green, red, Triggerbot)))
    Triggerbot.place(relx=1, x=-80, y=150, anchor=NE)
    #Config du Triggerbot
    Triggerbot_conf = Button(window, text="Config", fg='#000000', font=(40), command= lambda: triggerbot_conf())
    Triggerbot_conf.place(relx=1, x=-26, y=150, anchor=NE)

    #Noflash
    Noflash = Button(window, text="Noflash", bg=red, fg='#000000', font=(40), command= lambda: Noflash.configure(background = noflash(window, green, red, Noflash)))
    Noflash.place(relx=1, x=-200, y=200, anchor=NE)

    #RCS
    RCS = Button(window, text="RCS", bg=red, fg='#000000', font=(40), command= lambda: RCS.configure(background = rcs(window, green, red, RCS)))
    RCS.place(relx=1, x=-110, y=200, anchor=NE)

    #Radar Hack
    RadarHack = Button(window, text="RadarHack", bg=red, fg='#000000', font=(40), command= lambda: RadarHack.configure(background = radarhack(window, green, red, RadarHack)))
    RadarHack.place(relx=1, x=-200, y=250, anchor=NE)

    #Money Hack
    MoneyHack = Button(window, text="Show Money", bg=red, fg='#000000', font=(40), command= lambda: MoneyHack.configure(background = moneyhack(window, green, red, MoneyHack)))
    MoneyHack.place(relx=1, x=-60, y=250, anchor=NE)
    #Config du Money Hack
    MoneyHack_conf = Button(window, text="Config", fg='#000000', font=(40), command= lambda: moneyhack_conf())
    MoneyHack_conf.place(relx=1, x=-6, y=250, anchor=NE)

    #Config Loader
    Config_loader = Button(window, text="Configs", font=(40), command= lambda: config_loader())
    Config_loader.place(relx=1, x=-525, y=360, anchor=NE)

    window.mainloop()

if __name__ == '__main__':
    freeze_support()
    mainmenu(window, first)