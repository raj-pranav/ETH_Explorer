# import libraries
import tkinter
import customtkinter as CTK
from PIL import Image

## Parent app setting - global
app_version = '1.0'
CTK.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
CTK.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        ## Global options
        self.title(f"ETH Explorer  v{app_version}")
        self.geometry("720x480+400+200") # WxH: use x (and not *)  |  + (or -) is to display the window on the screen (+x+y)
        # self.resizable(False, False)     # Fix the window movement (width and height)


if __name__ == "__main__":
    app = App()
    app.mainloop() 


