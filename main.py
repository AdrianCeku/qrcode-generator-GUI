import qrcode
import tkinter
import customtkinter 


def create_qr():
    img = qrcode.make(content_box.get("1.0","" ))
    img.save(f"Codes/{filename_box.get()}{filetype_box.get()}")

#customtkinter setup
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")

#Generate Button
generate_button = customtkinter.CTkButton(master=root,
                                width=120,
                                height=32,
                                corner_radius=8,
                                text="Generate",
                                command=create_qr,)
generate_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

#Filename Entrybox
filename_box =customtkinter.CTkEntry(master=root,
                            placeholder_text="Filename",
                            width=350,
                            height=20,
                            border_width=2,
                            corner_radius=10)
filename_box.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

#Content Textbox
"""
content_box =customtkinter.CTkEntry(master=root,
                            placeholder_text="Content",
                            width=350,
                            height=200,
                            border_width=2,
                            corner_radius=10)
content_box.place(relx=0.5, rely=0.335, anchor=tkinter.CENTER)
"""
content_box = customtkinter.CTkTextbox(master=root,
                            width=350,
                            height=200,
                            border_width=2,
                            corner_radius=10)
content_box.place(relx=0.5, rely=0.335, anchor=tkinter.CENTER)

#Advanced Options FRame
advanced_options = customtkinter.CTkFrame(master=root,
                            width=350,
                            height=100,
                            border_width=2,
                            corner_radius=10)
advanced_options.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
#Filetype Combobox
filetype_box = customtkinter.CTkComboBox(master=advanced_options,
                                    width=70,
                                    height=20,
                                    values=[".jpg",".png",".svg",".webp"],
                                    )
filetype_box.place(relx=0.123, rely=0.2, anchor=tkinter.CENTER)
filetype_box.set(".jpg")  # set initial value



root.mainloop()

