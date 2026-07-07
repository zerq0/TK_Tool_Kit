import argparse
import time
from scanner import scan_port
from ports import parse_ports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--ports", required=True)
    parser.add_argument("--timeout", required=True, type=int)
    parser.add_argument("--onlyopen")   
    args = parser.parse_args()
    ports = parse_ports(args.ports)
    for port in ports:
        scan_port(args.host,port)
        time.sleep(args.timeout)
if __name__ == "__main__":
    main()

