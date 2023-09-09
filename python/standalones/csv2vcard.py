import csv
import datetime as dt

def convert_csv_to_vcard(csv_file, vcard_file):
  with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(next(reader))
    
    numberofphones = int(sum([1 for e in next(reader).keys() if e.startswith("Phone")])/2)
    numberofemails = int(sum([1 for e in next(reader).keys() if e.startswith("Email")])/2)


    with open(vcard_file, 'w') as vcardfile:
      for row in reader:
        vcard = f"BEGIN:VCARD\nVERSION:3.0\n"

        #get the basic info
        vcard += f"FN:{row['Name']};;;\n"
        vcard += f"N:{row['Family Name']};{row['Given Name']};{row['Additional Name']};;\n"

        if(row['Birthday'] != ""):
          vcard += f"BDAY:{row['Birthday']}\n"

        if(row['Notes'] != ""):
          vcard += f"NOTE:{row['Notes']}\n"

        #add address
        if(row["Address - Type"] != ""):
          vcard += f"ADR;TYPE={row['Address - Type']}:{row['Address - PO Box']};;{row['Address - Street']};{row['Address - City']};{row['Address - Region']}{row['Address - Postal Code']}{row['Address - Country']}"
          vcard += f"LABEL;TYPE={row['Address - Type']}:{row['Address - Formatted']}"

        #loop through all the phones (col's should be formatted as "Phone {#} - Type" and "Phone {#} - Value")
        for i in range(1,numberofphones+1):
          if(row[f'Phone {i} - Type'] != ""):
            vcard += f"TEL;TYPE={row[f'Phone {i} - Type']}:{row[f'Phone {i} - Value']}\n"

        #loop through all the emails
        for i in range(1,numberofemails+1):
          if(row[f'Email {i} - Type'] != ""):
            vcard += f"EMAIL;TYPE={row[f'Email {i} - Type']}:{row[f'Email {i} - Value']}\n"

        vcard += f"END:VCARD\n"

        print(vcard,"\n")
        vcardfile.write(vcard)


convert_csv_to_vcard('./my-contacts.csv', f'my-contacts--{dt.datetime.today()}.vcf')
print("done")