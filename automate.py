# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from tkinter import *

def launchBrowser():

    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    #options.add_argument("--headless")
    options.add_argument("--incognito")
    

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome( options=options , service=s)
    driver.set_window_size(709, 1200)

    driver.get('https://www.omegle.com')
    return driver

        # leerArchivo = driver.find_element(By.ID, "MainContent_lbProgressFile2")

def seleniumAuto():
    mensaje = mensajeOmegle.get()
    cantidad = cantMensajes.get()


    

    return

options = webdriver.ChromeOptions()
driver = launchBrowser()

driver.execute_script("window.scrollTo(0, window.scrollY + 250)")

root = Tk()
root.geometry("500x200")

l_mensajeOmegle = Label(root, text="Mensaje a Spammear en Omegle")
l_mensajeOmegle.pack()

mensajeOmegle = Entry(root, width=30)
mensajeOmegle.pack()

l_cantMensajes = Label(root, text="Cantidad de repeticiones del mensaje")
l_cantMensajes.pack()

cantMensajes = Entry(root, width=30)
cantMensajes.pack()

btn_enviar = Button(root, text="Enviar",width=30,height=5, command=seleniumAuto)
btn_enviar.pack(pady=20)


root.mainloop()




