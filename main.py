import pyttsx3
import PyPDF2
import mysql.connector as my
conn=my.connect(host="localhost",
                user="root",
                password="",
                database="loginapp")
s="select files from p where name='paper'"
cur=conn.cursor()
cur.execute(s)
data=cur.fetchall()
for i in data:
    a=i[0]
book = open(a,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
num =int(input("enter page number: "))
if num>pages:
    print("Invalid page number, please enter valid page number")

for i in range(num-1,pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
