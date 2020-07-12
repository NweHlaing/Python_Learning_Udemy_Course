import csv
#Reading CSV File
data = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\PropertyReport.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
print("Data lines...",data_lines)
print("Liens 3::::",data_lines[:3])
for line in data_lines[:5]:
    print(line)

print("Length....",len(data_lines))
print("index 2....",data_lines[2][2])

#Writing CSV Files
file_to_output = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6'],['7','8','9']])
file_to_output.close()

#Existing File
f = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()

