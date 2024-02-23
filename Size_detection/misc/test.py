import cv2 as cv 






def show(height,width,new_height,new_width,h_difference,w_difference):

    print("------------------------------------------------------\n")
    print(f'-Initial height:{height}  | -New height:{new_height}\n-Initial width:{width}   | -New width:{new_width}')
    print(f'\n>> height difference: {h_difference}')
    print(f'>> width difference: {w_difference}\n')
    print("------------------------------------------------------\n")



def calculate(height,width,new_height,new_width):


    if new_height!= 0 and new_width != 0 and height!=0 and width!=0:
        if new_height!= None and new_width != None and height!=None and width!=None: 

            if new_height > height and new_width> width:
                h_difference = new_height - height
                w_difference = new_width - width
                show(height,width,new_height,new_width,h_difference,w_difference)


            elif height > new_height and width > new_width:
                h_difference = height - new_height
                w_difference = width  - new_width
                show(height,width,new_height,new_width,h_difference,w_difference)




            else:
                print("\n-------------------")
                print("same dimensions!")
                print("-------------------")

        

        else:
            print("\n-----------------------------")
            print("Heights and widths are empty!")
            print("-----------------------------")


    else:
        print("\n-----------------------------")
        print("heights and widths = 0 ")
        print("\n-----------------------------")





if __name__ =='__main__':

    """
    operations = 0 
    cond = True 

    while cond == True:

        try: 
            choice = str(input("do you want to scan a new"))

        except ValueError: 
            print("invalid input please try again")

    """
    
    calculate(35,35,37,37)
    calculate(34,34,30,30)
    calculate(35,35,35,35)
    calculate(None,None,None,None)
    calculate(0,0,0,0)
    

