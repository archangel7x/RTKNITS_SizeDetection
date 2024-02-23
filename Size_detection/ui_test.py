import customtkinter as ct
from tkinter import messagebox
from tkinter import PhotoImage

f = "Roboto"
f1 = "Serif"
f2= "Monospace"
f3="Monaco"


def login():
    print("test")


def kill(root):
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()


   


def user_interface():



    ct.set_appearance_mode('Dark')
    #ct.set_default_color_theme('green')

    root = ct.CTk()
    root.title("Main Menu - RtKnits - Size Detection Software ")
    root.geometry("1920x1080")
   # bg_image = PhotoImage(file="images/better.png")
        # Create a label to hold the background image
   # background_label = ct.CTkLabel(master=root, image=bg_image)
   # background_label.place(relwidth=1, relheight=1)


    width = 100

    frame = ct.CTkFrame(master=root)
    frame.pack(pady=20, padx=30, fill="both", expand=True)

    
    #label = ct.CTkLabel(master=frame, text="\n                                                  Welcome                                                 \n", font=(f, 24), bg_color="black")
    label=ct.CTkLabel(master=frame,text="  Welcome  ",font=(f1, 24))
    label.pack(pady=75, padx=10)



    button1 = ct.CTkButton(master=frame, text=" Calibrate Camera ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="w")#,hover_color="gray")
    button1.pack(side="top", pady=12, padx=10)

    button2 = ct.CTkButton(master=frame, text=" Measuring Process ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button2.pack(side="top", pady=12, padx=10)

    button3 = ct.CTkButton(master=frame, text="   Comparing     ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button3.pack(side="top", pady=12, padx=10)

    button4 = ct.CTkButton(master=frame, text="   How to use    ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button4.pack(side="top", pady=12, padx=10)

    button5 = ct.CTkButton(master=frame, text="Exit", font=(f3, 20), width=width,fg_color="Red",border_color="Black", command=lambda:kill(root), anchor="center")
    button5.pack(side="top", pady=12, padx=10)

    # test = ct.CTkInputDialog ----> might be usefull for searching ids, or not if it is as simple as calling the other function? but will be good for compare
    #maybe already make an input box based of all the images it finds ^
    
    #background_label.lower()


    # ct.CTkToplevel ----> to create additional windows 
    root.protocol("WM_DELETE_WINDOW", lambda:kill(root))
    root.mainloop()




if __name__ =="__main__":
    user_interface()