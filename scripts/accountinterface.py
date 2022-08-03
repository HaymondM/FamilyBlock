#import sys
import tkinter as tk
from tkinter import messagebox
#from deploy import blockactions
#from enterinfo import infoWindow
from familytree import familyTree


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
        Inco1 = userInco1.get()
        Inco2 = userInco2.get()
        #Infa = userInfa.get()
        #print(Inna, Inag)

        personcon = mainblock.adddata(Inna, Inag, Inda, Inba, Inco1, Inco2)
        return messagebox.showinfo('FamilyBlock', f"Here is the contract number of the person: {personcon}")

    def getfaminfo():
        # print(aa)
        userIncoo = userInco.get()

        person1 = mainblock.getdata(userIncoo)
        if person1[0][5] or person1[0][6] != 'N/A':  # has parent info
            p2con = person1[0][5]
            p3con = person1[0][6]
            person2 = mainblock.getdata(p2con)
            person3 = mainblock.getdata(p3con)
            print('here1')
            if person2[0][5] or person2[0][6] != 'N/A':  # has parent info
                p4con = person2[0][5]
                p5con = person2[0][6]
                print(person2[0][0])
                print(p5con)
                person4 = mainblock.getdata(p4con)
                person5 = mainblock.getdata(p5con)
                print('here2')
            if person3[0][5] or person3[0][6] != 'N/A':  # has parent info
                p6con = person3[0][5]
                p7con = person3[0][6]
                person6 = mainblock.getdata(p6con)
                person7 = mainblock.getdata(p7con)

        familyTree(mainblock, person1, person2, person3,
                   person4, person5, person6, person7)
        # return messagebox.showinfo('FamilyBlock', f"{persontree}")

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
    pk.place(relx=0.75, rely=0.35, anchor='s')

    txtVarna = tk.StringVar(root)
    userInna = tk.Entry(root, textvariable=txtVarna, width=50)
    userInna.place(relx=0.75, rely=0.35, anchor='n')

    pk = tk.Label(root, text="Age")
    pk.place(relx=0.75, rely=0.45, anchor='s')

    txtVarag = tk.StringVar(root)
    userInag = tk.Entry(root, textvariable=txtVarag, width=50)
    userInag.place(relx=0.75, rely=0.45, anchor='n')

    pk = tk.Label(root, text="Date of birth")
    pk.place(relx=0.75, rely=0.55, anchor='s')

    txtVarda = tk.StringVar(root)
    userInda = tk.Entry(root, textvariable=txtVarda, width=50)
    userInda.place(relx=0.75, rely=0.55, anchor='n')

    pk = tk.Label(root, text="BirthPlace")
    pk.place(relx=0.75, rely=0.65, anchor='s')

    txtVarba = tk.StringVar(root)
    userInba = tk.Entry(root, textvariable=txtVarba, width=50)
    userInba.place(relx=0.75, rely=0.65, anchor='n')

    pk = tk.Label(root, text="Contract # of mom")
    pk.place(relx=0.75, rely=0.75, anchor='s')

    txtVarco1 = tk.StringVar(root)
    userInco1 = tk.Entry(root, textvariable=txtVarco1, width=50)
    userInco1.place(relx=0.75, rely=0.75, anchor='n')

    pk = tk.Label(root, text="Contract # of dad")
    pk.place(relx=0.75, rely=0.85, anchor='s')

    txtVarco2 = tk.StringVar(root)
    userInco2 = tk.Entry(root, textvariable=txtVarco2, width=50)
    userInco2.place(relx=0.75, rely=0.85, anchor='n')

    #enter in contract
    pk = tk.Label(root, text="Contract # of person")
    pk.place(relx=0.25, rely=0.45, anchor='s')

    txtVarba = tk.StringVar(root)
    userInco = tk.Entry(root, textvariable=txtVarba, width=25)
    userInco.place(relx=0.25, rely=0.45, anchor='n')

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
        command=lambda: getfaminfo()
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
