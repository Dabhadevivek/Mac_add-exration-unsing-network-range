# Mac_add-exration-unsing-network-range
Basic network scanner written in Python using the Scapy library. It performs an ARP (Address Resolution Protocol) scan on a given target IP address or IP range to discover devices connected to a network



# Network Scanner Project

## Description
This project provides a simple network scanner application using Flask and Selenium. The Flask application performs network scanning and the Selenium script automates input and output handling.

## Setup

1. **Clone the repository**:

    ```sh
    git clone <repository-url>
    cd network_scanner
    ```

2. **Create and activate a Python virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```sh
    python app.py
    ```

5. **Run the Selenium script**:

    Ensure the Flask application is running, then execute:

    ```sh
    python selenium_script.py
    ```

## Notes

- Ensure you have ChromeDriver or the appropriate WebDriver installed for Selenium.
- Adjust the IP range in the Selenium script as needed.

