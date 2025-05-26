from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")

def caso_1_login_correcto():
    driver.refresh()
    usuario = driver.find_element(By.ID, "usuario")
    clave = driver.find_element(By.ID, "clave")
    boton = driver.find_element(By.TAG_NAME, "button")

    usuario.send_keys("admin")
    clave.send_keys("1234")
    boton.click()
    time.sleep(1)
    mensaje = driver.find_element(By.ID, "mensaje").text
    assert mensaje == "Bienvenido admin", "Error en login correcto"

def caso_2_login_usuario_incorrecto():
    driver.refresh()
    driver.find_element(By.ID, "usuario").send_keys("root")
    driver.find_element(By.ID, "clave").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    assert "Credenciales incorrectas" in driver.find_element(By.ID, "mensaje").text

def caso_3_login_clave_incorrecta():
    driver.refresh()
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "clave").send_keys("0000")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    assert "Credenciales incorrectas" in driver.find_element(By.ID, "mensaje").text

def caso_4_login_campos_vacios():
    driver.refresh()
    driver.find_element(By.ID, "usuario").clear()
    driver.find_element(By.ID, "clave").clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    assert "Credenciales incorrectas" in driver.find_element(By.ID, "mensaje").text

def caso_5_login_espacios_blancos():
    driver.refresh()
    driver.find_element(By.ID, "usuario").send_keys("   ")
    driver.find_element(By.ID, "clave").send_keys("   ")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    assert "Credenciales incorrectas" in driver.find_element(By.ID, "mensaje").text

# Ejecutar los 5 casos
caso_1_login_correcto()
caso_2_login_usuario_incorrecto()
caso_3_login_clave_incorrecta()
caso_4_login_campos_vacios()
caso_5_login_espacios_blancos()

driver.quit()
