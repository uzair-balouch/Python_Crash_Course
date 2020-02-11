from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Data of Universe")
window.resizable(False,False)
window.iconbitmap('images/dou.ico')
window.geometry("800x500")


image0 = ImageTk.PhotoImage(Image.open('images/0.jpg'))
image1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
image2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))
image3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
image4 = ImageTk.PhotoImage(Image.open('images/4.jpg'))


def Key_Pressed(event):
	if event.char == 'a':
		label = Label(window, image=image0)
		label.grid(row=0, column=0, columnspan=3)
		print("a key is pressed")
	if event.char == 's':
		label = Label(window, image=image1)
		label.grid(row=0, column=0, columnspan=3)
		print("s key is pressed")
	if event.char == 'd':
		label = Label(window, image=image2)
		label.grid(row=0, column=0, columnspan=3)
		print("d key is pressed")
	if event.char == 'f':
		label = Label(window, image=image3)
		label.grid(row=0, column=0, columnspan=3)
		print("f key is pressed")
	if event.char == 'g':
		label = Label(window, image=image4)
		label.grid(row=0, column=0, columnspan=3)
		print("g key is pressed")






window.bind("<Key>", Key_Pressed)








window.mainloop()
