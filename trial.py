from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "rash.1234"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root", password=mypass,database=mydatabase)
cur = con.cursor()


# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"

allBid = []  #To store all the Book ID’s
global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
bid = "605"
issueto ="Nisar"
extractBid = "select bid from "+bookTable
cur.execute(extractBid)
con.commit()
for i in cur:
    print ("i is ", i)
    allBid.append(i[0])
print("allbid is",allBid)
if bid in allBid:
    checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
    result=cur.execute(checkAvail)
    con.commit()
    for i in cur:
        #print("i is ",i)
        check = i[0]
        print("Check is ",check)
        if check == 'avail':
            status = True
        else:
            status = False
    print(status)
