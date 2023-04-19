# qrcode-generator
Lightweight application with a GUI to quickly export qr codes as png, jpg, webp or svg files. 

![Screenshot](https://user-images.githubusercontent.com/95617181/233199277-afeafbd2-3843-42be-9ac9-bc3fab1cdb59.png)

## How to use:

0. Install Python.
1. Clone or download the repository.
2. Use "pip install -r requirements.txt" to install the needed libraries (qrcode and customtkinter)
3. Use "python main.py" for the GUI or "python terminal_version.py" for the terminal version.
4. Enter Filename, Content and choose your settings. Then click on "Generate".
5. The file should be saved to ".../qrcode-generator/QR-Codes".

## Advanced Options

**File Extension**: Choose between .png, .jpg, .svg and .webp file extensions for your QR-Code.

**Error Correction**: Changes Error Correction Level. M allows 15% of the code to be unreadable, Q 25% and so on.

**Color**: Changes the Color of the Code itself.

**Background Color**: Changes the Background Color.

**Version**: Determines the version of the QR-Code. Higher versions inceare the complexity of the qrcode allow for more Data to be stored in it.

**Size**: Changes the "line thickness" of the QR-Code.

**Border Size**: Changes distance to the border of the image. The lowest recommended value is 4.

## Terminal Version
The Terminal version doesnt offer any advanced options and saves files as png. When asked to generate another one, enter "n" to quit or anything else to keep going.

