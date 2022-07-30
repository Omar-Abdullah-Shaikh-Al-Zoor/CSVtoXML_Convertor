import csv
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title('CSV to XML Convertor')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Upload a CSV File to Proceed', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)

b2 = tk.Button(my_w, text='Choose the path of the new XML file',
               width=40, command=lambda: xml_path())

b2.grid(row=5, column=1)

my_str = tk.StringVar()
l2 = tk.Label(my_w, textvariable=my_str, fg='red')
l2.grid(row=3, column=1)
my_str.set("")

def upload_file():
    f_types = [('CSV files', "*.csv")]
    file = filedialog.askopenfilename(
        filetypes=f_types)
    if (file):
        my_str.set("CSV file path is: " + file)
        fob = open(file, 'r')
        print(fob.read())
        global csv_path
        csv_path = file

my_str2 = tk.StringVar()
l3 = tk.Label(my_w, textvariable=my_str2, fg='red')
l3.grid(row=8, column=1)
my_str2.set("")


def xml_path():
    tk.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    my_str2.set("Path of New XML File is: " + folder_path)
    global xml_path
    xml_path = folder_path

b3 = tk.Button(my_w, text='Convert to XML',
               width=20, command=lambda: Convertor(csv_path,xml_path))
b3.grid(row=9, column=1)

def Convertor(csv_path,xml_path):
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
    xml_file=str(xml_path) +"\\file.xml"
    with open(xml_file, "w") as f:
        f.write(xml)
        l4 = tk.Label(my_w, text='File Converted Successfully', width=30, font=my_font1)
        l4.grid(row=10, column=1)
        open(xml_file)

my_w.mainloop()  # Keep the window open
