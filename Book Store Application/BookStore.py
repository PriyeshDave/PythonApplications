import sqlite3
from tkinter import *

conn = sqlite3.connect('Book.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS "BookStore"("Id" INTEGER PRIMARY KEY,"Title" TEXT, "Author" TEXT, "Year" TEXT, "ISBN" INT)')

window = Tk()



def viewBooks():
  cur.execute('SELECT * FROM BookStore')
  books = cur.fetchall()
  textField.delete(0,END)
  for book in books:
    textField.insert(END,book)
 

def searchBook():
  author = bookAuthor.get()
  title = bookTitle.get()
  year = bookYear.get()
  isbn = int(isbnNum.get())
  cur.execute('SELECT * FROM BookStore WHERE Author=? OR Title=? OR Year=? OR ISBN=?',(author,title,year,isbn))
  books = cur.fetchall()
  textField.delete(0,END)
  for book in books:
    bookDetail = book[0]+ ", "+ book[1]+ ", "+book[2]+", "+book[3] + "\n"
    textField.insert(END,bookDetail)


def addBook():
  inputBookTitle  = bookTitle.get()
  author = bookAuthor.get()
  year = bookYear.get()
  isbn = int(isbnNum.get())
  cur.execute('INSERT INTO BookStore(Title,Author,Year,ISBN) VALUES (?,?,?,?)',(inputBookTitle,author,year,isbn))
  conn.commit()
  

def deleteBook():
  cur.execute('DELETE FROM BookStore WHERE Id=?',(selected_book[0],))
  conn.commit()

def updateBook():
  cur.execute('UPDATE BookStore SET Author= ? WHERE Id = ? AND Title = ? AND Author = ? AND Year= ? AND ISBN = ?',
  (authorText.get(),selected_book[0],selected_book[1],selected_book[2],selected_book[3],int(selected_book[4])))
  conn.commit()

def get_selected_row(event):
  global selected_book
  index = textField.curselection()[0]
  selected_book = textField.get(index)
  #Deleting the entry fields before displaying values.
  titleText.delete(0,END)
  authorText.delete(0,END)
  yearText.delete(0,END)
  isbnText.delete(0,END)
  #Showing the selected values in the entry fields.
  titleText.insert(END,selected_book[1])
  authorText.insert(END,selected_book[2])
  yearText.insert(END,selected_book[3])
  isbnText.insert(END,selected_book[4])
  print(selected_book)
  
  
title = Label(window, text = 'Title')
title.grid(row=0,column=0)

bookTitle = StringVar()
titleText = Entry(window,textvariable=bookTitle)
titleText.grid(row=0,column=1)

author = Label(window, text='Author')
author.grid(row=0,column=2)

bookAuthor = StringVar()
authorText = Entry(window,textvariable=bookAuthor)
authorText.grid(row=0,column=3)

year = Label(window, text='Year')
year.grid(row=1,column=0)

bookYear = StringVar()
yearText = Entry(window,textvariable=bookYear)
yearText.grid(row=1,column=1)

isbn = Label(window, text='ISBN')
isbn.grid(row=1,column=2)

isbnNum = StringVar()
isbnText = Entry(window,textvariable=isbnNum)
isbnText.grid(row=1,column=3)

viewAll = Button(window, text='View All',command=viewBooks)
viewAll.grid(row=2,column=3)

searchEntry = Button(window, text='Search Entry',command=searchBook)
searchEntry.grid(row=3,column=3)

addEntry = Button(window, text='Add Entry',command=addBook)
addEntry.grid(row=4,column=3)

updateSelected = Button(window, text='Update Selected',command=updateBook)
updateSelected.grid(row=5,column=3)

deleteSelected = Button(window, text='Delete Selected',command=deleteBook)
deleteSelected.grid(row=6,column=3)

close = Button(window, text='Close')
close.grid(row=7,column=3)

textField = Listbox(window,height=6,width=35)
textField.grid(row=2,column=0,columnspan=2)

textField.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2)

textField.configure(yscrollcommand=sb1.set)
sb1.configure(command=textField.yview)

window.mainloop()
cur.close()