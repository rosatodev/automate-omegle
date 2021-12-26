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
    options.add_argument("--headless")
    options.add_argument("--incognito")
    

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome( service_log_path='/dev/null', service=s)
    driver.set_window_size(709, 1200)

    driver.get('https://www.omegle.com')
    return driver

def ingresos():
    mensajeOmegle = input("Ingresa el texto que queres spammear en Omegle: ")
    while (mensajeOmegle == ""):
        mensajeOmegle = input("Ingresa el texto que queres spammear en Omegle: ")

    cantMensajes = int(input("Ingrese cantidad de veces que quiera enviar el mensaje: "))
    while (cantMensajes < 0):
        cantMensajes = int(input("ERROR, el valor ingresado es inválido, intente de nuevo.\n\nIngrese cantidad de veces que quiera enviar el mensaje: "))

    # leerArchivo = driver.find_element(By.ID, "MainContent_lbProgressFile2")

    return (mensajeOmegle, cantMensajes)

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


ingresos()

root.mainloop()




