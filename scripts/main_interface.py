from deploy import connection
#import sys
import tkinter as tk

#sys.path.insert(0, './scripts')


def connect_to_block():
    INPUT = T.get("1.0", "end-1c")
    print(connection(INPUT))


window_width = 600
window_height = 400

root = tk.Tk()

root.title('Family Block')
root.config(bg='#adbce6')
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set the window to not be resizable
root.resizable(False, False)

# set the icon
root.iconbitmap('.\\assets\FamilyBlock.ico')

# Set up text
# Create label
T = tk.Text(root, height=1, width=22)

l = tk.Label(root, text="Enter in the local blockchain address")
l.config(font=("Courier", 14))

address_text = "HTTP://127.0.0.1:7545"

# Create button for next text.
button_connect = tk.Button(
    root, text="Connect", command=lambda: connect_to_block())

l.pack()
button_connect.pack()
T.pack()
T.insert(tk.END, address_text)

# set up buttons
exit_button = tk.Button(
    root,
    text="Exit",
    command=lambda: root.quit()
).place(x=265, y=350)


root.mainloop()
