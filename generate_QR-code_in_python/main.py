import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Create and place widgets
        self.label = tk.Label(root, text="Enter text to generate QR code:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)

        self.paste_button = tk.Button(root, text="Paste from Clipboard",
                                      command=self.paste_from_clipboard)
        self.paste_button.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate QR Code",
                                         command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def paste_from_clipboard(self):
        try:
            clipboard_text = self.root.clipboard_get()
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, clipboard_text)
        except tk.TclError:
            messagebox.showerror("Error", "Failed to get text from clipboard.")

    def generate_qr_code(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        file_path = 'QR-code.png'
        img.save(file_path)

        # Notify user after saving the QR code
        self.display_image(file_path)
        messagebox.showinfo("Success", f"QR code saved as {file_path}")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((250, 250), Image.Resampling.LANCZOS)  # Updated line
        img_tk = ImageTk.PhotoImage(img)

        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
