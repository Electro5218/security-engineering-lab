# Security Engineering Lab

This repository contains educational security projects focused on **network security** and **IoT experimentation**. The projects included are **ESP32 Jammer** and **Find Open Ports**, both intended for **learning and lab purposes only**.

> ⚠️ **Disclaimer:** Do **not** use these tools on live systems or networks without proper authorization. The author is **not responsible** for any misuse.

---

## ESP32 Jammer

**Technologies:** ESP32, BlueFlasher.exe, IoT hardware  
**Description:**  
This is an educational IoT project simulating jamming attacks in a controlled lab environment. The device can disrupt wireless communication in the 2.4GHz band, including Wi-Fi, Bluetooth, and other remote-controlled devices. It is intended **only for lab networks and educational purposes**.

**Usage Instructions:**  
1. Download the latest **BlueFlasher.exe**.  
2. Run the application.  
3. Select the COM port corresponding to your ESP32 device.  
4. Hold down the **Boot** button on the ESP32.  
5. Choose the firmware you want to flash.  
6. Release the **Boot** button.  
7. Wait until the firmware is flashed (check the console for confirmation).  

---

## Find Open Ports

**Technologies:** Python, socket  
**Description:**  
A single-threaded TCP port scanner. Attempts to connect to each port in the specified range. If the connection succeeds, the port is considered **open**.

**Usage:**  
```bash
python port_scanner.py --start <start_port> --end <end_port> --ip <target_ip>
```

## NBP API
---
**Technologies:** Python, requests library
**Description:**  
This Python script fetches the average exchange rates for a given currency from the National Bank of Poland (NBP) for the last 5 days and calculates the differences between consecutive days. Intended for educational and personal use only.

**Usage:**
```bash
python NBPAPI.py <CURRENCY_CODE>
```