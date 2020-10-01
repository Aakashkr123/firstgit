from tkinter import *
import tkinter.messagebox as tkmsg
class Helpmenu:
    def __init__(self,root,textarea,p_menu):
        self.root = root
        self.textarea = textarea
        self.p_menu = p_menu
        self.main()
    def main(self):
        help = Menu(self.p_menu,tearoff=0)
        self.p_menu.add_cascade(label="Help",menu=help)
        help.add_command(label="About",command=self.msg)
        help.add_command(label="Quit",command=quit)
    def msg(self):
        tkmsg.showinfo("My Diary -About","This is a text editing app like a notepad \n Designed by Akash kumar")
if __name__ == "__main__":
    print("nothing")