import csv


filename = 'my_file.csv'
def convert_row(headers, row):
    s = f'<Contact id="{row[0]}">\n'
    for header, item in zip(headers, row):
        s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
    return s + '</Contact>'
with open(filename, 'r') as f:
    r = csv.reader(f)
    headers = next(r)
    xml = '<PhoneBook>\n'
    for row in r:
        xml += convert_row(headers, row) + '\n'
    xml += '</PhoneBook>'
save_path_file = "Phonebook.xml"

with open(save_path_file, "w") as f:
    f.write(xml)




