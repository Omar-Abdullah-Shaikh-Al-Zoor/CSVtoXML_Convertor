import tkinter
import tkinter.messagebox
import customtkinter
from tkinter.filedialog import askopenfile
import Conv_func as cf

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

global csv_path, xml_path, paths


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CSV to XML Convertor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create a frame ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="n", padx=20, pady=30)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=5, rowspan=5, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CSV to XML Convertor\n\n Credits: Omar Shaikh Abdullah Al Zoor",
                                                   text_color="turquoise",
                                                   text_font=("Arial", 15),
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.CENTER)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", pady=15, padx=20)

        # ============ Buttons ============

        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                width=370,
                                                height=65,
                                                text_color="turquoise",
                                                text_font=("Arial", 15),
                                                text="Choose a CSV File",
                                                command=self.csv_upload)
        self.button_1.grid(row=5, column=0, columnspan=1, rowspan=1, padx=30, pady=10)

        self.button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Choose the path of the new XML file",
                                                width=400,
                                                state=tkinter.DISABLED,
                                                text_color="turquoise",
                                                text_font=("Arial", 13),
                                                height=65,
                                                command=self.loc_xmlpath)

        self.button_2.grid(row=5, column=1, columnspan=1, rowspan=1, pady=10, padx=20)
        self.button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Convert to XML",
                                                width=300,
                                                height=50,
                                                background="red",
                                                border_color="red",
                                                border_width=3,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                hover_color="tomato",
                                                text_color="red",
                                                state=tkinter.DISABLED,
                                                text_font=("Arial", 20),
                                                command=self.convertor)
        self.button_3.grid(row=9, column=1, columnspan=2, rowspan=2, pady=20, padx=20, sticky="we")

        # ============ Radio Button and Combobox  ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        width=300,
                                                        height=60,
                                                        text_color="turquoise",
                                                        text="Choose XML Converter Mode",
                                                        fg_color=("white", "gray38"),  # <- custom tuple-color
                                                        corner_radius=7,
                                                        text_font=("Arial", 14),
                                                        )
        self.label_radio_group.grid(row=6, column=0, columnspan=1, rowspan=1, pady=5, padx=0, sticky="")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    width=100,
                                                    height=50,
                                                    dropdown_text_color="turquoise",
                                                    dropdown_text_font=("Arial", 12),
                                                    text_color="turquoise",
                                                    state=tkinter.DISABLED,
                                                    text_font=("Arial", 15),
                                                    command=self.xml_mode,
                                                    values=["PhoneDirectory", "XML Mode 2"])

        self.combobox_1.grid(row=6, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        # ============ Appearance ============
        self.label_mode = customtkinter.CTkLabel(master=self.frame_right,
                                                 width=300,
                                                 height=30, text_color="blue",
                                                 text_font=("Arial", 15),
                                                 text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=50, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_right,
                                                        text_color="turquoise",
                                                        text_font=("Arial", 15),
                                                        dropdown_text_font=("Arial", 12),
                                                        dropdown_text_color="turquoise",
                                                        values=["Light", "Dark"],
                                                        width=320,
                                                        height=40,
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, columnspan=1, rowspan=1, pady=20, padx=43, sticky="w")

        # ============ Functions ============

        # set default values
        self.optionmenu_1.set("Dark")

    def csv_upload(self):
        global csv_path, paths, filename
        csv_path, paths, filename = cf.csv_upload()
        self.label_info_1.set_text(paths)
        if paths != "none":
            self.button_2.configure(state=tkinter.NORMAL)

    def loc_xmlpath(self):
        global xml_path
        xml_path, path = cf.loc_xmlpath(paths)
        self.label_info_1.set_text(path)
        if path != "none":
            self.combobox_1.configure(state=tkinter.NORMAL)
            self.combobox_1.set("XML Modes")

    def xml_mode(self, xml_value):
        if self.combobox_1.current_value == "PhoneDirectory" or self.combobox_1.current_value == "XML Mode 2":
            self.button_3.configure(state=tkinter.NORMAL)

    def convertor(self):
        if self.combobox_1.current_value == "PhoneDirectory":
            value = cf.Convertor_m1(csv_path, xml_path, filename)
            if value == 1:
                self.label_info_1.set_text("Successfully Created XML File")
            else:
                self.label_info_1.set_text("Failed to Create XML File")
        elif self.combobox_1.current_value == "XML Mode 2":
            value = cf.Convertor_m2(csv_path, xml_path, filename)
            if value == 1:
                self.label_info_1.set_text("Successfully Created XML File")
            else:
                self.label_info_1.set_text("Failed to Create XML File")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        if self.optionmenu_1.current_value == "Dark":
                self.button_1.configure(text_color="turquoise")
                self.button_2.configure(text_color="turquoise")
                self.button_3.configure(text_color="red")
                self.button_3.configure(border_color="red")
                self.optionmenu_1.configure(text_color="turquoise")
                self.combobox_1.configure(text_color="turquoise")
                self.combobox_1.configure(dropdown_text_color="turquoise")
                self.optionmenu_1.configure(dropdown_text_color="turquoise")
                self.label_info_1.configure(text_color="aqua")
                self.label_radio_group.configure(text_color="turquoise")
        elif self.optionmenu_1.current_value == "Light":
                self.button_1.configure(text_color="navy")
                self.button_2.configure(text_color="navy")
                self.button_3.configure(text_color="red")
                self.button_3.configure(border_color="red")
                self.optionmenu_1.configure(text_color="navy")
                self.combobox_1.configure(text_color="navy")
                self.combobox_1.configure(dropdown_text_color="navy")
                self.optionmenu_1.configure(dropdown_text_color="navy")
                self.label_info_1.configure(text_color="red")
                self.label_radio_group.configure(text_color="navy")



    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
