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

     _         _                        _   _           
    / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___ ___  
   / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __/ _ \ 
  / ___ \ |_| | || (_) | | | | | | (_| | |_| | (_| (_) |
 /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___\___/ 
                                                        
    
    
    '''
)

str_correo = input("Ingrese su correo electrónico institucional: ")
str_password = input("Ingrese su contraseña: ")

driver = webdriver.Edge()

driver.maximize_window()

driver.get('https://siie.nlaredo.tecnm.mx/')

driver.find_element(By.CLASS_NAME, 'btn-get-started').click()

email = driver.find_element(By.ID, 'Input_Email')
email.send_keys(str_correo)

password = driver.find_element(By.ID, 'Input_Password')
password.send_keys(str_password)

password.submit()

driver.find_element(By.LINK_TEXT, 'Evaluación Docente').click()

texto = driver.find_element(By.TAG_NAME, 'h3')
cantidad_preguntas_texto = texto.find_element(By.TAG_NAME, 'span').text
cantidad_preguntas = cantidad_preguntas_texto.split('/')
cant = int(cantidad_preguntas[1])

for _ in range(cant): # Cambiar a cant-1
    form = driver.find_element(By.ID, 'formPregunta')
    selects = driver.find_elements(By.CLASS_NAME, 'form-control')

    for select in selects:
        selected = Select(select)
        selected.select_by_value('3')

    form.submit()

driver.find_element(By.LINK_TEXT, 'Generar el comprobante').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.press('enter')

time.sleep(2)
driver.quit()
time.sleep(1)
keyboard.press('esc')
