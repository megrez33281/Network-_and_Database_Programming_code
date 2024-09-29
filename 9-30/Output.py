import csv

csvIntialRow = [['學號', '姓名', '總成績']]
def createCSV(name, datarow):
    # 在創建指定名稱CSV檔案
    with open(name.replace('.csv', '') + '.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(datarow) #記得要在open指令下執行寫入，否則I/O會不允許

def appendCSV(name, datarow):
    # 在創建指定名稱CSV檔案
    with open(name.replace('.csv', '') + '.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(datarow) #記得要在open指令下執行寫入，否則I/O會不允許

def MakeCSV(name, datas):
    createCSV(name, csvIntialRow[0])
    for datarow in datas:
        appendCSV(name, datarow)

    

if __name__ == '__main__':
    
    csvFiles = []


        