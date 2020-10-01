from tkinter import *
class EditMenu:
    def __init__(self,root,textarea,p_menu):
        self.root = root
        self.textarea = textarea
        self.p_menu = p_menu
        self.main()

    def main(self):
        self.submenu = Menu(self.p_menu,tearoff=0)
        self.root.config(menu=self.p_menu)
        self.submenu.add_separator()
        self.p_menu.add_cascade(label="Edit",menu=self.submenu)
        self.submenu.add_command(label="Cut",command=self.cut)
        self.submenu.add_command(label="Copy",command=self.copy)
        self.submenu.add_separator()
        self.submenu.add_command(label="Paste",command=self.paste)
        self.submenu.add_separator()
        self.submenu.add_command(label="Replace",command=self.replace )

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste (self):
        self.textarea.event_generate("<<Paste>>")

    def replace (self):
        self.root.destroy()


if __name__ == "__main__":
    print("lol")