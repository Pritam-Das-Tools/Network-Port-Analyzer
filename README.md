# 🔍 Network Port Analyzer

**Network Port Analyzer** is a multithreaded TCP port scanning tool built with Python. It scans a range of ports on a given IP address, identifies open and closed ports, and visualizes the results using bar charts. Ideal for network diagnostics, penetration testing, and educational use.

---

## 📌 Features

- ⚡ High-speed scanning using multithreading
- 📈 Visualization of scan results with Matplotlib
- 🧠 Intelligent input validation (IP address and port range)
- 🧪 Lightweight and simple to use
- ✅ Clean terminal output with categorized results

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.7+ installed.

Clone the Repository:
    git clone https://github.com/Pritam-Das-Tools/Network-Port-Analyzer.git
    cd Network-Port-Analyzer

Install the required packages:

```bash
pip install matplotlib
```
```For Running the code port_scanner.py
python port_scanner.py // For running the program with the file extension .py
```
#### Output you might see.

  Enter target IP address: 192.168.1.1
  Enter start port: 20
  Enter end port: 100

###The script will:

Scan all ports in the range

Print open/closed ports in real-time

Show a bar chart summarizing the scan
