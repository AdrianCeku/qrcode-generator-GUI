# qrcode-generator-GUI
Lightweight application with a user friendly GUI to quickly export QR-Codes as png, jpg, webp or svg files. 

![Screenshot](https://user-images.githubusercontent.com/95617181/233199277-afeafbd2-3843-42be-9ac9-bc3fab1cdb59.png)

## How to use:

0. Install Python.
1. Clone or download the repository.
2. Open the repository folder, click inside of the "path bar" right next to the search bar, type "cmd" and press enter to open the terminal in your current directory.
3. Enter "pip install -r requirements.txt" to install the needed libraries (qrcode and customtkinter) or use "pip install qrcode" and "pip install customtkinter" to install them manually. 
4. Enter "python main.py" for the GUI or "python terminal_version.py" for the terminal version.
5. Enter Filename, Content and choose your settings. Then click on "Generate".
6. The file should be saved to ".../qrcode-generator/QR-Codes/name.extension".

## Advanced Options

**File Extension**: Choose between .png, .jpg, .svg and .webp file extensions for your QR-Code.

**Error Correction**: Changes Error Correction Level. M allows up to 15% of the QR-Code to be unreadable but still work. Q allows for 25% and so on.

**Color**: Changes the Color of the Code itself.

**Background Color**: Changes the Background Color.

**Version**: Determines the version of the QR-Code. Higher versions increase the complexity of the QR-Code and allow for more Data to be stored in it.

**Size**: Changes the "line thickness" of the QR-Code.

**Border Size**: Changes distance from the edge of the code to the border of the image. The lowest recommended value is 4.

## Terminal Version
The Terminal version doesnt offer any advanced options and saves files as png. Default settings in the terminal version are the same as the default settings in the GUI Version. 

When asked to generate another one, enter "n" to quit or anything else to keep going.

