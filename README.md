# Internet Outage Logger

## Description
This Python script continuously monitors your internet connection and logs every instance when the internet goes down. It checks for connectivity at regular intervals and writes the date and time of any outages to a log file.

## Features
- **Automated Checking:** The script checks internet connectivity at regular intervals.
- **Logging:** Records the date and time of each detected internet outage.
- **Customizable Interval:** Users can set the interval between connectivity checks.
- **Customizable Target Website:** The script can be easily modified to check connectivity to a website of your choice.

## Installation

### Prerequisites
- Python 3.x
- `requests` library

### Steps
1. **Install Python**: Download and install Python from [python.org](https://www.python.org/). Ensure Python is added to your system's PATH.
2. **Install Requests Library**: Run `pip install requests` to install the necessary Python requests library.
3. **Download the Script**: Download `internet_outage_logger.py` from this repository.

## Usage

1. **Navigate to Script Directory**: Open a command prompt or terminal and navigate to the directory containing `internet_outage_logger.py`.
2. **Run the Script**: Execute the script by running `python internet_outage_logger.py`.
3. **Check the Logs**: The script creates and updates a log file named `internet_outage_log.txt` in the same directory.

## Customization

- **Checking Interval**: Change the interval of connectivity checks by modifying the `time.sleep(interval_in_seconds)` line in the script. The default is set to 60 seconds (1 minute).
- **Target Website**: To change the website used for checking internet connectivity, modify the URL in the `check_internet` function. Replace `"http://www.google.com"` with the URL of your preferred website.

## Contributing

Contributions to the script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
