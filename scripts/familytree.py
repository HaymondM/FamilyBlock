#import sys
import tkinter as tk
from tkinter import messagebox
#from deploy import blockactions
from enterinfo import infoWindow


#sys.path.insert(0, './scripts')


def familyTree(mainblock, mainperson, person2, person3,
               person4, person5, person6, person7):

    def disinfo(person):
        disformat = f'Name: {person[0][0]}\n Age: {person[0][1]}\n Birth Year: {person[0][2]}\n Birhtplace: {person[0][3]}\n'
        return messagebox.showinfo('FamilyBlock', disformat)

    # Set Up Main window
    window_width = 600
    window_height = 400

    root = tk.Tk()

    root.title('Family Block')
    root.config(bg='#adbce6')
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()
    # Create a line in canvas widget
    canvas.create_line(350, 250, 300, 300, width=5)  # p1R
    canvas.create_line(250, 250, 300, 300, width=5)  # p1L

    canvas.create_line(450, 150, 353, 247, width=5)  # p1RR
    canvas.create_line(150, 150, 247, 247, width=5)  # p1LL

    canvas.create_line(325, 150, 353, 247, width=5)  # p1RRR
    canvas.create_line(275, 150, 250, 250, width=5)  # p1LLL

    canvas.configure(bg='#adbce6')

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # Create a canvas widget

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # set the window to not be resizable
    root.resizable(False, False)

    # set the icon
    root.iconbitmap('.\\assets\FamilyBlock.ico')
    # Set Up Main window

    # edit here

    mtext = mainperson[0][0]  # get main name
    # get person parents
    p2text = person2[0][0]
    p3text = person3[0][0]
    # get person parents
    p4text = person4[0][0]
    p5text = person5[0][0]
    p6text = person6[0][0]
    p7text = person7[0][0]

    aa = tk.Label(root, text="The Family Tree",
                  bg='#adbce6', fg='#FF7F7F')
    aa.config(font=('Helvetica bold', 25))
    aa.place(relx=0.5, rely=0.12,  anchor='s')

    # be able to click name of person to get more info
    tk.Button(
        root,
        text=mtext,
        command=lambda: disinfo(mainperson)
    ).place(relx=0.5, rely=0.73, anchor='n')

    tk.Button(
        root,
        text=p2text,
        command=lambda: disinfo(person2)
    ).place(relx=0.42, rely=0.6, anchor='n')

    tk.Button(
        root,
        text=p3text,
        command=lambda: disinfo(person3)
    ).place(relx=0.59, rely=0.6, anchor='n')

    tk.Button(
        root,
        text=p4text,
        command=lambda: disinfo(person4)
    ).place(relx=0.57, rely=0.35, anchor='n')

    tk.Button(
        root,
        text=p7text,
        command=lambda: disinfo(person7)
    ).place(relx=0.4, rely=0.35, anchor='n')  # grandma dad

    tk.Button(
        root,
        text=p6text,
        command=lambda: disinfo(person6)
    ).place(relx=0.2, rely=0.35, anchor='n')  # grandpa dad

    tk.Button(
        root,
        text=p5text,
        command=lambda: disinfo(person5)
    ).place(relx=0.74, rely=0.35, anchor='n')

    tk.Button(
        root,
        text="Go Back",
        command=lambda: root.destroy()
    ).place(relx=0.52, rely=0.9, anchor='n')

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
