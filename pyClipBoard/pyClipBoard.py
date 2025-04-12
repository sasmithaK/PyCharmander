import pyperclip
import time

last_copied = ""

with open("clipboard_log.txt", "a", encoding="utf-8") as f:
    while True:
        try:
            current = pyperclip.paste()
            if current != last_copied:
                last_copied = current
                timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
                f.write(f"{timestamp} {current}\n\n")
                print(f"Saved: {current}")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nClipboard recorder stopped.")
            break