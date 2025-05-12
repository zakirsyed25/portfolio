import socket
import threading
import time
from collections import defaultdict

REQUEST_LIMIT = 10
TIME_WINDOW = 5  # seconds

ip_requests = defaultdict(list)
blocked_ips = set()

def load_firewall():
    try:
        with open('firewall.txt', 'r') as f:
            for line in f:
                blocked_ips.add(line.strip())
    except FileNotFoundError:
        pass

def log_and_block(ip):
    if ip not in blocked_ips:
        print(f"[!] Blocking IP: {ip}")
        blocked_ips.add(ip)
        with open('firewall.txt', 'a') as f:
            f.write(ip + '\n')

def handle_client(conn, addr):
    ip = addr[0]

    if ip in blocked_ips:
        print(f"[!] Blocked IP attempted connection: {ip}")
        conn.close()
        return

    now = time.time()
    ip_requests[ip] = [t for t in ip_requests[ip] if now - t < TIME_WINDOW]
    ip_requests[ip].append(now)

    if len(ip_requests[ip]) > REQUEST_LIMIT:
        log_and_block(ip)
        conn.close()
        return

    print(f"[+] Connection accepted from {ip}")
    conn.send(b"Hello from secure server\n")
    conn.close()

def start_server():
    load_firewall()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen()

    print("[*] Server is running on port 8080...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
