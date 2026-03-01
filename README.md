# Port Scanner

A Python-based multithreaded Port Scanner that scans a target host for open ports and retrieves basic service information using banner grabbing.

---

## Features

- Scan a range of TCP ports
- Detect open ports
- Banner grabbing for service identification
- Multithreaded scanning for faster performance
- Command-line interface (CLI)
- Colored output using Colorama
- Option to save results to a file

---

## How It Works

1. Takes target host and port range as input  
2. Resolves domain to IP address  
3. Scans ports using multithreading  
4. Identifies open ports  
5. Attempts to grab service banner  
6. Displays results and optionally saves them to a file  

---

## Installation

Make sure Python 3.8 or higher is installed.

Clone the repository:

git clone https://github.com/oo7-dev/port-scanner.git

cd port-scanner


Install dependencies:
pip install -r requirements.txt


---

## Usage

Basic scan:

python main.py -t scanme.nmap.org -p 1-100

Save results to a file:
python main.py -t scanme.nmap.org -p 1-100 -o results.txt

---

## Example Target (Safe for Testing)

Use the official test server:

- scanme.nmap.org

---

## Project Structure

port-scanner/
│
├── main.py
├── scanner.py
├── banner.py
├── requirements.txt
└── README.md

---

## Technologies Used

- Python
- Socket Programming
- ThreadPoolExecutor (Multithreading)
- Argparse
- Colorama

---

## Disclaimer

This tool is created for educational and ethical testing purposes only.  
Do not scan systems without proper authorization.

---

## Author

Dev  
Computer Engineering Student | Cybersecurity Enthusiast