# src/commands/trace.py

import os
from src.utils.colors import green, red, reset

def trace_route(destination):
    # Ejecutar el comando tracert (traceroute) en Windows
    response = os.system(f"tracert {destination}")
    
    # Verificar si el traceroute fue exitoso
    if response == 0:
        print(green + f"Traceroute to {destination} completed." + reset)
    else:
        print(red + f"Traceroute to {destination} failed." + reset)
