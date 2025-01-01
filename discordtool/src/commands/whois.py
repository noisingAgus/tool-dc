# src/commands/whois.py

import os
from src.utils.colors import green, red, reset
import whois

def whois_lookup(domain):
    # Ejecutar el comando whois (asegúrate de tener instalado whois)
    response = os.system(f"whois {domain}")
    
    # Verificar si el comando whois se ejecutó correctamente
    if response == 0:
        print(green + f"Whois lookup for {domain} completed." + reset)
    else:
        print(red + f"Whois lookup for {domain} failed." + reset)
