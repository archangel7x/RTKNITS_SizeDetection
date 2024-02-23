import cv2 as cv
import numpy as np
import pyautogui
import os 
import pandas as pd 
from PIL import Image 
import save as s


def calculate_distance(point1, point2, camera_height):
    # Assuming camera_height is in centimeters
    pixel_distance = np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    # Assuming the field of view is 60 degrees
    angle_in_radians = np.radians(60)
    real_world_distance = 2 * camera_height * np.tan(angle_in_radians / 2) * (pixel_distance / 1080)
    return real_world_distance


def draw(keypoints_coordinates, size, image, thickness,camera_height,font,org,fontScale,ident,saving_directory):
    top_right = []
    top_left = []
    bottom_right = []
    bottom_left = []
    color = (0, 255, 0)
  

    input_top_right = int(input("input the top right keypoint number "))
    input_top_left = int(input("input the top left keypoint number "))
    input_bottom_right = int(input("input the BOTTOM right keypoint number "))
    input_bottom_left = int(input("input the BOTTOM left keypoint number "))

    top_right.append(keypoints_coordinates[input_top_right - 1])
    print(top_right)
    print(top_right[0][1])

    top_left.append(keypoints_coordinates[input_top_left - 1])
    print(top_left)

    bottom_right.append(keypoints_coordinates[input_bottom_right - 1])
    print(bottom_right)

    bottom_left.append(keypoints_coordinates[input_bottom_left - 1])
    print(bottom_left)

    # Extract the points from the lists and convert to integers
    top_right = tuple(map(int, top_right[0]))
    top_left = tuple(map(int, top_left[0]))
    bottom_right = tuple(map(int, bottom_right[0]))
    bottom_left = tuple(map(int, bottom_left[0]))
    #print("test:",top_right)


    # Draw lines between the points
    cv.line(image, top_left, top_right, color, thickness)
    cv.line(image, top_right, bottom_right, color, thickness)
    cv.line(image, bottom_right, bottom_left, color, thickness)
    cv.line(image, bottom_left, top_left, color, thickness)



    # Calculate distances between lines
    distance_top = calculate_distance(top_left, top_right, camera_height)           #distance from the top left point to the top right point
    distance_right = calculate_distance(top_right, bottom_right, camera_height)     #distance from the top right point to the bottom right point
    distance_bottom = calculate_distance(bottom_left, bottom_right,camera_height)   #distance from the bottem left to bottom left point
    distance_left = calculate_distance(bottom_left, top_left, camera_height)        #distance from bottom left to top left point 

    print(f"Distance Top: {distance_top:.2f} cm")
    print(f"Distance Right: {distance_right:.2f} cm")
    print(f"Distance Bottom: {distance_bottom:.2f} cm")
    print(f"Distance Left: {distance_left:.2f} cm")
        
        
        
        
# Define the positions for putting text next to each line
    text_position_top = ((top_left[0] + top_right[0]) // 2, (top_left[1] + top_right[1]) // 2 -5 )
    text_position_right = ((top_right[0] + bottom_right[0]) // 2 -80 , (top_right[1] + bottom_right[1]) // 2 -25) 
    text_position_bottom = ((bottom_left[0] + bottom_right[0]) // 2, (bottom_left[1] + bottom_right[1]) // 2 - 5)
    text_position_left = ((bottom_left[0] + top_left[0]) // 2 -80 , (bottom_left[1] + top_left[1]) // 2 -25 )

   # Draw text next to each line
    image = cv.putText(image, f"{distance_top:.2f} cm", text_position_top, font, fontScale, color, thickness, cv.LINE_AA)
    image = cv.putText(image, f"{distance_right:.2f} cm", text_position_right, font, fontScale, color, thickness, cv.LINE_AA)
    image = cv.putText(image, f"{distance_bottom:.2f} cm", text_position_bottom, font, fontScale, color, thickness, cv.LINE_AA)
    image = cv.putText(image, f"{distance_left:.2f} cm", text_position_left, font, fontScale, color, thickness, cv.LINE_AA)



    cv.namedWindow('Keypoints', cv.WINDOW_NORMAL)  # Create a resizable window

    # Get the screen width and height
    screen_width = size[0]
    screen_height = size[1]

    # Resize the window to fit the screen
    cv.resizeWindow('Keypoints', min(screen_width, 1920), min(screen_height, 1080))

    cv.imshow("Keypoints", image)

    
    while True:
        key = cv.waitKey(1) & 0xFF

        # Check if the 'ESC' key is pressed or the window is closed
        if key == 27 or cv.getWindowProperty('Keypoints', cv.WND_PROP_VISIBLE) < 1:
            break


    cv.destroyAllWindows()
    s.save(ident,saving_directory,image,measure=True)
    s.savefile(ident,distance_top,distance_right,distance_bottom,distance_left)
    




