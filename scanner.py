import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) 
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open on {host}.")
            else:
                print(f"Port {port} is closed on {host}.")
    except Exception as e:
        print(f"Error scanning port {port} on {host}: {e}")

# scan_port('localhost', 80) works