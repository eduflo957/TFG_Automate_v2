from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el controlador del navegador
driver = webdriver.Chrome()

# Acceder a la página web
driver.get("https://twitter.com/search?q=perro&src=typed_query&f=user")

# Encontrar el botón y hacer clic en él
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Botón de ejemplo')]")))
button.click()

# Cerrar el navegador
driver.quit()