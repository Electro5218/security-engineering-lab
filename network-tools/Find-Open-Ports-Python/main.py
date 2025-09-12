import socket
import argparse


def skanowanie_portow(ip, port):
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).settimeout(0.01)
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, port))
        print(f"[+] Port {port} jest otwarty")
    except (socket.timeout, ConnectionRefusedError):
        pass

def main():
    parser = argparse.ArgumentParser(description="Wypisywanie otwartych portow")

    parser.add_argument("ip", type=str, help="Podaj adres ip")
    parser.add_argument("--start", type=int, default=1, help="Początkowy port(domyślnie 1)")
    parser.add_argument("--end", type=int, default=65535, help="końcowy port(domyślnie 65535)")
    args = parser.parse_args()

    ip = args.ip
    start_port = args.start
    end_port = args.end

    print(f"Skanowanie portów TCP na {ip} w zakresie {start_port}-{end_port}")

    for port in range(start_port, end_port+1):
        skanowanie_portow(ip, port)

if __name__ == "__main__":
    main()