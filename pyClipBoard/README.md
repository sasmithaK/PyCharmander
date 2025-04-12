## 📋 Clipboard Logger
A simple Python script that monitors your clipboard and logs copied content to a file (clipboard_log.txt) along with a timestamp. Useful for keeping a history of what you copy for reference or debugging purposes.

## 🧰 Features
- Continuously monitors clipboard changes
- Logs new clipboard entries with timestamps
- Saves all logs to a local file

## 💾 Requirements
Install pyperclip

`pip install pyperclip`

## Run the script:

`python clipboard_logger.py`

Start copying text!

The script will check your clipboard every second. 
When it detects new content, it logs it in *clipboard_log.txt* with a timestamp.