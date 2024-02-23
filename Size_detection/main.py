import blob_detection as d 
import random

def menu():

    print("\n#### WELCOME ####\n")
    print("1. Calibrate Camera")
    print("2. Mesuring Process")
    print("3. Comparing")
    print("4. How to use")
    print("5. Exit")



if __name__ == '__main__':

    path = 'images/testing.png' # must make user input when building UI and save it as a config file 

    directory = 'saved_images'
    cond =True
    goodbye= ["\n See you soon! :) ","\n Goodbyeee! ;)", "\n Have a nice evening! :)"]

    while cond  == True:

        menu()
        try: 
            choice = int(input("\n> Please make a selection: "))
        except:
            raise ValueError('\n----- [ERROR]: incorrect format please try again.\n')
        

        if choice <= 0 or choice >5:
            print("[ERROR: invalid selections.... please try again")

        elif choice == 2:
            d.main(path,directory)
            str(input('hit any key to continue...\n'))


        elif choice == 5:
            bye = random.choice(goodbye)
            print(bye)
            cond = False 

        




    
        
    


    


