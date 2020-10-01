import formate as formate_logs
import file_menu as file_logs
import tkinter as tk
import tkinter.simpledialog as s_log
import helpmenu as hp
import editmenu as ed
import MySQLdb
count = 0
# try to connet with mysqldb
try:
    conn = MySQLdb.connect(
        user="root",
        host="localhost",
        password="1234",
        database="users"
    )
    def connected(roll):
        command = f"select * from friends where password = '{roll}'"
        try:
            myc = conn.cursor()
            myc.execute(command)
            row = myc.fetchone()
            print(row[1])
            safe0.main()
            myc.close()
            conn.close()



        except:
            print("not abailabe")



except:
    print("connection error\n"
          "may be not connected")








root = tk.Tk()
root.title("My Diary")
textarea = tk.Text(root)
textarea.pack(fill="both",expand=1)


p_menu = tk.Menu(root)
safe_menu = tk.Menu(root)
root.config(menu=p_menu)

def head_menu():
    #file menu updated
    file_l = file_logs.File(root,textarea,p_menu)


    # formate menu updated
    formate = formate_logs.Formate(root,textarea)
    formate.Style(p_menu)

    # help menu
    helpmenu = hp.Helpmenu(root,textarea,p_menu)

    #edit menu updated
    edit = ed.EditMenu(root,textarea,p_menu)

head_menu()
class Safe():
    def __init__(self,root,textarea,safe_menu,**no):
        self.root = root
        self.textarea = textarea
        self.safe_menu = safe_menu
        self.no = no
        self.count = 0

    def safe(self):
        self.root.config(menu=self.safe_menu)
        self.submenu = tk.Menu(self.safe_menu, tearoff=False)
        for k, v in self.no.items():
            self.submenu.add_command(label=k, command=v)
        self.safe_menu.add_cascade(label="SAFE FILE", menu=self.submenu)


    def main(self):
        global p_menu
        if self.count == 0 :
            try :
                p_menu.destroy()
                self.safe()


                self.count = 1

            except:
                p_menu.destroy()
                self.safe_menu = tk.Menu(self.root)
                self.safe()
                self.count = 1

        else:
            try:
                self.safe_menu.destroy()
                head_menu()
                self.count = 0

            except:
                print("error")

                p_menu = tk.Menu(self.root)
                self.safe_menu.destroy()
                head_menu()
                self.count = 0







safe0 = Safe(root,textarea,safe_menu)
def safe_conn(event):
    global count
    if count == 0:
        roll = s_log.askstring("PASSWORD","Enter the password of database friends ")
        connected(roll)
        count = 1

    else:
        safe0.main()

root.bind("<Control-q>",safe_conn)




root.mainloop()
