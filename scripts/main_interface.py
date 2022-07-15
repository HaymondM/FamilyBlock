#from deploy import connection
from deploy import blockactions
from accountinterface import accountWindow
#import sys
import tkinter as tk

#sys.path.insert(0, './scripts')


# Set Up Main window
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
# Set Up Main window


def connect_to_block():
    INPUT = T.get("1.0", "end-1c")
    mainblock = blockactions(INPUT)

    res = mainblock.connection(INPUT)

    print(res)
    if res == True:
        root.destroy()
        accountWindow(mainblock)

    else:
        openFailWindow()


def openFailWindow():

    # Make a new window on top of root window
    failWindow = tk.Toplevel(root)

    # sets the title
    failWindow.title('Family Block')
    failWindow.config(bg='#adbce6')

    # sets the geometry

    # Set Up Main window
    Nwindow_width = 300
    Nwindow_height = 45
    screen_width = failWindow.winfo_screenwidth()
    screen_height = failWindow.winfo_screenheight()

    center_x = int(screen_width/2 - Nwindow_width / 2)
    center_y = int(screen_height/2 - Nwindow_height / 2)

    # set the position of the window to the center of the screen
    failWindow.geometry(
        f'{Nwindow_width }x{Nwindow_height}+{center_x}+{center_y}')

    tk.Label(failWindow,
             text="Failed to connect to the BlockChain").pack()

    # set the window to not be resizable
    failWindow.resizable(False, False)

    # set the icon
    failWindow.iconbitmap('.\\assets\FamilyBlock.ico')


def openMainWindow():
    # Make a new window on top of root window
    failWindow = tk.Toplevel(root)

    # sets the title
    failWindow.title('Family Block')
    failWindow.config(bg='#adbce6')

    # sets the geometry

    # Set Up Main window
    Nwindow_width = 300
    Nwindow_height = 45
    screen_width = failWindow.winfo_screenwidth()
    screen_height = failWindow.winfo_screenheight()

    center_x = int(screen_width/2 - Nwindow_width / 2)
    center_y = int(screen_height/2 - Nwindow_height / 2)

    # set the position of the window to the center of the screen
    failWindow.geometry(
        f'{Nwindow_width }x{Nwindow_height}+{center_x}+{center_y}')

    # A Label widget to show in toplevel
    tk.Label(failWindow,
             text="Failed to connect to the BlockChain").pack()

    # set the window to not be resizable
    failWindow.resizable(False, False)

    # set the icon
    failWindow.iconbitmap('.\\assets\FamilyBlock.ico')


# set up buttons
# Create button for next text.
button_connect = tk.Button(
    root, text="Connect", command=lambda: connect_to_block())


exit_button = tk.Button(
    root,
    text="Exit",
    command=lambda: root.quit()
).place(relx=0.5, rely=0.9, anchor='n')


# Set up text
# Create label
T = tk.Text(root, height=1, width=22)

l = tk.Label(root, text="Enter in the local blockchain address")
l.config(font=("Courier", 14))

address_text = "HTTP://127.0.0.1:7545"


l.pack()
button_connect.pack()
T.pack()
T.insert(tk.END, address_text)

root.mainloop()
