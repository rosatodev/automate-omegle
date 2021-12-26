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

def omegleStart():

        tocarTexto = driver.find_element(By.ID, "textbtn")
        tocarTexto.click()

        clickCheck = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[1]/label/input")
        clickCheck.click()

        clickCheck = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[2]/label/input")
        clickCheck.click()

        clickCheck = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[3]/input")
        clickCheck.click()    

        sleep(1)

def seleniumAuto():
    mensaje = mensajeOmegle.get()
    cantidad = cantMensajes.get()

    i = 0

    omegleStart()

    while (i != int(cantidad)):
        if (i % 10 == 0):
            waiting = Label(root, text="Esperando 5 segundos...")
            waiting.pack()
            sleep(5)
        else:
            waiting.pack_forget()

        try:
            writeText = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
            writeText.click()
            writeText.send_keys(mensaje)

            sendText = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button")
            sendText.click()
            
            sleep(0.5)
            
            nextPerson = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
            nextPerson.click()
            sleep(1)

            nextPerson = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
            nextPerson.click()
            sleep(1)

            nextPerson = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
            nextPerson.click()
            sleep(2.5)
            
            i+=1

        except:
            waiting.config(text="Hubo un error, intentando de nuevo...")

    return

options = webdriver.ChromeOptions()
driver = launchBrowser()

driver.execute_script("window.scrollTo(0, window.scrollY + 250)")

root = Tk()
root.title("Omegle Automate")
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




