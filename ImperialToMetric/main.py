import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Unit Converter")

# UI Elements
title = customtkinter.CTkLabel(app, text="Input Imperial Unit")
title.pack(padx=20, pady=20)
dropdowntitle = customtkinter.CTkLabel(app, text="Select Measurement To Convert")
dropdowntitle.pack(padx=20, pady=20)

# Imperial Input
imperial_input = customtkinter.CTkEntry(app, width=400, height=60)
imperial_input.pack()

# Conversion Selector
dropdownmenu = customtkinter.CTkOptionMenu(app, width=140, height=28)
dropdownmenu.pack()

# Output
outputbox = customtkinter.CTkLabel(app, text=("Conversion:", "NULL","UNITS"))
outputbox.pack()

# Run app
app.mainloop()

