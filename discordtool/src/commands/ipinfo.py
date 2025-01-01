from src.utils.colors import yellow, reset, red
from src.utils.ip_lookup import get_ip_info

def ipinfo(ip):
    print(red + "[#] " + reset + "Getting data from the entered IP...\n")
    
    # Obtener los datos de la IP
    data = get_ip_info(ip)
    
    location = data.get('location', 'N/A')
    if location != 'N/A':
        lat, lon = location.split(',')  # Separar latitud y longitud
        location = f"Lat: {lat}, Lon: {lon}"
    
    # Mostrar los resultados formateados
    print(f"{yellow}► IP:{reset} {ip}")
    print(f"{yellow}► Hostname:{reset} {data.get('hostname', 'N/A')}")
    print(f"{yellow}► City:{reset} {data.get('city', 'N/A')}")
    print(f"{yellow}► Region:{reset} {data.get('region', 'N/A')}")
    print(f"{yellow}► Country:{reset} {data.get('country', 'N/A')}")
    print(f"{yellow}► Location:{reset} {location}")
    print(f"{yellow}► Org:{reset} {data.get('org', 'N/A')}")
    print(f"{yellow}► Postal Code:{reset} {data.get('postal_code', 'N/A')}")
    print(f"{yellow}► Timezone:{reset} {data.get('timezone', 'N/A')}")
