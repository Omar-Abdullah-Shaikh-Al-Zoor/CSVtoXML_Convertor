import csv
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile


def csv_upload():
    f_types = [('CSV files', "*.csv")]
    file = filedialog.askopenfilename(
        filetypes=f_types)
    if (file):
        path = "CSV file path is: " + file
        # self.label_info_1.set_text(path)
        fob = open(file, 'r')
        global csv_path, paths
        paths = path + "\n"
        csv_path = file


def loc_xmlpath():
    tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    path = "Path of New XML File is: " + folder_path
    # self.label_info_1.set_text(path)
    global xml_path, paths
    paths = path + "\n"
    xml_path = folder_path


def Convertor( csv_path, xml_path):
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

