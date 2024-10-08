import win32com.client as win32


def sendMail(subject, body, Receiver):
    # 設置郵件主題、正文和收件人
    #print(subject)
    #print(body)
    #print(Receiver)
    recipients = Receiver
    try:
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.Subject = subject
        mail.Body = body
        mail.To = recipients
        mail.Send()
        print("郵件寄出成功！")
    except Exception as e:
        print("郵件寄出失敗:", str(e))
        return 
        


if __name__ == '__main__': 
    sendMail([])