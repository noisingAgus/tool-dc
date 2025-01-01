import whois
import sys

def whois_lookup(domain):
    try:
        # Realizar la consulta WHOIS del dominio
        domain_info = whois.whois(domain)
        
        # Imprimir la información del dominio
        if domain_info:
            print(f"WHOIS Information for {domain}:\n")
            for key, value in domain_info.items():
                # Mostrar cada campo de la información
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"WHOIS information not found for {domain}.")
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python whois_lookup.py [domain]")
        sys.exit(1)

    domain = sys.argv[1]
    whois_lookup(domain)

if __name__ == "__main__":
    main()
