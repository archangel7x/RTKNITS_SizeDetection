import customtkinter as ct
from tkinter import messagebox
from tkinter import PhotoImage
import blob_detection2 as bd
import time 
import os

f = "Roboto"
f1 = "Serif"
f2= "Monospace"
f3="Monaco"


def kill(root):
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()
        return


def calling_measuring_process(path,directory,font_n):

    after_wash  = str(input("is the image after washing?: "))

    if after_wash == 'y':
        after_wash = True


    elif after_wash =='n':
        after_wash = False

    else:
        print("wrong input")



    def on_enter():
    
        print("test")
        i = ident.get()
        print(i)
        root2.destroy()

        if i :
            filename = f'output_image{i}.jpg'
            joined_path = os.path.join(directory, filename)
            cond = bd.duplicate_check(joined_path)


            if cond == True: 
                calling_measuring_process(path,directory,f2)
                return 
            
            else:
                bd.main(path,directory,i,after_wash)



    ct.set_appearance_mode('Dark')
    root2 = ct.CTk()
    root2.title("Measuring Process - RtKnits - Size Detection Software ")
    root2.geometry("600x600")

    frame2 = ct.CTkFrame(master=root2)
    frame2.pack(pady=20, padx=30, fill="both", expand=True)

    labeli=ct.CTkLabel(master=frame2,text=" Enter a Unique Identifier for your image:",font=(f2, 15))
    labeli.pack(pady=12, padx=10)

    ident = ct.CTkEntry(master=frame2, placeholder_text="Enter Image UID here: ")
    ident.pack(pady=12, padx=10)

    enter = ct.CTkButton(master=frame2, text="Enter", font=(f2, 20), width=200, fg_color=("transparent"), hover_color="#151515", anchor="center",command=on_enter)
    enter.pack(side="top", pady=12, padx=10)



    root2.wait_window()




    

def user_interface(path,direc):



    ct.set_appearance_mode('Dark')
    #ct.set_default_color_theme('green')

    root = ct.CTk()
    root.title("Main Menu - RtKnits - Size Detection Software ")
    root.geometry("600x600")


    width = 100

    frame = ct.CTkFrame(master=root)
    frame.pack(pady=20, padx=30, fill="both", expand=True)

    
    #label = ct.CTkLabel(master=frame, text="\n                                                  Welcome                                                 \n", font=(f, 24), bg_color="black")
    label=ct.CTkLabel(master=frame,text="   ~Welcome~  ",font=(f1, 24))
    label.pack(pady=75, padx=10)



    button1 = ct.CTkButton(master=frame, text="  Calibrate Camera ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")#,hover_color="gray")
    button1.pack(side="top", pady=12, padx=10)

    button2 = ct.CTkButton(master=frame, text="  Measuring Process ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", command=lambda:calling_measuring_process(path,direc,f2),anchor="center")
    button2.pack(side="top", pady=12, padx=10)

    button3 = ct.CTkButton(master=frame, text="    Comparing     ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button3.pack(side="top", pady=12, padx=10)

    button6 =ct.CTkButton(master=frame, text="    Settings     ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button6.pack(side="top", pady=12, padx=10)

    button4 = ct.CTkButton(master=frame, text="    How to use    ", font=(f2, 20), width=width,fg_color=( "transparent"),hover_color="#151515", anchor="center")
    button4.pack(side="top", pady=12, padx=10)

    button5 = ct.CTkButton(master=frame,text="Exit", font=(f3, 20), width=width,fg_color="Red",border_color="Black", command=lambda:kill(root), anchor="center")
    button5.pack(side="top", pady=12, padx=10)

    # test = ct.CTkInputDialog ----> might be usefull for searching ids, or not if it is as simple as calling the other function? but will be good for compare
    #maybe already make an input box based of all the images it finds ^
    

    # ct.CTkToplevel ----> to create additional windows 
    root.protocol("WM_DELETE_WINDOW", lambda:kill(root))
    root.mainloop()




if __name__ =="__main__":
    path = 'images/testing.png'
    directory = 'saved_images'
    user_interface(path,directory)