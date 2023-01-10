import pandas as pd
import webbrowser
from urllib.request import urlopen

def main():
    doc = pd.read_excel("C:/Users/Edu guapo/Desktop/afueraEstudios/TFG_enlaces.xls", header =None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    arrayEnlaces = []
    
    for x in range (0,tamFilas):
        arrayEnlaces.append(doc.iloc[x].to_string(index=False))
        print('"'+arrayEnlaces[x]+'"')
        webbrowser.open(arrayEnlaces[x], new=0, autoraise=True)

    # url = "https://twitter.com/SoyHijoDelPerro"
    # webbrowser.open(url, new=0, autoraise=True) 

if __name__=='__main__':
    main()