#import sys
import tkinter as tk
from tkinter import messagebox
#from deploy import blockactions
from enterinfo import infoWindow


#sys.path.insert(0, './scripts')


def accountWindow(mainblock):
    # Set Up Main window
    window_width = 600
    window_height = 400

    root = tk.Tk()

    def addinfo():
        # print(aa)
        aaa = userInaa.get()
        pkk = userInpk.get()
        mainblock.addmaindata(aaa, pkk, 1337)
        print(mainblock.my_address)
        print(mainblock.private_key)
        userInpk.delete(0, tk.END)
        return messagebox.showinfo('FamilyBlock', "ACCOUNT ADDRESS and PRIVATE KEY added")

    def addfaminfo():
        # print(aa)
        Inna = userInna.get()
        Inag = userInag.get()
        Inda = userInda.get()
        Inba = userInba.get()
        #Infa = userInfa.get()

        mainblock.adddata(Inna, Inag, Inda, Inba)
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

    # start family inputs
    pk = tk.Label(root, text="Name")
    pk.place(relx=0.75, rely=0.4, anchor='s')

    txtVarna = tk.StringVar(root)
    userInna = tk.Entry(root, textvariable=txtVarna, width=50)
    userInna.place(relx=0.75, rely=0.4, anchor='n')

    pk = tk.Label(root, text="Age")
    pk.place(relx=0.75, rely=0.5, anchor='s')

    txtVarag = tk.StringVar(root)
    userInag = tk.Entry(root, textvariable=txtVarag, width=50)
    userInag.place(relx=0.75, rely=0.5, anchor='n')

    pk = tk.Label(root, text="Date of birth")
    pk.place(relx=0.75, rely=0.6, anchor='s')

    txtVarda = tk.StringVar(root)
    userInda = tk.Entry(root, textvariable=txtVarda, width=50)
    userInda.place(relx=0.75, rely=0.6, anchor='n')

    pk = tk.Label(root, text="BirthPlace")
    pk.place(relx=0.75, rely=0.7, anchor='s')

    txtVarba = tk.StringVar(root)
    userInba = tk.Entry(root, textvariable=txtVarba, width=50)
    userInba.place(relx=0.75, rely=0.7, anchor='n')

    #pk = tk.Label(root, text="Family ID")
    #pk.place(relx=0.75, rely=0.8, anchor='s')

    #txtVarfa = tk.StringVar(root)
    #userInfa = tk.Entry(root, textvariable=txtVarfa, width=50)
    #userInfa.place(relx=0.75, rely=0.8, anchor='n')

    # End Family ID

    aainfo = userInaa.get()
    pkinfo = userInpk.get()

    # set up buttons

    tk.Button(
        root,
        text="Add",
        command=lambda: addinfo()
    ).place(relx=0.5, rely=0.25, anchor='n')

    tk.Button(
        root,
        text="Enter info",
        command=lambda: addfaminfo()
    ).place(relx=0.75, rely=0.9, anchor='n')

    tk.Button(
        root,
        text="Retrieve a family tree/persons info",
        command=lambda: root.quit()
    ).place(relx=0.25, rely=0.5, anchor='n')

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