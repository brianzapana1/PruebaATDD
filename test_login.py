from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")

def esperar(ms=2):
    time.sleep(ms)

def caso_1_login_correcto():
    print("🧪 Caso 1: Login correcto")
    driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")
    esperar(1)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    esperar(1)
    driver.find_element(By.ID, "clave").send_keys("1234")
    esperar(1)
    driver.find_element(By.ID, "login").click()
    esperar(2)

    assert "bienvenido.html" in driver.current_url, "❌ No se redirigió a bienvenido.html"
    print("✅ Login correcto detectado\n")

def caso_2_login_usuario_incorrecto():
    print("🧪 Caso 2: Usuario incorrecto")
    driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")
    esperar(1)

    driver.find_element(By.ID, "usuario").send_keys("root")
    esperar(1)
    driver.find_element(By.ID, "clave").send_keys("1234")
    esperar(1)
    driver.find_element(By.ID, "login").click()
    esperar(2)

    mensaje = driver.find_element(By.ID, "mensaje").text.strip()
    assert mensaje == "Credenciales incorrectas", "❌ Usuario incorrecto no detectado"
    print("✅ Usuario incorrecto detectado\n")

def caso_3_login_clave_incorrecta():
    print("🧪 Caso 3: Contraseña incorrecta")
    driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")
    esperar(1)

    driver.find_element(By.ID, "usuario").send_keys("admin")
    esperar(1)
    driver.find_element(By.ID, "clave").send_keys("0000")
    esperar(1)
    driver.find_element(By.ID, "login").click()
    esperar(2)

    mensaje = driver.find_element(By.ID, "mensaje").text.strip()
    assert mensaje == "Credenciales incorrectas", "❌ Contraseña incorrecta no detectada"
    print("✅ Contraseña incorrecta detectada\n")

def caso_4_login_campos_vacios():
    print("🧪 Caso 4: Campos vacíos")
    driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")
    esperar(1)

    driver.find_element(By.ID, "usuario").clear()
    driver.find_element(By.ID, "clave").clear()
    esperar(1)
    driver.find_element(By.ID, "login").click()
    esperar(2)

    mensaje = driver.find_element(By.ID, "mensaje").text.strip()
    assert mensaje == "Por favor complete todos los campos", "❌ Campos vacíos no detectados"
    print("✅ Campos vacíos detectados\n")

def caso_5_login_espacios_blancos():
    print("🧪 Caso 5: Espacios en blanco")
    driver.get("file:///C:/Users/user/OneDrive/Escritorio/PRUEBA%20ATDD/login.html")
    esperar(1)

    driver.find_element(By.ID, "usuario").send_keys("   ")
    driver.find_element(By.ID, "clave").send_keys("   ")
    esperar(1)
    driver.find_element(By.ID, "login").click()
    esperar(2)

    mensaje = driver.find_element(By.ID, "mensaje").text.strip()
    assert mensaje == "Por favor complete todos los campos", "❌ Espacios en blanco no detectados"
    print("✅ Espacios en blanco detectados\n")

# Ejecutar todos los casos con pausa entre cada uno
caso_1_login_correcto()
esperar(2)
caso_2_login_usuario_incorrecto()
esperar(2)
caso_3_login_clave_incorrecta()
esperar(2)
caso_4_login_campos_vacios()
esperar(2)
caso_5_login_espacios_blancos()
esperar(2)

print("🎉 Todos los casos pasaron correctamente.")
driver.quit()
