# Span remover

First (and probably last) project in Python :)

Version v1.0 differed in the fact that two buttons were added in versions v1.1 and v1.2:
- Delete span and copy(second button)
- Delete div and copy(third button)

**Source code is located in the "src-code" folder**

----------

## The origin of the program

In my work, copywriters throw the prepared text into CRM. They have to use the right colors in the text when uploading, so when uploading text to a text editor (Joomla) it is problematic - it adds "span" if you paste only with CTRL+V, I know you can do it with CTRL+SHIFT+V, but then you have to set bold, headers and linking again, and it takes some time. I saw that in CRM there is an option of suspicious source code and found that the process of copying the content can be optimized. At that time I was just interested in the Python language, and more specifically in the subject of web scraping. I decided to take up this topic because it seemed quite simple to me. At the very beginning I created the whole graphic interface. Then I created an option that removes span from HTML tags. The most important thing I wanted to do was to set the H1 tag directly in HTML, if it was the first one to appear (copywriters let us know then that it will be one of the headers e.g.: H1: About us, H2: Home page). At this point a more experienced friend helped me. Next, I simply added the same option to remove span and div. Currently, the program works in such a way that we insert HTML source code, click the appropriate button, and this removes the tags and automatically copies them to our clipboard and can be directly pasted into the source code in our text editor. From what I've noticed this program optimizes our work a lot.

This program did not need any approval from the management because it does not interfere with the software and systems we use.

----------

## How it works?

- First button -> If you paste the source code: `<p><span>Example</span></p>` you will receive `<p>Example</p>` and it will be copied to the system clipboard.
- Second button -> If you paste the source code: `<p><span>H1: Example</span></p>` you will receive `<h1>Example</h1>` and this will be copied to the system clipboard.
- Third button -> If you paste the source code: `<div><p>H1: Example</p></div>` you will receive `<p>Example</p>` and this will be copied to the system clipboard.

This program is in Polish because I work in a Polish company and most employees find it easier to speak in their native language.

----------

## What next?

One day I would like to improve the program so that linking in the text changes to the appropriate HTML tags in our Joomla text editor. We get from the copywriters e.g: (linking to: Windows). Currently no time.

----------

## What have I learned in this project?

I learned in this project:
- Use basic concepts in Python
- How to generate an application.exe using Python EXE Executable
- Create a graphical interface using Tkinter
- Use the Beautiful Soup option
- Use the pyperclip option to copy to the system clipboard

----------

## What made me most of the problems?

The biggest problem for me was the transformation of the text into source code e.g:
- H1: About us -> `<h1>About us</h1>`

----------

## A few words from me

Python is not my main language, but only a side language. I was interested in this language because of its simplicity and popularity. I spent one month on this language together - including learning and writing this program. I used the course with Udemy and read a book -> Automate the Boring Stuff with Python.

I'm sorry about my English not very good. I'm trying to improve my level overnight, I used -> [deepl.com](https://www.deepl.com/translator) to translate most of it.

**Thank you for reading and taking your time :)**