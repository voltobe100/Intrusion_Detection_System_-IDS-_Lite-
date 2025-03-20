# Intrusion Detection System (IDS) Lite

A lightweight Python-based **Intrusion Detection System (IDS)** that monitors network traffic and detects anomalies using packet analysis.

## Features

✅ **Monitors network traffic** using Scapy  
✅ **Detects anomalies** based on packet volume  
✅ **Threshold-based detection** to flag unusual activity  
✅ **Logging support** for easy debugging  
✅ **Cross-platform support** (Linux & Windows with admin privileges)

## Installation

Ensure you have **Python 3.x** installed.  
Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/IDS-Lite.git
cd IDS-Lite
```

### Install Dependencies

```bash
pip install scapy
```

## Usage

Run the script with administrative privileges:

```bash
sudo python ids_lite.py  # Linux/Mac
python ids_lite.py       # Windows (Run as Admin)
```

## Requirements

- **Python 3.x**
- **Scapy** for network packet analysis
- **Administrator/root privileges** to capture network traffic

## License

This project is licensed under the **MIT License**.
