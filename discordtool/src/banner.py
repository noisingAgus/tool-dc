

from src.utils.colors import red, grey, light_green, dark_grey, reset

def print_ascii_banner():
    
    banner = red + """
     ▐▄▄▄ ▄▄▄· ▪  ▄▄▄            ▄▄▄▄▄            ▄▄▌  
  ·██▐█ ▀█ ██ ▀▄ █·▪         •██  ▪     ▪     ██•  
▪▄ ██▄█▀▀█ ▐█·▐▀▀▄  ▄█▀▄      ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  
▐▌▐█▌▐█ ▪▐▌▐█▌▐█•█▌▐█▌.▐▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
 ▀▀▀• ▀  ▀ ▀▀▀.▀  ▀ ▀█▄▀▪     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
    """ + reset

    
    description = grey + "Advanced tool for pentesting discord servers" + reset
    version = light_green + " [1.0.0]" + reset

    
    print(banner)
    print(description + version + "\n")  
