import requests
import wget

url = "https://sistema.lksh.ru/static/upload/entrance-exam-pdfs/"
for i in range(1, 1000):
    url_pdf = url + str(i) + ".pdf"
    if requests.get(url_pdf).status_code == 200:
        res = wget.download(url_pdf)
        print(i, end=" ")
