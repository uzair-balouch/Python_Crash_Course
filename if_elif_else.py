from tkinter import *

window = Tk()
window.title("City Dial Log")
window.resizable(False,False)
window.geometry('247x375')
window.iconbitmap('images/dou.ico')


entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=3)


def click_button(number):
	first_number = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(first_number) + str(number))


# Karchi = 021
# Faisalabad = 041
# Hyderabad = 0221
# Islamabad/Rawalpindi = 051
# Lahore = 042
# Multan = 061
# Okara = 0442
# Peshawar = 091
# Quetta = 081
# Sahiwal = 0441
# Sargodha = 0451
# Sialkot = 0524


def Check():
	check_number = entry.get()
	entry.delete(0, END)
	if check_number == '021':
		string_to_display = "*** " + check_number + " It's Karachi's Code  ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Karachi's Code.")
	elif check_number == '041':
		string_to_display = "*** " + check_number + " It's Faisalabad's Code ****"
		string_to_display = "*** " + check_number + " It's Faisalabad's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Faisalabad's Code.")
	elif check_number == '051':
		string_to_display = "*** " + check_number + " It's Islamabad/Rawalpindi's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Islamabad/Rawalpindi's Code.")
	elif check_number == '0221':
		string_to_display = "*** " + check_number + " It's Hyderabad's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Hyderabad's Code.")
	elif check_number == '042':
		string_to_display = "*** " + check_number + " It's Lahore's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Lahore's Code.")
	elif check_number == '061':
		string_to_display = "*** " + check_number + " It's Multan's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Multan's Code.")
	elif check_number == '0442':
		string_to_display = "*** " + check_number + " It's Okara's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Okara's Code.")
	elif check_number == '091':
		string_to_display = "*** " + check_number + " It's Peshawar's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Peshawar's Code.")
	elif check_number == '081':
		string_to_display = "*** " + check_number + " It's Quetta's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Quetta's Code.")
	elif check_number == '0441':
		string_to_display = "*** " + check_number + " It's Sahiwal's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Sahiwal's Code.")
	elif check_number == '0451':
		string_to_display = "*** " + check_number + " It's Sargodha's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Sargodha's Code.")
	elif check_number == '0524':
		string_to_display = "*** " + check_number + " It's Sialkot's Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print(check_number + " It's Sialkot's Code.")
	else:
		string_to_display = "*** It is wrong Code ****"
		label = Label(window, font=("Times",12, 'bold'))
		label["text"] = string_to_display
		label.grid(row=1, column=0, columnspan=3)
		print("***It is wrong Code***")
	entry.delete(0, END)


Button(window, text='1', height=5, width=7, command=lambda: click_button(1)).grid(row=2, column=0)
Button(window, text='2', height=5, width=7, command=lambda: click_button(2)).grid(row=2, column=1)
Button(window, text='3', height=5, width=7, command=lambda: click_button(3)).grid(row=2, column=2)
Button(window, text='4', height=5, width=7, command=lambda: click_button(4)).grid(row=3, column=0)
Button(window, text='5', height=5, width=7, command=lambda: click_button(5)).grid(row=3, column=1)
Button(window, text='6', height=5, width=7, command=lambda: click_button(6)).grid(row=3, column=2)
Button(window, text='7', height=5, width=7, command=lambda: click_button(7)).grid(row=4, column=0)
Button(window, text='8', height=5, width=7, command=lambda: click_button(8)).grid(row=4, column=1)
Button(window, text='9', height=5, width=7, command=lambda: click_button(9)).grid(row=4, column=2)
Button(window, text='0', height=5, width=7, command=lambda: click_button(0)).grid(row=5, column=0)
Button(window, text='Check', height=5, width=14, command=Check).grid(row=5, column=1, columnspan=2)





window.mainloop()
