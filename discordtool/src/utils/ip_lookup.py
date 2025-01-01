import requests

def get_ip_info(ip):
    
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url)
        data = response.json()  # Convertir la respuesta JSON en un diccionario
        
        # Retornar los datos relevantes o un valor por defecto si no existen
        return {
            'hostname': data.get('hostname', 'N/A'),
            'city': data.get('city', 'N/A'),
            'region': data.get('region', 'N/A'),
            'country': data.get('country', 'N/A'),
            'location': data.get('loc', 'N/A'),
            'org': data.get('org', 'N/A'),
            'postal_code': data.get('postal', 'N/A'),
            'timezone': data.get('timezone', 'N/A')
        }
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {
            'hostname': 'N/A',
            'city': 'N/A',
            'region': 'N/A',
            'country': 'N/A',
            'location': 'N/A',
            'org': 'N/A',
            'postal_code': 'N/A',
            'timezone': 'N/A'
        }
