from tabnanny import check
import minecraft_launcher_lib
import subprocess
import tkinter 
from tkinter import ttk
from tkinter import *
import sys
import urllib.request
import os
import urllib.request, urllib.error
from zipfile import ZipFile
import glob
import hashlib
import json
import pathlib
import platform
import random
import traceback
import webbrowser
import psutil


#Variables
minecraft_directory = "game_data"
vanilla_version = "1.16.5"
launcher_title = "DrakoClient"
version = minecraft_launcher_lib.forge.find_forge_version(vanilla_version)


#Login
options = minecraft_launcher_lib.utils.generate_test_options()


#Check Folders
def check_game_folder():
    if os.path.exists("game_data/mods"):
        print('game_folder is checked')
        install_mods()
        launch_game()
        
    else:
        os.mkdir("game_data/mods")
        check_game_folder()


#Install Mods
def install_mods():

    try:
        urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=1CHCWm5pJNA7mXcyB-FXr0krGlnjC3cp4', "game_data/mods/pvp_patcher.jar")
        print("loaded mod")
    except urllib.error.HTTPError as e:
        print("failed:", e)


    #2
    try:
            urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=1Iv4WYLp7AWRa4qr9d2DdEqOu7SdntKKQ', "game_data/mods/main_menu.jar")
            print("loaded mod")
    except urllib.error.HTTPError as e:
            print("failed:", e)


    #3
    try:
        urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=1gZsLN-tPcFOgfCVxceUBqAhLcTyZ2LS2', "game_data/mods/keystrokes.jar")
        print("loaded mod")
    except urllib.error.HTTPError as e:
        print("failed:", e)


    #4
    try:
        urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=1X5doPE5-Xv_YA1yJkRVr7M_QjxrVePkH', "game_data/mods/optifine.jar")
        print("loaded mod")
    except urllib.error.HTTPError as e:
        print("failed:", e)

    #5
    try:
        urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=1WY153RcbYisce_4QnuCb8v97PBP35hfd', "game_data/mods/placebo.jar")
        print("loaded mod")
    except urllib.error.HTTPError as e:
        print("failed:", e)


#Launch the Game
def launch_game():
    minecraft_launcher_lib.forge.install_forge_version(version, minecraft_directory)
    full_name_forge_version = version.replace("-", "-forge-")
    command = minecraft_launcher_lib.command.get_minecraft_command(full_name_forge_version,minecraft_directory,options)
    subprocess.call(command)

def start_java_client():
    check_game_folder()


start_java_client()












