# Standard imports
import cv2 as cv
import numpy as np
import pyautogui
import os 
import pandas as pd 
from PIL import Image 
import save as s  
import draw as d
import customtkinter as ct
from tkinter import messagebox
from tkinter import PhotoImage
import blob_detection2 as bd
import time  


def duplicate_check(path):
    if os.path.isfile(path):
        if messagebox.askokcancel("DUPLICATE ID FOUND", "Do you wish to comtinue"):
            cond =False

        else:
            cond = True 
            messagebox.showinfo("Duplicate ID", "Please try again with a different ID.")


        return cond
            
    else:
        print("No duplicate files found in dir... processing...")

def main(path,saving_directory,ident,after_wash):
    """
    # Read image
    cond = True
    while cond == True:"""

    #image1 = cv.imread("images/test9.png") #png 
    image1 = cv.imread(path) #jpg 
    im = cv.cvtColor(image1, cv.IMREAD_GRAYSCALE)
    size = pyautogui.size() # getting the size of the device's screen, for output window scalling
    #ident= int(input("enter image ID here:" ))

    #ond = duplicate_check(joined_path)


    camera_height = 65.5 
    



    #font for texts 
    font = cv.FONT_HERSHEY_SIMPLEX 

    # Set up the parameters for the detector
    params = cv.SimpleBlobDetector_Params()

    ###########################################################

    #FILTERING BLOBS/DOTS TO MODIFY IF NEEDED.

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 25 # Minimum blob area  #better5.png to change
    params.maxArea = 1000 #maximum blob area 

    # Filter by Circularity
    params.filterByCircularity = True 
    params.minCircularity = 0.55 #min circularity
    params.maxCircularity = 1# max circularity


    # Filter by Convexity
    params.filterByConvexity = False # Not used 
    params.minConvexity = 0.95  # Minimum convexity

    # Filter by Inertia? 
    params.filterByInertia = False #Not used 
    params.minInertiaRatio = 0.08  # Minimum inertia ratio

    # Create the detector with customized parameters
    detector = cv.SimpleBlobDetector_create(params)

    ############################################################


    # Detect blobs.
    keypoints = detector.detect(im)
    keypoints_coordinates = []
    # Draw detected blobs as red circles.
    # cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv.drawKeypoints(im, keypoints, np.array([]), (255, 0, 0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # org 
    org = (50, 50) 

    # fontScale 
    fontScale = 0.5

    # Blue color in BGR 
    color = (255, 0, 0) 

    # Line thickness 
    thickness = 1
    thickness2= 1

    # Using cv2.putText() method 
    im_with_keypoints = cv.putText(im_with_keypoints,f'IM_ID:{ident}', org, font,  
                    fontScale, color, thickness, cv.LINE_AA) 
    

     
    
    
    print("\n ##### keypoints found ##### \n")


    for i, keypoint in enumerate(keypoints):
        x, y = keypoint.pt
        keypoints_coordinates.append((x, y))
        print(f'Keypoint {i+1}: Coordinates: ({x}, {y})')
        
            # Convert the coordinates to integers
        x_int, y_int = int(x), int(y)   
        # Draw the text on the image
        cv.putText(im_with_keypoints, f'(k{i+1}: {x_int}, {y_int})', (x_int, y_int), font, fontScale, color, thickness, cv.LINE_AA)




   # cv.namedWindow('Keypoints', cv.WINDOW_NORMAL)  # Create a resizable window

    # Get the screen width and height
    #screen_width = size[0]
    #screen_height = size[1]

    # Resize the window to fit the screen
    #cv.resizeWindow('Keypoints', min(screen_width, 1920), min(screen_height, 1080))

    #cv.imshow("Keypoints", im_with_keypoints)

        # cv.waitKey(0)

       # Saving the first image
    s.save(ident,saving_directory,im_with_keypoints,measure=False)

    """
    while True:
        key = cv.waitKey(1) & 0xFF

        # Check if the 'ESC' key is pressed or the window is closed
        if key == 27 or cv.getWindowProperty('Keypoints', cv.WND_PROP_VISIBLE) < 1:
            break

    """


 

    cv.destroyAllWindows()

    d.draw(keypoints_coordinates, size, im_with_keypoints, thickness2,camera_height,font,org,fontScale,ident,saving_directory,after_wash)  


if __name__ == '__main__':

    #path = 'images/better2.png' 
    path = 'images/testing.png'
    #path = 'images/test3.jpg' 
    directory = 'saved_images'

    main(path,directory,7)
    cv.destroyAllWindows()
