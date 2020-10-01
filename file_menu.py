from tkinter import Tk,Menu,Label,Text,INSERT
import tkinter.filedialog as tkfile
import os
count = 0
class File:
    def __init__(self,root,textarea,p_menu):
        self.p_menu = p_menu
        self.root = root
        self.textarea = textarea
        self.filemenu()
        self.file ="new.txt"
        # self.root.bind_all(self.new)

    def filemenu(self):

        subfile = Menu(self.p_menu,tearoff=False)
        # file.add_cascade(label="File",menu = subfile)
        # file.add_cascade(label="name", menu=subfile)
        self.p_menu.add_cascade(label="File",menu=subfile)
        subfile.add_separator()
        subfile.add_command(label="New                      Ctrl+N",command=self.new)
        subfile.add_command(label="Open                     Ctrl+O",command=self.open_)
        subfile.add_separator()
        subfile.add_command(label="Save..                     Ctrl+S",command=self.save)
        subfile.add_command(label="Save as....",command=self.save_as)

    def new(self):
       self.root.title("New Diary")
       self.textarea.delete(1.0,"end")
       self.file = "New Diary1"



    def open_(self):
        self.textarea.delete(1.0,"end")
        self.file = tkfile.askopenfilename()
        self.root.title(os.path.basename(self.file))
        with open(self.file) as writing_file:
            txt = writing_file.read()
            # w_file = newfile.write()
            self.textarea.insert("insert",f"{txt}")


    def save(self):
        print(self.file)
        f0 = self.textarea.get(1.0,"end")

        with open(self.file,"w") as ff:
            f1 = ff.write(f0)
        with open(self.file) as fop:
            print(fop.read())



    def save_as(self):
        filename = tkfile.asksaveasfilename()
        print(filename)
        f0 = self.textarea.get(1.0, "end")

        with open(filename, "w") as ff:
            f1 = ff.write(f0)
        with open(filename) as fop:
            print(fop.read())

        self.root.title(os.path.basename(filename))




if __name__ == "__main__":
    print("run subfiles of file menu")
# root = Tk()
# textarea = Text(root)
# textarea.pack()
# a = File(root,textarea)
#
# root.mainloop()


