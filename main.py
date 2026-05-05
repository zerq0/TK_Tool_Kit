import argparse
from scanner import scan_port
from ports import parse_ports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host")
    parser.add_argument("--ports")
    args = parser.parse_args()
    ports = parse_ports(args.ports)
    for port in ports:
        scan_port(args.host,port)
    
if __name__ == "__main__":
    main()

