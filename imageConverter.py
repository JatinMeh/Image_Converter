from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox


root = Tk()

root.title("Image_Conversion_App")
root.config(bg="#f0ece1")


def jpg_to_png():
	global im1

	#take the jpg file from the computer
	import_filename = fd.askopenfilename()
	if import_filename.endswith(".jpg"):

		im1 = Image.open(import_filename)

		#save as
		export_filename = fd.asksaveasfilename(defaultextension=".png")
		im1.save(export_filename)

		messagebox.showinfo("success ", "your Image converted to Png")
	else:

		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=80, y=280)
		messagebox.showerror("Fail!!", "Something Went Wrong...")


def png_to_jpg():
	global im1
	import_filename = fd.askopenfilename()

	if import_filename.endswith(".png"):
		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".jpg")
		im1.save(export_filename)

		messagebox.showinfo("success ", "your Image converted to jpg ")
	else:
		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=80, y=280)

		messagebox.showerror("Fail!!", "Something Went Wrong...")


j2p = PhotoImage(file="j2p.png")
i2p = PhotoImage(file="i2p.png")

button1 = Button(root, text="JPG_to_PNG",image=j2p,command=jpg_to_png)
button1.place(x=100, y=20)

button2 = Button(root, text="PNG_to_JPEG",image=i2p,command=png_to_jpg)
button2.place(x=100, y=220)
root.geometry("500x500+400+200")
root.mainloop()
