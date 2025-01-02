import tkinter as tk
from tkinter import messagebox
import keyboard
from time import sleep
from pynput.keyboard import Controller

pynput_keyboard_controller = Controller()


class HotkeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotkey Typing App")

        # Variables
        self.hotkey = None
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

    def set_hotkey(self):
        # Prompt user for hotkey
        def on_key(event):
            self.hotkey = event.name
            self.hotkey_label.config(text=f"Hotkey set: {self.hotkey}")
            keyboard.unhook_all()  # Stop listening after key is set
            messagebox.showinfo("Hotkey Set", f"Hotkey '{self.hotkey}' has been set!")
            self.bind_hotkey()

        messagebox.showinfo("Set Hotkey", "Press any key to set as hotkey.")
        keyboard.hook(on_key)  # Hook to capture key press

    def bind_hotkey(self):
        # Unbind previous hotkey if it exists
        keyboard.unhook_all_hotkeys()
        if self.hotkey:
            keyboard.add_hotkey(self.hotkey, self.type_text)

    def type_text(self):
        text = self.text_to_type.get()
        if text:
            sleep(1)
            for char in text:
                pynput_keyboard_controller.type(char)
                sleep(0.01)
        else:
            messagebox.showwarning("Empty Input", "The input text is empty!")

    def cleanup(self):
        # Unbind hotkeys on exit
        keyboard.unhook_all()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = HotkeyApp(root)
    root.mainloop()
