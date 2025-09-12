# NBPAPI – Currency Rate Checker

This Python script fetches the **average exchange rates** for a given currency from the **National Bank of Poland (NBP)** for the last 5 days and calculates the differences between consecutive days.

> ⚠️ **Disclaimer:** This script is intended for **educational and personal use only**.

---

## Features
- Fetches currency data from the NBP API.
- Displays the average exchange rate for each of the last 5 days.
- Calculates the difference between consecutive days.
- Easy-to-use command-line interface.

---

## Requirements
- Python 3.x  
- `requests` library

---

Install the `requests` library if you don't have it:
```bash
pip install requests
```

---

Run the script from the command line with the currency code as an argument: 
```bash
python NBPAPI.py <CURRENCY_CODE>
``` 