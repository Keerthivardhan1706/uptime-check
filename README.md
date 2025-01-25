
# Application Uptime Checker

This is a simple Python-based GUI application to check the uptime status of a given web application URL. The application uses the `requests` library to send HTTP GET requests and provides real-time feedback on whether the given URL is **UP** or **DOWN**, using the `tkinter` library for the graphical interface.

## Features

- Easy-to-use interface:** Enter a URL and check its status with a single click.  
- Error Handling:** Handles invalid URLs, connection errors, and request timeouts.  
- Responsive UI:** The application remains responsive while checking the URL.  
- Status Indication:** Displays results in green (UP) or red (DOWN).  

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**  
- Required Python libraries:

  Install them using:

  ```bash
  pip install requests validators
  ```

## Installation

1. Clone the repository or copy the script to your local machine.

   ```bash
   git clone https://github.com/your-repo/application-uptime-checker.git
   cd application-uptime-checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python uptime_checker.py
   ```

## Usage

1. Open the application.
2. Enter a valid URL in the input field (e.g., `https://www.google.com`).
3. Click **"Check Status"** to see whether the application is UP or DOWN.
4. The result will be displayed in the interface.

## Example

- **Input:** `https://www.google.com`  
  **Output:** `The application at https://www.google.com is UP.`  

- **Input:** `https://invalid-url.com`  
  **Output:** `The application at https://invalid-url.com is DOWN.`  

---

Let me know if you need any further changes!
