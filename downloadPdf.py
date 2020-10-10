import requests
import sys
import os


def downloadFile(url, fileName):
    try:
        response = requests.get(url)
    except:
        print("error happen")

    print(response.url)
    print(response)
    if response.url == url and response.status_code != 404:
        with open(fileName, "wb") as file:

            file.write(response.content)


scriptPath = sys.path[0]
downloadPath = os.path.join(scriptPath)
url = "https://alqabas.com/pdf/download/37934"
# url = "http://pdf2020.seyasi.com/pdf/2020/ln_20200901_1.pdf"
# url = "https://www.alwatan.com.sa/uploads/pdf/2020/09/01/watanksa-20200901.pdf"
day = url.split('/')
# print(day)
fileName = day[2].replace('.', '_', day[2].count('.')) + day[-1]
string = day[-1]
# print('str is ...', string)
if string.find(".pdf") == -1:
    print("NO")
    fileName = fileName + '.pdf'
print(fileName)
downloadPath = downloadPath + '/download/' + fileName
downloadFile(url, downloadPath)
