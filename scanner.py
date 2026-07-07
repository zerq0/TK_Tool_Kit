import socket
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) 
            result = s.connect_ex((host, port))
            if result == 0:
                return "Open", f"Port {port} is open on host {host}"
            else:
                return "Closed", f"Port {port} is closed on host {host}"
    except Exception as e:
        return "Error", f"Error scanning port {port} on host {host}"
# scan_port('localhost', 80) works