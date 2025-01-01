# src/commands/help.py

from src.utils.colors import yellow, magenta, reset

def show_help():
    print("\n" + yellow + "• Commands:" + reset)
    print(magenta + "   ► ipinfo [ip]" + reset)
    print(magenta + "   ► server [ip:port]" + reset)
    print(magenta + "   ► ping [ip]" + reset)
    print(magenta + "   ► trace [ip]" + reset)
    print(magenta + "   ►whois [ip]" + reset)
