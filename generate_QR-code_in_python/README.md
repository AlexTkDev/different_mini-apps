## Project: QR Code Generation

#### Project Description
This project is a simple application for generating QR codes using the `qrcode` and `Pillow (PIL)`
libraries. The application features a graphical user interface that allows users to enter or paste 
text to generate a QR code based on that text. The generated QR code is saved as an image and 
displayed within the application window.

#### Key Features
- **QR Code Generation:**
  - Users can input text or paste copied text from the clipboard to create a QR code through the graphical interface.
  - The size and parameters of the QR code can be adjusted using version, error_correction, box_size, and border settings.
  - The generated QR code image is saved in PNG format and displayed in the application window.
  
- **Clipboard Integration:**
  - Users can paste text directly from the clipboard into the text entry field using the "Paste from Clipboard" button.
  
- **Notification System:**
  - Users are notified with a success message once the QR code is successfully generated and saved.

#### Requirements
The project requires the following dependencies:
- `Python 3.x`
- `qrcode`
- `Pillow (PIL)`

You can install all dependencies by running:
```sh
  pip install -r requirements.txt
```

#### How to Use
1. **QR Code Generation:**
   - Run the application.
   - Enter the text you want to encode in the QR code into the text entry field, or click the "Paste from Clipboard" button to insert copied text.
   - Click the "Generate QR Code" button.
   - The QR code will be generated, saved as `QR-code.png`, and displayed in the application window.

2. **Clipboard Integration:**
   - Click the "Paste from Clipboard" button to paste any copied text into the text entry field from the system clipboard.

#### License
This project is licensed under the MIT License. You are free to use, copy, modify, and distribute 
the code under the terms of this license.
