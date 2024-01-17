import requests
import time
from datetime import datetime

def check_internet():
    try:
        requests.get("http://www.google.com", timeout=10)
        return True
    except requests.ConnectionError:
        return False

def log_outage():
    with open("internet_outage_log.txt", "a") as log_file:
        log_file.write(f"Internet outage detected at: {datetime.now()}\n")

def main():
    while True:
        if not check_internet():
            log_outage()
        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    main()
