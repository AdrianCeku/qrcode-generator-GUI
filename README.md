# qrcode-generator-GUI
Lightweight application with a user friendly GUI to quickly export QR-Codes as png, jpg, webp or svg files. 

![Screenshot](https://github.com/AdrianCeku/qrcode-generator-GUI/assets/95617181/87bb06c6-ebc9-4baf-867c-8b98c2e1a28d)

## How to use:


0. Install Python.
1. Clone or download the repository.
2. Open the repository folder, click inside of the "path bar" right next to the search bar, type "cmd" and press enter to open the terminal in your current directory.
3. Enter "pip install -r requirements.txt" to install the needed libraries (qrcode, customtkinter and pillow) or install them manually. 
4. Enter "python main.py" for the GUI or "python terminal_version.py" for the terminal version.
5. Enter Filename, Content and choose your settings. Then click on "Save".
6. The file should be saved to ".../qrcode-generator/QR-Codes/name.extension".

## Advanced Options

**File Extension**: Choose between .png, .jpg, .svg and .webp file extensions for your QR-Code.

**Error Correction**: Changes Error Correction Level. M allows up to 15% of the QR-Code to be unreadable but still work. Q allows for 25% and so on. If you enable the logo, you will be locked to using Q (25%) or H (30%). 

**Color**: Changes the color of the QR-Code itself.

**Background Color**: Changes the background color. Choosing transparent removes the option to export as .jpg since it doesnt support transparency.

**Version**: Determines the version of the QR-Code. Higher versions increase the complexity of the QR-Code and allow for more data to be stored in it.

**Border Size**: Changes distance from the edge of the code to the border of the image. The lowest recommended value is 4.

**Size**: Changes the "line/block thickness" of the QR-Code. Your image resolution will be <number_of_blocks(determined by version and content) * size> pixels. 

**Enable Preview**: Extends the window to the right and shows a live preview of your QR-Code. Using high versions whith preview enabled may lead to lag.

**Enable Logo**: Adds a chosen logo to the center of the QR-Code. This option disables .svg export and some other sliders. Saving a QR-Code with a logo, will always be 2000x2000px image.

**Change Logo**: Opens up the file explorer to select a logo. Only supports .png, .jpg and .webp files.

## Terminal Version
The Terminal version doesnt offer any advanced options and saves files as png. Default settings in the terminal version are the same as the default settings in the GUI Version. 

When asked to generate another one, enter "n" to quit or anything else to keep going.
