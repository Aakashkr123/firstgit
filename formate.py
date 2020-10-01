from tkinter import *
import tkinter.colorchooser as tkcolor
import tkinter.messagebox as tkmsg
count = 0
class Formate():

	def __init__(self,root,textarea):
		self.root = root
		self.textarea = textarea
		
	# changing background 
	def changeBg(self):
		color = tkcolor.askcolor()
		
		if color[1]== None:
			print('color not seleted')
			
		else:
			self.textarea["bg"] = color[1]
			
		
	# changing foreground 
	def changeFg(self):
		color = tkcolor.askcolor()
		self.textarea.configure(foreground=color[1])
		
		
	def Style(self,p_menu):
		# making parent menu
		self.p_menu = p_menu
		#child menu of parent 
		self.c_menu = Menu(self.p_menu,tearoff=False)
		self.p_menu.add_cascade(label='Style',menu=self.c_menu)
		self.c_menu.add_command(label='Bold',command=self.bold)
		
		self.c_menu.add_command(label='Italic',command=self.italic)
		
		self.c_menu.add_command(label='Underline',command=self.underline)
		self.c_menu.add_separator()
		self.c_menu.add_command(label='Reset',command=self.reset)
		self.c_menu.add_separator()
		self.c_menu.add_command(label='Background',command=self.changeBg)
		self.c_menu.add_command(label='Foreground',command=self.changeFg)


		self.i_b_u= "lucida 10 bold italic underline "
		self.i_b = "lucida 10 bold italic"
		self.u_i = "lucida 10 underline italic"
		self.u_b = "lucida 10 underline bold"
		self.i = "lucida 10 italic"
		self.b = "lucida 10 bold"
		self.u = "lucida 10 underline "
		
	def bold(self):
		global count
		if count == 0:
			self.textarea["font"]=self.b
			count = "b"

		elif count == "i":
			self.textarea["font"] = self.i_b
			count == "i_b"

		elif count == "u":
			self.textarea["font"] = self.u_b
			count = "u_b"

		else :
			self.textarea["font"] =self.i_b_u
			count = "eles"

	def italic(self,):
		global count
		if count == 0:
			self.textarea["font"] = self.i
			count = "i"

		elif count == "b":
			self.textarea["font"] = self.i_b
			count == "i_b"

		elif count == "u":
			self.textarea["font"] = self.u_i

		else :
			self.textarea["font"] =self.i_b_u
			count ="eles"



	def underline(self,):
		global count
		if count == 0:
			self.textarea["font"] = self.u
			count = "u"

		elif count == "b":
			self.textarea["font"] = self.u_b
			count == "u_b"

		elif count == "i":
			self.textarea["font"] = self.u_i

		else :
			self.textarea["font"] =self.i_b_u
			count = "eles"


	def reset(self):
		global count
		question = tkmsg.askquestion("Reset","With Background?")
		if question == "yes":
			self.textarea["font"] = "lucida 10"
			self.textarea["bg"] = "white"
			self.textarea["fg"] = "black"
			count = 0

		else:
			self.textarea["font"] = "lucida 10"
			count = 0


if __name__ == "__main__":
	print("run Formate sub classes ")


