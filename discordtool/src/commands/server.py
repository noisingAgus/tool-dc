# server.py
import socket
import time
from src.utils.colors import red, yellow, reset

def check_server(ip, ports=None):
    # Si no se pasan puertos, se verifican los puertos comunes
    if ports is None:
        ports = [80, 443, 21, 22, 25, 3389]  # Puertos comunes: HTTP, HTTPS, FTP, SSH, etc.
    
    for port in ports:
        try:
            # Medir el tiempo de conexión
            start_time = time.time()
            
            # Crear el socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            
            # Intentar conectarse al puerto
            result = s.connect_ex((ip, int(port)))
            
            # Verificar si la conexión fue exitosa
            if result == 0:
                # Si la conexión fue exitosa, calcular el tiempo
                end_time = time.time()
                duration = end_time - start_time
                print(yellow + f"[+] Server {ip}:{port} is reachable. Connection took {duration:.3f} seconds." + reset)
                
                # Enviar una solicitud mínima HTTP para obtener el banner (si es HTTP/HTTPS)
                if port == 80 or port == 443:
                    try:
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')  # Solicitar el encabezado
                        banner = s.recv(1024)  # Intentar obtener una respuesta del servidor
                        print(yellow + f"  Banner: {banner.decode('utf-8', 'ignore')}" + reset)
                    except Exception as e:
                        print(red + f"  [!] Error while getting banner: {e}" + reset)
            else:
                print(red + f"[-] Server {ip}:{port} is not reachable or port is closed. Result code: {result}" + reset)
            
            s.close()
        
        except socket.timeout:
            print(red + f"[-] Server {ip}:{port} timed out." + reset)
        except ConnectionRefusedError:
            print(red + f"[-] Server {ip}:{port} refused the connection." + reset)
        except socket.gaierror:
            print(red + f"[-] Invalid hostname or IP address: {ip}" + reset)
        except Exception as e:
            print(red + f"[!] An error occurred with port {port}: {e}" + reset)

