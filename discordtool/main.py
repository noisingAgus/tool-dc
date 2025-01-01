# main.py
from colorama import init
from src.banner import print_ascii_banner
from src.commands.help import show_help
from src.commands.ipinfo import ipinfo
from src.commands.server import check_server
from src.commands.ping import ping_server  # Importar el comando ping
from src.commands.trace import trace_route
from src.commands.whois import whois_lookup
from src.utils.colors import grey, red, reset


import sys
sys.stdout.reconfigure(encoding='utf-8')  # Forzar UTF-8 en Windows

# Inicializar colorama
init(autoreset=True)

def main():
    print_ascii_banner()
    print("\n")

    while True:
        # Prompt en gris, flecha en rojo en nueva línea
        print(grey + "windows@tool ~" + reset + "\n" + red + "> " + reset, end="")
        command = input()

        if command == "help":
            show_help()
        elif command.startswith("ipinfo"):
            try:
                _, ip = command.split()
                ipinfo(ip)
            except ValueError:
                print("Usage: ipinfo [ip]")
        elif command.startswith("server"):
            try:
                _, address = command.split()
                ip, port = address.split(":")
                check_server(ip, port)
            except ValueError:
                print("Usage: server [ip:port]")
        elif command.startswith("ping"):  # Comando para hacer ping
            try:
                _, ip = command.split()
                ping_server(ip)
            except ValueError:
                print("Usage: ping [ip]")
        elif command.startswith("trace"):
            try:
                _, destination = command.split()
                trace_route(destination)
            except ValueError:
                print("Usage: trace [destination]")
        elif command.startswith("whois"):
            try:
                _, domain = command.split()
                whois_lookup(domain)
            except ValueError:
                print("Usage: whois [domain]")
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Command not found")

if __name__ == "__main__":
    main()
