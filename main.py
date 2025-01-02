# import tkinter as tk
from tkinter import messagebox
import platform
import pyautogui
import threading

# Check the OS and import the appropriate library
if platform.system() == "Windows":
    import keyboard
else:
    from pynput import keyboard as pynput_keyboard
    from pynput.keyboard import Controller

class HotkeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotkey Typing App")

        # Variables
        self.hotkey = "caps lock"  # Default hotkey
        self.text_to_type = tk.StringVar()

        # Input box
        tk.Label(root, text="Input Text:").pack(pady=5)
        self.input_box = tk.Entry(root, textvariable=self.text_to_type, width=50)
        self.input_box.pack(pady=5)

        # Button to set hotkey
        self.set_hotkey_button = tk.Button(root, text="Set Hotkey", command=self.set_hotkey)
        self.set_hotkey_button.pack(pady=10)

        # Label to display the set hotkey
        self.hotkey_label = tk.Label(root, text=f"Hotkey set: {self.hotkey}", fg="blue")
        self.hotkey_label.pack(pady=5)

        # Register the default hotkey
        self.bind_hotkey()

        # Unregister hotkey on app close
        self.root.protocol("WM_DELETE_WINDOW", self.cleanup)

    def set_hotkey(self):
        if platform.system() == "Windows":
            self.set_hotkey_windows()
        else:
            self.set_hotkey_linux()

    def set_hotkey_windows(self):
        def on_key(event):
            self.hotkey = event.name
            self.hotkey_label.config(text=f"Hotkey set: {self.hotkey}")
            keyboard.unhook_all()  # Stop listening after key is set
            messagebox.showinfo("Hotkey Set", f"Hotkey '{self.hotkey}' has been set!")
            self.bind_hotkey()

        messagebox.showinfo("Set Hotkey", "Press any key to set as hotkey.")
        keyboard.hook(on_key)  # Hook to capture key press

    def set_hotkey_linux(self):
        def on_press(key):
            try:
                self.hotkey = key.char or str(key)
            except AttributeError:
                self.hotkey = str(key)
            self.hotkey_label.config(text=f"Hotkey set: {self.hotkey}")
            self.listener.stop()
            messagebox.showinfo("Hotkey Set", f"Hotkey '{self.hotkey}' has been set!")
            self.bind_hotkey()

        messagebox.showinfo("Set Hotkey", "Press any key to set as hotkey.")
        self.listener = pynput_keyboard.Listener(on_press=on_press)
        self.listener.start()

    def bind_hotkey(self):
        if platform.system() == "Windows":
            keyboard.unhook_all_hotkeys()
            if self.hotkey:
                keyboard.add_hotkey(self.hotkey, self.type_text)
        else:
            self.start_pynput_listener()

    def start_pynput_listener(self):
        def listen_for_hotkey():
            with pynput_keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()

        # Run the listener in a separate thread to avoid freezing the GUI
        thread = threading.Thread(target=listen_for_hotkey, daemon=True)
        thread.start()

    def on_press(self, key):
        try:
            if key.char == self.hotkey or str(key) == self.hotkey:
                self.type_text()
        except AttributeError:
            if str(key) == self.hotkey:
                self.type_text()

    def type_text(self):
        text = self.text_to_type.get()
        if text.strip():
            pyautogui.typewrite(text)
        else:
            messagebox.showwarning("Empty Input", "The input text is empty!")

    def cleanup(self):
        if platform.system() == "Windows":
            keyboard.unhook_all()
        else:
            if hasattr(self, 'listener') and self.listener:
                self.listener.stop()
        self.root.destroy()


if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    app = HotkeyApp(root)
    root.mainloop()
