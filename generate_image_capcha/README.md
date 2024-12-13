### CAPTCHA Generation Script Documentation

#### Description
This script generates CAPTCHA images with random text. The CAPTCHA text consists of uppercase letters and digits. The generated image is saved to a specified file path.

#### Installation of Dependencies
The script requires the following packages:
- `captcha`: to generate CAPTCHA images
- `Pillow (PIL)`: to work with images

Create a `requirements.txt` file with the following dependencies:
```text
captcha==0.4
Pillow==9.2.0
```

##### Installing Dependencies:
1. Ensure you have Python 3.6 or higher installed.
2. Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

#### How to Use the Script
Once the dependencies are installed, you can run the script to generate a CAPTCHA image.

##### Example Usage:
1. **Default Usage**:
   Generate a CAPTCHA with a default length of 10 characters, image size 500x100 pixels, and save it to `CAPTCHA.png`:
   ```bash
   python captcha_generator.py
   ```

2. **Specify CAPTCHA Length**:
   Generate a CAPTCHA with a text length of 6 characters:
   ```bash
   python captcha_generator.py --length 6
   ```

3. **Change Image Size**:
   Generate a CAPTCHA with 8 characters, an image size of 400x120 pixels:
   ```bash
   python captcha_generator.py --length 8 --width 400 --height 120
   ```

4. **Save CAPTCHA to a Different Path**:
   Generate a CAPTCHA with 6 characters and save the file to a specific directory:

   ```bash
   python captcha_generator.py --length 6 --save_path ./output/captcha_image.png
   ```

   If the `output` directory does not exist, the script will create it automatically.

5. **Complex Example**:
   Generate a CAPTCHA with 8 characters, image size 600x150 pixels, and save the file to `./images/captcha.png`:
   ```bash
   python captcha_generator.py --length 8 --width 600 --height 150 --save_path ./images/captcha.png
   ```

#### Parameter Description
- `--length`: The length of the CAPTCHA text (default: 10 characters). You can specify any integer.
- `--width`: The width of the CAPTCHA image in pixels (default: 500).
- `--height`: The height of the CAPTCHA image in pixels (default: 100).
- `--save_path`: The file path to save the CAPTCHA image (default: `CAPTCHA.png`). If the directory does not exist, it will be created automatically.

#### Logging
The script uses standard logging to output information about the process:
- Successful CAPTCHA file creation.
- Errors during image generation or file saving.

#### Example Log Output:
```bash
INFO:root:Captcha successfully saved to ./output/captcha_image.png
INFO:root:Captcha text: X7C9D2
```
