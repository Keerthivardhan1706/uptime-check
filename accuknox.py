import requests
import tkinter as tk
from tkinter import messagebox

def check_application_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"The application at {url} is UP."
        else:
            return f"The application at {url} is DOWN. Status code: {response.status_code}"
    except requests.ConnectionError:
        return f"The application at {url} is DOWN. Connection error occurred."
    except requests.Timeout:
        return f"The application at {url} is DOWN. Request timed out."
    except Exception as e:
        return f"The application at {url} is DOWN. Error: {e}"

def check_status():
    url = url_entry.get().strip()
    if url:
        status = check_application_status(url)
        result_label.config(text=status, fg="green" if "UP" in status else "red")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")

# Create GUI
root = tk.Tk()
root.title("Application Uptime Checker")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Application URL:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

tk.Button(root, text="Check Status", font=("Arial", 12), bg="#4CAF50", fg="white", command=check_status).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
