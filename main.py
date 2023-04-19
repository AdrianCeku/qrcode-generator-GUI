import qrcode
import qrcode.image.svg
import tkinter
import customtkinter 

# Generates the QR Code and saves it. Gets called when you press on "Generate" 
def create_qr():
    qr = qrcode.QRCode(
            version=round(version_slider.get()),
            box_size=round(boxsize_slider.get()),
            border=round(border_slider.get()),
            error_correction=get_error_correction()
    )
    qr.add_data(content_box.get("1.0","end-1c"))

    if filetype_box.get() == ".svg":
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
    else: img = qr.make_image(back_color=background_color_box.get(),fill_color=fill_color_box.get())

    img.save(f"QR-Codes/{filename_box.get()}{filetype_box.get()}")

# Returns selected Error Correction Level. Gets called when Generating a QR Code
def get_error_correction():
    if error_corection_box.get()=="L (7%)":
        return qrcode.constants.ERROR_CORRECT_L
    elif error_corection_box.get()=="M (15%)":
        return qrcode.constants.ERROR_CORRECT_M
    elif error_corection_box.get()=="Q (25%)":
        return qrcode.constants.ERROR_CORRECT_Q
    elif error_corection_box.get()=="H (30%)":
        return qrcode.constants.ERROR_CORRECT_H
    else: return qrcode.constants.ERROR_CORRECT_M

# Updates slider values to represent current value. Gets called whenever a slider is moved
def update_slider_labels(_):
    version_slider_label.configure(text=f"Version ({round(version_slider.get())})")
    boxsize_slider_label.configure(text=f"Size ({round(boxsize_slider.get())})")
    border_slider_label.configure(text=f"Bordersize ({round(border_slider.get())})")



# customtkinter setup
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("600x600")
root.title("QR Code Generator by Adrian Ceku")
root.resizable(False,False)
root.iconbitmap("icon.ico")

# Generate Button
generate_button = customtkinter.CTkButton(master=root,
                                width=120,
                                height=32,
                                corner_radius=8,
                                text="Generate",
                                command=create_qr,)
generate_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Filename Entrybox + Label
filename_box =customtkinter.CTkEntry(master=root,
                            #placeholder_text="Filename",
                            width=450,
                            height=20,
                            border_width=2,
                            corner_radius=10)
filename_box.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

filename_box_label = customtkinter.CTkLabel(master=root,
                                text="Filename",
                                width=100,
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
filename_box_label.place(relx=0.175, rely=0.060, anchor=tkinter.CENTER)

# Content Textbox + Label
content_box = customtkinter.CTkTextbox(master=root,
                            width=450,
                            height=200,
                            border_width=2,
                            corner_radius=10)
content_box.place(relx=0.5, rely=0.335, anchor=tkinter.CENTER)

content_box_label = customtkinter.CTkLabel(master=root,
                                text="Content",
                                width=100,
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
content_box_label.place(relx=0.170, rely=0.15, anchor=tkinter.CENTER)

# Advanced Options Frame + Label
advanced_options = customtkinter.CTkFrame(master=root,
                            width=450,
                            height=150,
                            border_width=2,
                            corner_radius=10)
advanced_options.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

advanced_options_label = customtkinter.CTkLabel(master=root,
                                text="Advanced Options",
                                width=100,
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
advanced_options_label.place(relx=0.22, rely=0.55, anchor=tkinter.CENTER)

# Filetype Combobox + Label
filetype_box = customtkinter.CTkComboBox(master=advanced_options,
                                    width=70,
                                    height=20,
                                    values=[".png",".jpg",".svg",".webp"],
                                    )
filetype_box.place(relx=0.2, rely=0.27, anchor=tkinter.CENTER)
filetype_box.set(".png")  # Sets initial value

filetype_box_label = customtkinter.CTkLabel(master=advanced_options,
                                text="File Extension",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
filetype_box_label.place(relx=0.2, rely=0.12, anchor=tkinter.CENTER)

# Errorcorrection Combobox + Label
error_corection_box = customtkinter.CTkComboBox(master=advanced_options,
                                    width=70,
                                    height=20,
                                    values=["L (7%)","M (15%)","Q (25%)","H (30%)"],
                                    )
error_corection_box.place(relx=0.4, rely=0.27, anchor=tkinter.CENTER)
error_corection_box.set("M (15%)")  # Sets initial value

filetype_box_label = customtkinter.CTkLabel(master=advanced_options,
                                text="Error Correction",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
filetype_box_label.place(relx=0.4, rely=0.12, anchor=tkinter.CENTER)

# Color Combobox # Label
fill_color_box = customtkinter.CTkComboBox(master=advanced_options,
                                    width=70,
                                    height=20,
                                    values=["black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                    )
fill_color_box.place(relx=0.6, rely=0.27, anchor=tkinter.CENTER)
fill_color_box.set("black")  # Sets initial value

filetype_box_label = customtkinter.CTkLabel(master=advanced_options,
                                text="Color",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
filetype_box_label.place(relx=0.6, rely=0.12, anchor=tkinter.CENTER)

# Backgroundcolor Combobox + Slider
background_color_box = customtkinter.CTkComboBox(master=advanced_options,
                                    width=70,
                                    height=20,
                                    values=["black","white","red","green", "blue", "yellow", "orange", "pink", "purple"],
                                    )
background_color_box.place(relx=0.8, rely=0.27, anchor=tkinter.CENTER)
background_color_box.set("white")  # Sets initial value

filetype_box_label = customtkinter.CTkLabel(master=advanced_options,
                                text="Background Color",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
filetype_box_label.place(relx=0.8, rely=0.12, anchor=tkinter.CENTER)

# Version Slider + Label
version_slider = customtkinter.CTkSlider(master=advanced_options,
                                        width=320,
                                        height=20,
                                        from_=1,
                                        to=40,
                                        number_of_steps=40,
                                        command=update_slider_labels)
version_slider.place(relx=0.6, rely=0.47, anchor=tkinter.CENTER)
version_slider.set(1) # Sets initial value

version_slider_label = customtkinter.CTkLabel(master=advanced_options,
                                text=f"Version ({round(version_slider.get())})",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
version_slider_label.place(relx=0.125, rely=0.47, anchor=tkinter.CENTER)

# Boxsize Slider + Label
boxsize_slider = customtkinter.CTkSlider(master=advanced_options,
                                        width=320,
                                        height=20,
                                        from_=1,
                                        to=100,
                                        number_of_steps=100,
                                        command=update_slider_labels)
boxsize_slider.place(relx=0.6, rely=0.67, anchor=tkinter.CENTER)
boxsize_slider.set(10) # Sets initial value

boxsize_slider_label = customtkinter.CTkLabel(master=advanced_options,
                                text=f"Size ({round(boxsize_slider.get())})",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent",
                                )
boxsize_slider_label.place(relx=0.125, rely=0.67, anchor=tkinter.CENTER)

# Border Slider + Label
border_slider = customtkinter.CTkSlider(master=advanced_options,
                                        width=320,
                                        height=20,
                                        from_=0,
                                        to=100,
                                        number_of_steps=101,
                                        command=update_slider_labels)
border_slider.place(relx=0.6, rely=0.87, anchor=tkinter.CENTER)
border_slider.set(4) # Sets initial value

border_slider_label = customtkinter.CTkLabel(master=advanced_options,
                                text=f"Border Size ({round(border_slider.get())})",
                                height=20,
                                corner_radius=8,
                                fg_color="transparent")
border_slider_label.place(relx=0.125, rely=0.87, anchor=tkinter.CENTER)


# Starts the program
root.mainloop()

