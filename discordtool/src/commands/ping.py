# src/commands/ping.py

import os
from src.utils.colors import green, red, reset

def ping_server(ip):
    # Ejecutar el comando ping en el sistema
    response = os.system(f"ping -n 1 {ip}")
    
    # Verificar si el ping fue exitoso (response == 0 es éxito)
    if response == 0:
        print(green + f"[+] {ip} is reachable." + reset)
    else:
        print(red + f"[-] {ip} is not reachable." + reset)
