import cv2 as cv
import numpy as np
import pyautogui
import os 
import pandas as pd 
from PIL import Image 


def save(ident,saving_directory,image,measure):

    if measure == False: 
       
       
            # Saving the first image
        
        filename = f'output_image{ident}.jpg'  #  change the filename and extension as needed

        # Make sure the directory exists
        if not os.path.exists(saving_directory):
            os.makedirs(saving_directory)

        # Provide the full path for the output image
        output_path = os.path.join(saving_directory, filename) 
        
        #opening the image auto, closing system image 

        # Save the image
        cv.imwrite(output_path, image) #Note to self: must check if file already exists

        print("\n--------------------------------------------------------------------")
        print(f'Successfully saved: {output_path}')
        print("----------------------------------------------------------------------\n")

        im= Image.open(str(output_path)) 
        im.show()  

    elif measure == True:

        filename = f'output_image_with_measures{ident}.jpg'  # You can change the filename and extension as needed
       

        # Make sure the directory exists
        if not os.path.exists(saving_directory):
            os.makedirs(saving_directory)

        # Provide the full path for the output image
        output_path = os.path.join(saving_directory, filename) 
        
        #opening the image auto, closing system image 

        # Save the image
        cv.imwrite(output_path, image) #Note to self: must check if file already exists

        print("\n--------------------------------------------------------------------")
        print(f'Successfully saved: {output_path}')
        print("----------------------------------------------------------------------\n")


        #im= Image.open(str(output_path)) 
        #im.show()  
    else:
        print("\n[ERROR]: wrong argument passed! File not saved.\n")



def savefile(ident,distance_top,distance_right,distance_bottom,distance_left):
        
        textfilename = f'{ident}.txt'
        datapath = 'saved_dimensions'

        if not os.path.exists(datapath):
            os.makedirs(datapath)


        joined_paths = os.path.join(datapath, textfilename)
        f=open(str(joined_paths),'w')
        f.write(f'top width:{distance_top}cm\nbottom width:{distance_bottom}cm\nright-height:{distance_right}cm\nleft-height:{distance_left}cm')
        print("\n--------------------------------------------------------------------")
        print(f'Successfully saved data file: {joined_paths}')
        print("----------------------------------------------------------------------\n")




        
def save_dataframe(ident, distance_top, distance_right, distance_bottom, distance_left,after_wash ,csv_file):
    
    # Read the existing CSV file into a DataFrame


    if after_wash == True: 
        try:
            df = pd.read_csv(csv_file, delimiter='\t')
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['ID', 'Initial Bottom Width', 'AfterWash_Bottom_width', 'Initial_Top_width', 'AfterWash_Top_width', 'Initial_Left_height', 'AfterWash_Left_Height', 'Initial_Right_height', 'AfterWash_Right_Height'])

        # Check if the ID already exists
        existing_row = df[df['ID'] == ident]

        if not existing_row.empty:
            # ID already exists, prompt the user for replacement
            user_decision = input(f"ID {ident} already exists. Do you want to replace the existing row? (yes/no): ").lower()

            if user_decision == 'yes':
                # Replace the existing row with the new data
                df.loc[existing_row.index[0]] = [ident, distance_bottom, distance_bottom, distance_top, distance_top, distance_left, distance_left, distance_right, distance_right]
                print(f"Row with ID {ident} replaced.")
            else:
                # User chose not to replace, do nothing
                print("No changes made.")
        else:
            # ID doesn't exist, append the new data to the DataFrame
            new_data = {'ID': ident,
                    
                        'AfterWash_Bottom_width': distance_bottom,
            
                        'AfterWash_Top_width': distance_top,
                     
                        'AfterWash_Left_Height': distance_left,
                  
                        'AfterWash_Right_Height': distance_right}

            df = df.append(new_data, ignore_index=True)
            print(f"Row with ID {ident} added.")

        # Write the updated DataFrame back to the CSV file
        df.to_csv(csv_file, sep='\t', index=False)







    elif after_wash == False:
        try:
            df = pd.read_csv(csv_file, delimiter='\t')
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame
            df = pd.DataFrame(columns=['ID', 'Initial Bottom Width', 'AfterWash_Bottom_width', 'Initial_Top_width', 'AfterWash_Top_width', 'Initial_Left_height', 'AfterWash_Left_Height', 'Initial_Right_height', 'AfterWash_Right_Height'])

        # Check if the ID already exists
        existing_row = df[df['ID'] == ident]

        if not existing_row.empty:
            # ID already exists, prompt the user for replacement
            user_decision = input(f"ID {ident} already exists. Do you want to replace the existing row? (yes/no): ").lower()

            if user_decision == 'yes':
                # Replace the existing row with the new data
                df.loc[existing_row.index[0]] = [ident, distance_bottom, distance_bottom, distance_top, distance_top, distance_left, distance_left, distance_right, distance_right]
                print(f"Row with ID {ident} replaced.")
            else:
                # User chose not to replace, do nothing
                print("No changes made.")
        else:
            # ID doesn't exist, append the new data to the DataFrame
            new_data = {'ID': ident,
                    
                        'Initial_Bottom_width': distance_bottom,
            
                        'Initial_Top_width': distance_top,
                     
                        'Initial_Left_height ': distance_left,
                  
                        'Initial_Right_height ': distance_right}

            df = df.append(new_data, ignore_index=True)
            print(f"Row with ID {ident} added.")

        # Write the updated DataFrame back to the CSV file
        df.to_csv(csv_file, sep='\t', index=False)

        


if __name__ == '__main__':
    save_dataframe(ident=7, distance_top=32.03, distance_right=33.56, distance_bottom=31.76, distance_left=33.92,after_wash=True ,csv_file='detection.csv')

