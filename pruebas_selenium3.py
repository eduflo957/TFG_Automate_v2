from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el controlador del navegador
driver = webdriver.Chrome()

# Acceder a la página web
driver.get("https://www.clasesprivadas.es/clases-particulares/33-programacion_y_lenguajes/")
driver.maximize_window()
time.sleep(5)
# Esperar a que el botón esté presente en el DOM
wait = WebDriverWait(driver, 10)

# Encontrar el botón y hacer clic en él
#button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Botón de ejemplo')]")))
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'barre')))
#driver.execute_script("arguments[0].click();", button)
time.sleep(5)

button.click()
# Cerrar el navegador
time.sleep(5)
driver.quit()