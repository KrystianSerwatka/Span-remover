from bs4 import BeautifulSoup
from tkinter import *
import pyperclip
import re

root = Tk()
root.title("Span remover")
root.iconbitmap('.ico/span.ico')

root.geometry("800x600")

v = StringVar()

yourText = Label(root, text="Wprowadź poniżej kod")
yourText.pack(pady=10)

textEntry = Entry(root, textvariable=v, width=75)
textEntry.pack(pady=10)


def Take_input():
    soup = BeautifulSoup(textEntry.get(), 'html.parser')

    for match in soup.findAll('span'):
        match.unwrap()

    for match in soup.find_all('p'):
        if ('H1:' in match.text) or ('H1: ' in match.text) or ('h1:' in match.text) or ('h1: ' in match.text):
            tag = match
            tag.name = 'h1'
            tag.string = tag.text[3:len(tag.text)].lstrip(' ')
        elif ('H2:' in match.text) or ('H2: ' in match.text) or ('h2:' in match.text) or ('h2: ' in match.text):
            tag = match
            tag.name = 'h2'
            tag.string = tag.text[3:len(tag.text)].lstrip(' ')
        elif ('H3:' in match.text) or ('H3: ' in match.text) or ('h3:' in match.text) or ('h3: ' in match.text):
            tag = match
            tag.name = 'h3'
            tag.string = tag.text[3:len(tag.text)].lstrip(' ')
        elif ('H4:' in match.text) or ('H4: ' in match.text) or ('h4:' in match.text) or ('h4: ' in match.text):
            tag = match
            tag.name = 'h4'
            tag.string = tag.text[3:len(tag.text)].lstrip(' ')

    Output.insert(END, soup)

    global myLabel
    myLabel = Label(root, text="Usunięto i skopiowano!")
    myLabel.pack()
    myLabel.after(3000, myLabel.destroy)

    pyperclip.copy(Output.get("1.0", END))

    textEntry.delete(0, 'end')

    Output.after(3000, lambda: Output.delete('1.0', END))


def clearButton():
    textEntry.delete(0, END)
    Output.delete('1.0', END)


def deleteSpan():
    soup = BeautifulSoup(textEntry.get(), 'html.parser')

    for match in soup.findAll('span'):
        match.unwrap()

    Output.insert(END, soup)

    myLabel = Label(root, text="Usunięto i skopiowano!")
    myLabel.pack()
    myLabel.after(3000, myLabel.destroy)

    pyperclip.copy(Output.get("1.0", END))

    textEntry.delete(0, 'end')

    Output.after(3000, lambda: Output.delete('1.0', END))


def deleteDiv():
    soup = BeautifulSoup(textEntry.get(), 'html.parser')

    for match in soup.findAll('div'):
        match.unwrap()

    Output.insert(END, soup)

    myLabel = Label(root, text="Usunięto i skopiowano!")
    myLabel.pack()
    myLabel.after(3000, myLabel.destroy)

    pyperclip.copy(Output.get("1.0", END))

    textEntry.delete(0, 'end')

    Output.after(3000, lambda: Output.delete('1.0', END))


removeButton = Button(
    root, text="Usuń span oraz zamień na nagłówek i skopiuj", command=Take_input)
removeButton.pack(pady=5)

removeSpan = Button(root, text="Usuń span i skopiuj", command=deleteSpan)
removeSpan.pack(pady=5)

removeDiv = Button(root, text="Usuń div i skopiuj", command=deleteDiv)
removeDiv.pack(pady=5)

Output = Text(root, height=15,  width=75,  bg="light cyan")
Output.pack(pady=10)

cleanButton = Button(root, text="Wyczyść", command=clearButton)
cleanButton.pack(pady=10)

createdBy = Label(root, text="© Copyright Krystian Serwatka")
createdBy.pack(side=BOTTOM)

version = Label(root, text="Version: 1.2")
version.pack(side=BOTTOM)

root.mainloop()