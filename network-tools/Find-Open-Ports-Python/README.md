# TCP Port Scanner

A simple program for scanning a network to find **open TCP ports** on a specified host.

> ⚠️ **Warning:** This program is **single-threaded**, so scanning all ports may take a long time. Use it only for testing in a lab environment or on systems you are authorized to scan.

---

## Features
- Attempts a TCP connection to the specified range of ports.
- Marks a port as **open** if the connection is successful.
- Does not require any external libraries (uses standard Python only).

---

## Requirements
- Python 3.x
- Access to the network you are scanning (authorization required!)

---

## Usage

```bash
python port_scanner.py --start <start_port> --end <end_port> --ip <target_ip>

