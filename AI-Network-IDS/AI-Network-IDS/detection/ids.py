print("AI Network Intrusion Detection System Started")

suspicious_ips = ["192.168.1.10", "10.0.0.5"]

def check_traffic(ip):
    if ip in suspicious_ips:
        print(f"ALERT: Suspicious activity detected from {ip}")
    else:
        print(f"Safe traffic from {ip}")

check_traffic("192.168.1.10")
check_traffic("192.168.1.20")
