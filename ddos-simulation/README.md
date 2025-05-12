# 🛡️ DDoS Attack Simulation & Mitigation

This project simulates a basic DDoS attack on a Python server and demonstrates a simple mitigation mechanism using IP rate limiting and dynamic blocking.

## 📁 Features
- Simulates attack from multiple threads
- Detects IPs sending too many requests
- Automatically blocks IPs by writing to a firewall file

## 🚀 How to Run

1. Start the server:
```
python server.py
```

2. Launch the simulated attack:
```
python attacker.py
```

3. Check `firewall.txt` for blocked IPs.

## 📚 Concepts Used
- DDoS basics
- Python socket programming
- Threading
- Rate limiting
