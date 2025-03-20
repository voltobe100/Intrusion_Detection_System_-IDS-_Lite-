import scapy.all as scapy
from collections import defaultdict
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Track packet counts per IP
traffic_stats = defaultdict(int)
THRESHOLD = 100  # Set anomaly threshold
MONITOR_TIME = 10  # Monitor traffic every 10 seconds

def packet_callback(packet):
    """Process captured packets."""
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        traffic_stats[src_ip] += 1

def detect_anomalies():
    """Detect unusual traffic activity."""
    logging.info("Analyzing traffic...")
    for ip, count in traffic_stats.items():
        if count > THRESHOLD:
            logging.warning(f"🚨 Anomaly detected: {ip} sent {count} packets in {MONITOR_TIME} sec!")
    traffic_stats.clear()

def main():
    logging.info("Starting IDS Lite - Monitoring Network Traffic...")
    while True:
        scapy.sniff(filter="ip", prn=packet_callback, timeout=MONITOR_TIME)
        detect_anomalies()
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Exiting IDS Lite...")
