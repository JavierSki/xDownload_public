try:
    # for Python2
    from Tkinter import *   # notice capitalized T in Tkinter
    from Tkinter.filedialog import askdirectory
except ImportError:
    # for Python3
    from tkinter import *   # notice lowercase 't' in tkinter here
    from tkinter.filedialog import askdirectory
try:
  # for Python2
  import ttk
except ImportError:
  # for Python3 
  from tkinter import ttk


import os
import subprocess
import platform
from CJsonFile import JsonFile
from PIL import Image, ImageTk

flag_downloading = False

def btnSearchAndDownload_Click():
    search = str(txtSearch.get()).replace(" ", "+") # replace spaces by +
    first_page = str(txtFirstPage.get())
    last_page = str(txtLastPage.get())
    server = str(cbserver.get())
    output_dir = str(txtOutput.get())
    # ordem: server, search, firt page, last page, output dir
    if plataforma == 'Linux':
        command = 'sudo python main.py ' + server + ' ' + search + ' ' + first_page + ' ' + last_page + ' ' + output_dir
    else:
        command = 'start pythonw main.py ' + server + ' ' + search + ' ' + first_page + ' ' + last_page + ' ' + output_dir
    global flag_downloading
    flag_downloading = True
    #os.system(command)
    subprocess.call(command, shell=True)


def get_output_dir():
    folder = askdirectory()
    dirStr = folder
    txtOutput.delete(0, END)
    txtOutput.insert(0, dirStr)


jsonfile = JsonFile("data")


def timer():
    if True:
        mainGUI.after(1000, timer) # call this function again in 1,000 milliseconds
        data = jsonfile.json_details_read()
        if flag_downloading:
            lblInfo1['text'] = str(data["link"])
            lblInfo2['text'] = "Downloading: " + str(int(data["current"])+1) + " from " + str(int(data["range"])+1)
            progress["value"] = int(data["%"])
        else:
            lblInfo1['text'] = "Link: -"
            lblInfo2['text'] = "Waiting"
            progress["value"] = 0



def btnExit_Click():
    mainGUI.destroy()


line1 = 10
line2 = 35
line3 = 60
line4 = 85
line5 = 110
line6 = 135
line7 = 181
line8 = 206
line9 = 225



plataforma = platform.system()

mainGUI = Tk()
mainGUI.title("xDownload V 1.0")


if plataforma == 'Linux':
  mainGUI.geometry("350x280+300+300")
else:
  mainGUI.geometry("270x280+300+300")



mainGUI.resizable(1, 1)

lblSubject = Label(mainGUI, text="Search:")
lblSubject.place(x=10, y=line1)

txtSearch = ttk.Entry(mainGUI, width=30)
txtSearch.place(x=70, y=line1)

lblInterval = Label(mainGUI, text="Range:")
lblInterval.place(x=10, y=line2)

txtFirstPage = ttk.Entry(mainGUI, width=5)
txtFirstPage.place(x=70, y=line2)

lblTo = Label(mainGUI, text="to")
lblTo.place(x=112, y=line2)

txtLastPage = ttk.Entry(mainGUI, width=5)
txtLastPage.place(x=140, y=line2)

lblPages = Label(mainGUI, text="<- (Pages)")
lblPages.place(x=180, y=line2)

lblserver = Label(mainGUI, text="Server:")
lblserver.place(x=10, y=line3)

box_value = StringVar()
cbserver = ttk.Combobox(mainGUI, textvariable=box_value, width=27)
cbserver.place(x=70, y=line3)
cbserver['values'] = ('Beeg',
                      'EPorner',
                      'GotPorn',
                      'Porn',
                      'PornHD',
                      'PornHub',
                      'RedTube',
                      'SpankBang',
                      'XHamster',
                      'XNXX',
                      'XVideos',
                      'YouPorn',)

lblOutPut = Label(mainGUI, text="Out dir:")
lblOutPut.place(x=10, y=line4)

dirStr = StringVar()
txtOutput = ttk.Entry(mainGUI, width=23, textvariable=dirStr)
txtOutput.place(x=70, y=line4)

buttonImage = Image.open('folder.png')
buttonPhoto = ImageTk.PhotoImage(buttonImage)

btnSelectDir = ttk.Button(mainGUI, image=buttonPhoto, command=get_output_dir, width=5)
btnSelectDir.place(x=225, y=line4)

btnSearchAndDownload = ttk.Button(mainGUI, text="Search and Download All", command=btnSearchAndDownload_Click, width=39)
btnSearchAndDownload.place(x=12, y=120)

btnExit = ttk.Button(mainGUI, text="Exit", command=btnExit_Click, width=39)
btnExit.place(x=12, y=150)

progress = ttk.Progressbar(mainGUI, orient="horizontal", length=244, mode="determinate")
progress["value"] = 2
progress["maximum"] = 100
progress.place(x=12, y=line7)

lblInfo2 = Label(mainGUI, text="0")
lblInfo2.place(x=10, y=line8)

lblInfo1 = Label(mainGUI, text="0", wraplength=250)
lblInfo1.place(x=10, y=line9)

timer()

mainGUI.mainloop()
