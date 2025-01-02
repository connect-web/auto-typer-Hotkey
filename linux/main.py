import tkinter as tk
from tkinter import messagebox
from time import sleep
from pynput import keyboard
from pynput.keyboard import Controller

pynput_keyboard_controller = Controller()


class HotkeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotkey Typing App")

        # Variables
        self.hotkey = None  # Hotkey will be set later
        self.text_to_type = tk.StringVar()

        # Input box
        tk.Label(root, text="Input Text:").pack(pady=5)
        self.input_box = tk.Entry(root, textvariable=self.text_to_type, width=50)
        self.input_box.pack(pady=5)

        # Button to set hotkey
        self.set_hotkey_button = tk.Button(root, text="Set Hotkey", command=self.set_hotkey)
        self.set_hotkey_button.pack(pady=10)

        # Label to display the set hotkey
        self.hotkey_label = tk.Label(root, text="Hotkey set: None", fg="blue")
        self.hotkey_label.pack(pady=5)

        # Unregister hotkey on app close
        self.root.protocol("WM_DELETE_WINDOW", self.cleanup)

        # Start hotkey listener
        self.listener = None

    def set_hotkey(self):
        # Prompt user for hotkey
        def on_press(key):
            try:
                self.hotkey = key.char  # Use character for alphanumeric keys
            except AttributeError:
                self.hotkey = str(key)  # Use key name for special keys
            self.hotkey_label.config(text=f"Hotkey set: {self.hotkey}")
            messagebox.showinfo("Hotkey Set", f"Hotkey '{self.hotkey}' has been set!")
            self.start_listener()  # Restart the listener with the new hotkey
            return False  # Stop capturing after one key press

        messagebox.showinfo("Set Hotkey", "Press any key to set as hotkey.")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def start_listener(self):
        # Stop any existing listener
        if self.listener:
            self.listener.stop()

        # Start a new listener
        def on_press(key):
            try:
                if key.char == self.hotkey:  # Check if pressed key matches the hotkey
                    self.type_text()
            except AttributeError:
                if str(key) == self.hotkey:
                    self.type_text()

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def type_text(self):
        text = self.text_to_type.get()
        if text:
            sleep(1)  # Delay before typing
            for char in text:
                pynput_keyboard_controller.type(char)
                sleep(0.01)
        else:
            messagebox.showwarning("Empty Input", "The input text is empty!")

    def cleanup(self):
        # Stop the listener on exit
        if self.listener:
            self.listener.stop()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HotkeyApp(root)
    root.mainloop()
