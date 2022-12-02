# Importar librerias
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pyautogui
import keyboard
from selenium.webdriver.support.ui import Select
import random

keyboard.press('f11')
print(
    '''
 /$$$$$$$$                  /$$                               /$$                           /$$$$$$$                                            /$$
| $$_____/                 | $$                              |__/                          | $$__  $$                                          | $$
| $$    /$$    /$$ /$$$$$$ | $$ /$$   /$$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$
| $$$$$|  $$  /$$/|____  $$| $$| $$  | $$ |____  $$ /$$_____/| $$ /$$__  $$| $$__  $$      | $$  | $$ /$$__  $$ /$$_____/ /$$__  $$| $$__  $$|_  $$_/   /$$__  $$
| $$__/ \  $$/$$/  /$$$$$$$| $$| $$  | $$  /$$$$$$$| $$      | $$| $$  \ $$| $$  \ $$      | $$  | $$| $$  \ $$| $$      | $$$$$$$$| $$  \ $$  | $$    | $$$$$$$$
| $$     \  $$$/  /$$__  $$| $$| $$  | $$ /$$__  $$| $$      | $$| $$  | $$| $$  | $$      | $$  | $$| $$  | $$| $$      | $$_____/| $$  | $$  | $$ /$$| $$_____/
| $$$$$$$$\  $/  |  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/| $$  | $$      | $$$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$
|________/ \_/    \_______/|__/ \______/  \_______/ \_______/|__/ \______/ |__/  |__/      |_______/  \______/  \_______/ \_______/|__/  |__/   \___/   \_______/

Desarrollado por: Josue Eguia
    '''
)

str_control = input("Ingrese su numero de control: ")
str_correo=f'l{str_control}@nlaredo.tecnm.mx'
str_password = input("Ingrese su contraseña: ")

while True:
    opcion = int(input("Seleccione el navegador: \n1) Edge\n2) Chrome\n3) Firefox\n !!!! Seleccionar uno que tenga "
                       "instalado !!!\nOpcion: "))
    if opcion==1 or opcion==2 or opcion==3:
        break
    else:print('\nOpcion no valida\n')

if (opcion == 1):
    driver = webdriver.Edge()
elif (opcion == 2):
    driver = webdriver.Chrome()
else:
    driver = webdriver.Firefox()

driver.maximize_window()

driver.get('https://siie.nlaredo.tecnm.mx/Identity/Account/login')

email = driver.find_element(By.ID, 'Input_Email')
email.send_keys(str_correo)

password = driver.find_element(By.ID, 'Input_Password')
password.send_keys(str_password)

password.submit()

op = driver.find_element(By.LINK_TEXT, 'Evaluación Docente').click()

if (op):
    texto = driver.find_element(By.TAG_NAME, 'h3')
    cantidad_preguntas_texto = texto.find_element(By.TAG_NAME, 'span').text
    cantidad_preguntas = cantidad_preguntas_texto.split('/')
    cant = int(cantidad_preguntas[1])

    for _ in range(cant - 1):  # Cambiar a cant-1
        form = driver.find_element(By.ID, 'formPregunta')
        selects = driver.find_elements(By.CLASS_NAME, 'form-control')

        for select in selects:
            selected = Select(select)
            selected.select_by_value(str(random.randint(3, 4)))

    form.submit()
    driver.find_element(By.LINK_TEXT, 'Generar el comprobante').click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)
    driver.quit()
    time.sleep(1)
    keyboard.press('esc')
else :
    driver.find_element(By.LINK_TEXT, 'Generar el comprobante').click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)
    driver.quit()
    time.sleep(1)
    keyboard.press('esc')