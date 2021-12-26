# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def launchBrowser():

    options.add_argument("--log-level=OFF")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")
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

    return (mensajeOmegle, cantMensajes)

options = webdriver.ChromeOptions()
driver = launchBrowser()

ingresos()




