import tkinter as tk
import sys

trans = {chr(x) : "%02d" % (x - 96) for x in range(97, 97 + 26)}
trans[' '] = '00'

root = None
text = None

class Struct(object):
    pass

def run():
    global root
    global text

    root = tk.Tk()

    root.bind("<Key>",key_pressed)
    root.bind("<BackSpace>", bs_pressed)
    root.bind("<Return>", en_pressed)
    root.bind("<Escape>", quit)

    canvas = tk.Canvas(root, width=1200, height=600)
    canvas.pack()

    text = tk.Text(canvas, width=120, height=40)
    canvas.create_window((0, 0), window=text, anchor='nw')

    root.mainloop()

#
# Callback to handle any key pressed
#
def key_pressed(event):
    try:
        print(event.keycode)
        if event.char == ".":
            text.insert(tk.INSERT, ".")
        else:
            text.insert(tk.INSERT, str(trans[event.char]) + " ")
    except:
        print("Unable to encode character")

#
# Callback to quit the application
#
def quit(event):
    global root
    root.quit()

#
# Callback to handle backspaces
#
def bs_pressed(event):
    text.delete("insert -3 chars", tk.INSERT)

#
# Callback to handle Return key pressed
#
def en_pressed(event):
    fd = open('text.txt', 'w')
    data = text.get("1.0", "end-1c")
    data = data.split()
    data = [x for x in data if x != "."]

    data = "\n".join(data)

    fd.write(data)
    fd.close()

#
# The main entry point
#
if __name__ == "__main__":
    run()
