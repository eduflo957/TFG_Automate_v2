import pandas as pd
import webbrowser
from urllib.request import urlopen

def main():
    doc = pd.read_excel("C:/Users/Edu guapo/Desktop/carpetaFicheros/TFG_pruebas_enlaces3.xls", header =None)
    
    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    #Acceder a la primera fila
    columna = doc.iloc[:, 0]
    
    for x in columna:
         print(x)

if __name__=='__main__':
    main()