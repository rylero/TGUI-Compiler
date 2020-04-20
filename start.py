from tkinter import *

inp = input("What tgui file would you like to run? ")
file = open(inp,"r")

t = None

action = False

guiStarted = False

buttons = []

for line in file.readlines():
	if line[0:-1] == "GUI START":
		guiStarted = True
		t = Tk()
		print("GUI Started")
	if guiStarted == True:
		if line.lstrip().rstrip().split(" ")[0] == "LABEL":
			label = Label(t,text=line.lstrip().rstrip().split(" ",1)[1])
			label.pack()
		if line.lstrip().rstrip().split(" ")[0] == "ENTRY":
			entry = Entry(t)
			entry.pack()
		if line.lstrip().rstrip().split(" ")[0].split("_",1)[0] == "BUTTON":
			button = Button(t,text=line.lstrip().rstrip().split(" ",1)[1])
			button.pack()
			buttons.append(line.lstrip().rstrip().split(" ")[0].split("_",1))
		if line.lstrip().rstrip().split(" ")[0] == "PRINT":
			print(line.lstrip().rstrip().split(" ",1)[1])

		if line.lstrip().rstrip().split(" ")[0] == "ACTION":
			for i in buttons:
				if i[1] == line.lstrip().rstrip().split(" ",1)[1]:
					action = True

		if line.lstrip().rstrip().split(" ")[0] == "END":
			action = False

print(buttons)

if guiStarted == True:
	t.mainloop() 