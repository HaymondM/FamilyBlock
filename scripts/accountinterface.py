#import sys
import tkinter as tk
from tkinter import messagebox
from deploy import blockactions

#sys.path.insert(0, './scripts')


def accountWindow():
    # Set Up Main window
    window_width = 600
    window_height = 400

    root = tk.Tk()

    def addinfo():
        # print(aa)
        aaa = userInaa.get()
        pkk = userInpk.get()
        mainblock.my_address = aaa
        mainblock.private_key = pkk
        print(mainblock.my_address)
        print(mainblock.private_key)
        userInpk.delete(0, tk.END)
        return messagebox.showinfo('FamilyBlock', "ACCOUNT ADDRESS and PRIVATE KEY added")

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

    # edit here

    # blockchain account
    aa = tk.Label(root, text="Enter Account Address")
    aa.place(relx=0.5, rely=0.1, anchor='s')

    txtVaraa = tk.StringVar(root)
    userInaa = tk.Entry(root, textvariable=txtVaraa, width=50)
    userInaa.place(relx=0.5, rely=0.1, anchor='n')

    # blockchain private key
    pk = tk.Label(root, text="Enter Private Key")
    pk.place(relx=0.5, rely=0.2, anchor='s')

    txtVarpk = tk.StringVar(root)
    userInpk = tk.Entry(root, textvariable=txtVarpk, width=50)
    userInpk.place(relx=0.5, rely=0.2, anchor='n')

    aainfo = userInaa.get()
    pkinfo = userInpk.get()

    mainblock = blockactions(aainfo, pkinfo)

    # set up buttons

    tk.Button(
        root,
        text="Add",
        command=lambda: addinfo()
    ).place(relx=0.5, rely=0.25, anchor='n')

    tk.Button(
        root,
        text="Exit",
        command=lambda: root.quit()
    ).place(relx=0.5, rely=0.9, anchor='n')

    '''For Testing 
    def test():
        print(mainblock.my_address)
        print(mainblock.private_key)
    tk.Button(
        root,
        text="test",
        command=lambda: test()
    ).place(relx=0.5, rely=0.5, anchor='n')
    '''
    root.mainloop()
