import csv

with open('persons.csv', 'w', newline='') as csvfile:  
    #寫入新檔 
    #記得要有newline=''否則不能正確解讀換行 'w'是開新檔 'a'則是開舊檔append
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession']) #記得要在open指令下執行寫入，否則I/O會不允許
    filewriter.writerow(['Derek', 'Software Developer'])    #open指令下，csvfile才為開啟狀態
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])

with open('persons.csv', 'a', newline='') as csvfile:   
    #寫入舊檔
    #記得要有newline=''否則不能正確解讀換行 'w'是開新檔 'a'則是開舊檔append
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #記得要在open指令下執行寫入，否則I/O會不允許
    filewriter.writerow(['Mary', 'Project manager'])
    filewriter.writerow(['George', 'Software Developer'])
    filewriter.writerow(['Danny', 'Manager'])

with open('persons.csv', 'r', newline='') as csvfile2:
     #讀取
    filereader=csv.reader(csvfile2)
    for row in filereader:
        print(row)

with open('persons.csv', 'r', newline='') as csvfile3:
    #讀取
    filereader=csv.reader(csvfile3)
    for row in filereader:
        print(row[0])
