from tkinter import * 
import os
import webbrowser
import minecraft_launcher_lib
import subprocess
from tkinter import ttk 
import sys
import psutil
import threading
from PIL import ImageTk, Image

def btn_play():
    loading()
    os.popen("launch.pyw")
    process()

def checkIfProcessRunning(Minecraft):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if Minecraft.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;




def process():

    if checkIfProcessRunning('java.exe'):
        print('Yes minecraft process is running')
        window.quit()
        
    else:
        print('No no process is running')
        process()
    
def btn_discord():
    webbrowser.open_new_tab("https://discord.gg/aAjvfRDSZd")

def btn_settings():
    os.popen("config.txt")

window = Tk()
window.title("Drako Client")
window.iconbitmap("icon.ico")
window.geometry("744x300")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 300,
    width = 744,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundv2.png")
background = canvas.create_image(
    400.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_discord,
    relief = "flat")

b0.place(
    x = 569, y = 230,
    width = 145,
    height = 40)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = threading.Thread(target=btn_play).start,
    relief = "flat")

b1.place(
    x = 562, y = 157,
    width = 160,
    height = 50)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_settings,
    relief = "flat")

b2.place(
    x = 623, y = 10,
    width = 100,
    height = 100)

def loading():
    pb = ttk.Progressbar(
        window,
        orient='horizontal',
        mode='indeterminate',
        length=380
    )
    pb.grid(column=0, row=0, columnspan=2, padx=10, pady=200)
    pb.start()
    

window.resizable(False, False)
window.mainloop()
