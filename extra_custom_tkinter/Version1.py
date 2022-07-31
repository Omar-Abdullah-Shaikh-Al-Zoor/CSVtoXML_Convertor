import csv
import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

global paths,csv_path,xml_path
class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CSV to XML Convertor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ Appearance ============
        self.label_mode = customtkinter.CTkLabel(master=self.frame_right,
                                                 width=300,
                                                 height=30, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_right,
                                                        values=["Light", "Dark", "System"],
                                                        width=320,
                                                        height=40,
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, columnspan=1, rowspan=1, pady=5, padx=20, sticky="w")

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
                                                   text="CSV to XML Convertor",
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", pady=20, padx=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                width=300,
                                                height=70,
                                                text="Choose a csv File",
                                                command=self.csv_upload)
        self.button_1.grid(row=5, column=0, columnspan=1, rowspan=1, pady=10)

        self.button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Choose the path of the new XML file",
                                                width=300,
                                                height=70,
                                                command=self.loc_xmlpath)

        self.button_2.grid(row=6, column=0, columnspan=1, rowspan=1, pady=0, padx=50)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        width=300,
                                                        height=50,
                                                        text="Choose CSV to XML Converter mode",
                                                        text_font=("Arial", 14))
        self.label_radio_group.grid(row=5, column=1, columnspan=1, rowspan=1, pady=5, padx=0, sticky="")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    width=100,
                                                    height=50,

                                                    values=["XML Mode 1", "XML Mode 2"])

        self.combobox_1.grid(row=6, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Convert to XML",
                                                width=300,
                                                height=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.loc_xmlpath)
        self.button_3.grid(row=9, column=1, columnspan=2, rowspan=2, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        self.combobox_1.set("XML Modes")

    def csv_upload(self):
        f_types = [('CSV files', "*.csv")]
        file = filedialog.askopenfilename(
            filetypes=f_types)
        if (file):
            path = "CSV file path is: " + file
            self.label_info_1.set_text(path)
            fob = open(file, 'r')
            paths = path + "\n"
            csv_path = file

    def loc_xmlpath(self):
        tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
        folder_path = filedialog.askdirectory()
        path = "Path of New XML File is: " + folder_path
        self.label_info_1.set_text(path)

        paths = path + "\n"
        xml_path = folder_path

    def Convertor(self,csv_path, xml_path):
        csvfile = csv_path

        def convert_row(headers, row):
            s = f'<Contact">\n'
            for header, item in zip(headers, row):
                s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
            return s + '</Contact>'

        with open(csvfile, 'r') as f:
            r = csv.reader(f)
            headers = next(r)
            xml = '<PhoneBook>\n'
            for row in r:
                xml += convert_row(headers, row) + '\n'
            xml += '</PhoneBook>'
        xml_file = str(xml_path) + "\\file.xml"
        with open(xml_file, "w") as f:
            f.write(xml)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
