import csv
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import customtkinter
import os

global csv_path,xml_path, paths
def csv_upload():
    f_types = [('CSV files', "*.csv")]
    file = filedialog.askopenfilename(
        filetypes=f_types)
    if (file):
        file_name = os.path.basename(file)
        filename = os.path.splitext(file_name)[0]
        path = "CSV file path is: " + file
        fob = open(file, 'r')
        paths = path
        csv_path = file

        return csv_path,path,filename


def loc_xmlpath(paths):
    tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    path = "Path of New XML File is: " + folder_path
    path1 = paths + "\n" + "\n" + path
    xml_path = folder_path
    return xml_path,path1


def Convertor_m1(csv_path, xml_path,filename):
    csvfile = csv_path
    def convert_row(headers, row):
        s = f'<Contact>\n'
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
    xml_file = str(xml_path) + "/"+filename+".xml"
    with open(xml_file, "w") as f:
        f.write(xml)
        return 1

def Convertor_m2(csv_path, xml_path, filename):
        csvfile = csv_path
        def convert_row(headers, row):
            s = f'<Contact>\n'
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
        xml_file = str(xml_path) + "/" + filename + ".xml"
        with open(xml_file, "w") as f:
            f.write(xml)
            return 1

