from tkinter import *
from tkinter import messagebox
import difflib

data = {}
with open('DictData.txt', 'r', encoding="utf-16", buffering=1) as file:
    for line in file:
        line = line.strip()
        if line.startswith('@'):
            key = line[1:].strip()
            data[key] = []
        elif line.startswith('*'):
            data[key].append({'type': line[1:].strip(), 'meanings': []})
        elif line.startswith('-'):
            if len(data[key]) > 0:
                data[key][-1]['meanings'].append(line[1:].strip())
            else:
                # Nếu danh sách rỗng, tạo một từ mới
                data[key].append({'type': '', 'meanings': [line[1:].strip()]})
        elif line.startswith('='):
            data[key][-1]['example'] = line[1:].strip()
        elif line.startswith('!'):
            data[key][-1]['idioms'] = line[1:].strip()


def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass

def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)


def search():
    keyword = enterwordentry.get()
    keyword = keyword.lower()
    if keyword in list(data.keys()):
        meanings = data[keyword]
        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)
        for meaning in meanings:
            textarea.insert(END, meaning['type'] + '\n\n')
            for item in meaning['meanings']:
                textarea.insert(END, u'\u2022' + item + '\n\n')
            if 'example' in meaning:
                textarea.insert(END, 'Example: ' + meaning['example'] + '\n\n')
            if 'idioms' in meaning:
                textarea.insert(END, 'Idioms: ' + meaning['idioms'] + '\n\n')
        textarea.config(state=DISABLED)
    else:
        textarea.delete(1.0, END)
        messagebox.showinfo('Information', 'Please type a correct word')


root = Tk()
root.geometry('1000x626+100+50')
root.title(' Dictionary ')


bgimage = PhotoImage(file='bg.png')

bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

enterwordLabel = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=530, y=20)

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=510, y=80)

enterwordentry.focus_set()

searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
searchButton.place(x=660, y=150)

meaninglabel = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
meaninglabel.place(x=580, y=240)

textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=460, y=300)


clearimage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2'
                     , command=clear)
clearButton.place(x=600, y=555)

exitimage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)
exitButton.place(x=750, y=555)


root.mainloop()
