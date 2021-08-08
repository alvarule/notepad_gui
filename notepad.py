# Creating a GUI Notepad In Tkinter

from tkinter import *
import tkinter.font as font
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                      ("Python Files", ".py")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(f"{os.path.basename(file)} - Notepad")


def saveasfile():
    global file
    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", title="Save As",
                             filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])
    f = open(file, "w")
    f.write(textarea.get(1.0, END))
    f.close()

    root.title(f"{os.path.basename(file)} - Notepad")


def _print():
    showinfo("Note", "This function is currently under development")


def undo():
    textarea.event_generate(("<<Undo>>"))


def redo():
    textarea.event_generate(("<<Redo>>"))


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def delete():
    textarea.event_generate(("<<Clear>>"))


def wordwrapon():
    textarea.config(wrap="word")


def wordwrapoff():
    textarea.config(wrap="none")


def _font():
    showinfo("Info", "This functionality is under development")
    '''
    f = Tk()
    # Basic Settings
    f.geometry("420x445")
    f.minsize(420, 445)
    f.maxsize(420, 445)
    f.title("Font")
    try:
        f.wm_iconbitmap("notepad.ico")
    except:
        pass

    # Tuples for storing listbox items
    fontfamilies = font.families()
    fontstyles = ("normal", "bold", "italic", "underline", "overstrike")
    fontsizes = (8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72)


    # Frames
    f1 = Frame(f, width=28, height=10)
    f1.pack(side=LEFT, anchor="n", padx=10, pady=10)
    f2 = Frame(f, width=18, height=10)
    f2.pack(side=LEFT, anchor="n", padx=10, pady=10)
    f3 = Frame(f, width=19, height=10)
    f3.pack(side=LEFT, anchor="n", padx=10, pady=10)

    # Variables for holding current selection of fontfamily, fontstyle, fontsize
    fontfamily = StringVar(value=textarea.cget("font"))
    # fontfamily.set(textarea.cget("font"))
    print(fontfamily.get())
    fontstyle = StringVar()
    fontsize = IntVar(value="12")

    # Labels
    Label(f1, text="Font:").pack(side=TOP, anchor="w")
    Label(f2, text="Font Style:").pack(side=TOP, anchor="w")
    Label(f3, text="Size:").pack(side=TOP, anchor="w")

    # Entry widgets for fontfamily, fontstyle, fontsize
    fontfamilyEntry = Entry(f1, textvariable=fontfamily, borderwidth=2, relief=GROOVE, width=28)
    fontfamilyEntry.pack(side=TOP, pady=0)
    fontstyleEntry = Entry(f2, textvariable=fontstyle, borderwidth=2, relief=GROOVE, width=18)
    fontstyleEntry.pack(side=TOP, pady=0)
    fontsizeEntry = Entry(f3, textvariable=fontsize, borderwidth=2, relief=GROOVE, width=9)
    fontsizeEntry.pack(side=TOP, pady=0)

    # Creating Listboxes

    fontfamilyls = Listbox(f1, width=26, borderwidth=2, relief=GROOVE)
    fontfamilyls.pack(side=LEFT, fill=BOTH, expand=True)
    ffs = Scrollbar(f1, command=fontfamilyls.yview)
    ffs.pack(side=LEFT, fill=Y)
    fontfamilyls.config(yscrollcommand=ffs.set)

    fontstylels = Listbox(f2, width=16, borderwidth=2, relief=GROOVE)
    fontstylels.pack(side=LEFT, fill=BOTH, expand=True)
    # fss = Scrollbar(f2, command=fontstylels.yview)
    # fss.pack(side=LEFT, fill=Y)
    # fontstylels.config(yscrollcommand=fss.set)

    fontsizels = Listbox(f3, width=7, borderwidth=2, relief=GROOVE)
    fontsizels.pack(side=LEFT, fill=BOTH, expand=True)
    fss = Scrollbar(f3, command=fontsizels.yview)
    fss.pack(side=LEFT, fill=Y)
    fontsizels.config(yscrollcommand=fss.set)

    # Inserting items in listboxes
    for item in fontfamilies:
        fontfamilyls.insert(END, item)
    for item in fontstyles:
        fontstylels.insert(END, item)
    for item in fontsizes:
        fontsizels.insert(END, item)

    # fontfamily.set(fontfamilyls.get(ACTIVE))
    # fontstyle.set(fontstylels.get(ACTIVE))
    print(fontfamily.get())
    # fontsize.set(fontsizels.get(ACTIVE))

    f.mainloop()
    '''


def find():
    showinfo("Info", "This functionality is under development")


def replace():
    showinfo("Info", "This functionality is under development")


def goto():
    showinfo("Info", "This functionality is under development")


def _help():
    showinfo("Note", "This software is developed by Atharva Varule"
                     "\nYou can ask him at varule.atharva@gmail.com"
                     "\nThank you for using our software!")


def feedback():
    showinfo("Note", "This software is developed by Atharva Varule"
                     "\nYou can send your feedback at varule.atharva@gmail.com"
                     "\nThank you for using our software!")


def about():
    showinfo("About", "This Notepad is developed by Atharva Varule")


if __name__ == '__main__':
    # Basic settings
    root = Tk()
    root.geometry("900x640")
    root.title("Untitled - Notepad")
    try:
        root.wm_iconbitmap("notepad.ico")
    except:
        pass

    # Creating textarea for the text to be displayed, edited, etc
    textarea = Text(root, wrap="none", undo=True)
    textarea.pack(fill=BOTH, expand=True)

    # Creating Scrollbars
    xscroll = Scrollbar(textarea, orient=HORIZONTAL, cursor="arrow")
    xscroll.pack(side=BOTTOM, fill=X)
    xscroll.config(command=textarea.xview)
    yscroll = Scrollbar(textarea, cursor="arrow")
    yscroll.pack(side=RIGHT, fill=Y)
    yscroll.config(command=textarea.yview)
    textarea.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

    file = None

    # Creating Menubar
    mainmenu = Menu(root)

    # File Menu
    filemenu = Menu(mainmenu, tearoff=0, background="black", fg="white")
    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open...", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_command(label="Save As...", command=saveasfile)
    filemenu.add_separator()
    filemenu.add_command(label="Print...              ", command=_print)
    filemenu.add_command(label="Exit", command=exit)
    mainmenu.add_cascade(label="File", menu=filemenu)

    # Edit Menu
    editmenu = Menu(mainmenu, tearoff=0, background="black", fg="white")
    editmenu.add_command(label="Undo", command=undo)
    editmenu.add_command(label="Redo", command=redo)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    editmenu.add_command(label="Delete", command=delete)
    editmenu.add_separator()
    editmenu.add_command(label="Find...", command=find)
    editmenu.add_command(label="Replace...", command=replace)
    editmenu.add_command(label="Go To...                              ", command=goto)
    mainmenu.add_cascade(label="Edit", menu=editmenu)

    # Format Menu
    formatmenu = Menu(mainmenu, tearoff=0, background="black", fg="white")
    wordwrapmenu = Menu(formatmenu, tearoff=0, background="black", fg="white")
    formatmenu.add_command(label="Font...", command=_font)
    wordwrapmenu.add_command(label="Word Wrap On", command=wordwrapon)
    wordwrapmenu.add_command(label="Word Wrap Off", command=wordwrapoff)
    formatmenu.add_cascade(label="Word Wrap", menu=wordwrapmenu)
    mainmenu.add_cascade(label="Format", menu=formatmenu)

    # Help Menu
    helpmenu = Menu(mainmenu, tearoff=0, background="black", fg="white")
    helpmenu.add_command(label="View Help", command=_help)
    helpmenu.add_command(label="Send Feedback", command=feedback)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=about)
    mainmenu.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=mainmenu)

    root.mainloop()

# exit()

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------Harry's Code---------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
'''
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Code With Harry")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()

'''
