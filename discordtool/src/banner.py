# src/banner.py

from src.utils.colors import red, grey, light_green, dark_grey, reset

def print_ascii_banner():
    # Arte ASCII personalizado
    banner = red + """
     ▐▄▄▄ ▄▄▄· ▪  ▄▄▄            ▄▄▄▄▄            ▄▄▌  
  ·██▐█ ▀█ ██ ▀▄ █·▪         •██  ▪     ▪     ██•  
▪▄ ██▄█▀▀█ ▐█·▐▀▀▄  ▄█▀▄      ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  
▐▌▐█▌▐█ ▪▐▌▐█▌▐█•█▌▐█▌.▐▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
 ▀▀▀• ▀  ▀ ▀▀▀.▀  ▀ ▀█▄▀▪     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
    """ + reset

    # Texto de descripción en gris oscuro y versión en verde claro
    description = grey + "Advanced tool for pentesting discord servers" + reset
    version = light_green + " [1.0.0]" + reset

    # Imprimir el banner y la descripción en la forma deseada
    print(banner)
    print(description + version + "\n")  # Concatenamos el texto y la versión en un solo print