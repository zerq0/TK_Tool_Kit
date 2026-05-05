import argparse
from scanner import scan_port
# from ports import parse_ports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host")
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    scan_port(args.host, args.port)
if __name__ == "__main__":
    main()

