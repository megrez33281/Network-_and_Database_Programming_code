import csv

csvFilesName = ['學生基本資料', '課程基本資料', '學生修課資料']
csvIntialRow = [
    ['姓名', '學號'],
    ['課名', '課號'],
    ['學號', '課號', '成績']
]

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

def readCSV(name):
    #讀取指定名稱CSV檔案
    row_data = []
    with open(name.replace('.csv', '') + '.csv', 'r', newline='') as csvfile:
        filereader=csv.reader(csvfile)
        for row in filereader:
            row_data.append(row)
    return row_data[1:]


def FindStudent(studentName):
    # 輸入學生姓名，列出所有修課的成績
    All_Data = []
    for name in csvFilesName:
        All_Data.append(readCSV(name))

    studentID = ''
    for row in All_Data[0]:
        if studentName == row[0]:
            #尋找學號
            studentID = row[1]
            break
    class_list = []
    for row in All_Data[2]:
        #搜尋學生修課課號、成績
        if row[0] == studentID:
            class_list.append(row[1:])

    for classInfo in class_list:
        #搜尋課號對應課名
        for row in All_Data[1]:
            if row[1] == classInfo[0]:
                classInfo.append(row[0])

    return class_list
        
    

if __name__ == '__main__':
    
    csvFiles = []
    for i in range(0, len(csvFilesName)):
        createCSV(csvFilesName[i], csvIntialRow[i])

    print("指令說明：")
    print("a. 新增學生基本資料（姓名、學號）：", "a 姓名 學號")
    print("b. 新增課程基本資料（課名、課號）：", "b 課名 課號")
    print("c. 新增學生修課資料（學號、課號、成績）：", "c 學號 課號 成績")
    print("d. 輸入學生姓名，列出所有修課的成績：", "d 姓名")
    print("輸入-1結束程式")
    command = input('請輸入指令：')
    while command != '-1':
        command_list = command.split(' ')
        if command_list[0] == 'a':
            data_row = command_list[1:]
            if len(data_row) != 2:
                print("資料格式錯誤")
                command = input('請輸入指令：')
                continue
            appendCSV(csvFilesName[0], data_row)

        elif command_list[0] == 'b':
            data_row = command_list[1:]
            if len(data_row) != 2:
                print("資料格式錯誤")
                command = input('請輸入指令：')
                continue
            appendCSV(csvFilesName[1], data_row)
        
        elif command_list[0] == 'c':
            data_row = command_list[1:]
            if len(data_row) != 3:
                print("資料格式錯誤")
                command = input('請輸入指令：')
                continue
            appendCSV(csvFilesName[2], data_row)

        elif command_list[0] == 'd':
            if len(command_list) != 2:
                print("資料格式錯誤")
                command = input('請輸入指令：')
                continue
            name = command_list[1]
            #排序為：課號、成績、課名
            class_info = FindStudent(name)
            print("課號", "課名", "成績")
            for info in class_info:
                print(info[0], info[2], info[1])
            print('\n')
        else:
            print("錯誤的指令")

        command = input('請輸入指令：')

        