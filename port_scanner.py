import socket
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
from datetime import datetime

# Global dictionaries to store results
results = {"open": [], "closed": []}

# Function to scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                results["open"].append(port)
            else:
                results["closed"].append(port)
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

# Visualization function
def show_chart():
    categories = ['Open', 'Closed']
    counts = [len(results["open"]), len(results["closed"])]

    plt.figure(figsize=(6,4))
    plt.bar(categories, counts, color=['green', 'red'])
    plt.title('Port Scan Results')
    plt.ylabel('Number of Ports')
    plt.show()

def main():
    print("=== Multithreaded Port Scanner with Visualization ===")
    target_ip = input("Enter target IP address: ").strip()

    # Validate IP
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("❌ Invalid IP address.")
        return

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("❌ Invalid port range.")
        return

    ports = range(start_port, end_port + 1)
    print("\n🔍 Scanning ports...")

    start_time = datetime.now()

    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, target_ip, port)

    duration = datetime.now() - start_time

    # Summary
    print(f"\n✅ Scan complete in {duration}.")
    print(f"🔓 Open ports: {results['open']}")
    print(f"🔐 Closed ports: {len(results['closed'])}")

    # Show results
    show_chart()

if __name__ == "__main__":
    main()
