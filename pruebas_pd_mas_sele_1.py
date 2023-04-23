import pandas as pd
import webbrowser
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    doc = pd.read_excel("C:/Users/Edu guapo/Desktop/carpetaFicheros/TFG_pruebas_enlaces3.xls", header =None)
    
    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    #Acceder a la primera fila
    columna = doc.iloc[:, 0]
    
    # Mostrar enlaces
    for x in columna:
         print(x)

    driver = webdriver.Chrome()

    for x in columna:
        driver.get(x)
        driver.maximize_window()
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'barre')))
        time.sleep(5)
        button.click()
        time.sleep(5)

    driver.quit()




if __name__=='__main__':
    main()