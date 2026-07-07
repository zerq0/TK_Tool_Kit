import argparse
import time
from scanner import scan_port
from ports import parse_ports

def main():
    open_ports = 0
    closed_ports = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--ports", required=True)
    parser.add_argument("--timeout", required=True, type=int)
    parser.add_argument("--onlyopen")   
    args = parser.parse_args()
    ports = parse_ports(args.ports)
    print(f"Scanning {args.host} on ports {ports}")
    for port in ports:
        status,message = scan_port(args.host,port)
        print(message)
        if status == "Open":
            open_ports += 1
        if status == "Closed":
            closed_ports += 1
        time.sleep(args.timeout)
    print(f"Number of open ports: {open_ports}")
    print(f"Number of closed ports: {closed_ports}")
if __name__ == "__main__":
    main()

