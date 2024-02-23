import cv2
import numpy as np
import math
import pyautogui

def draw_ruler(image, length_cm, pixels_per_cm, ruler_position_x, ruler_position_y, rotation_angle):
    # Calculate pixel length
    length_pixels = int(length_cm * pixels_per_cm*1.5)

    # Create a black image with an alpha channel
    ruler_image = np.zeros((100, length_pixels, 4), dtype=np.uint8)

    # Draw the ruler lines and set alpha channel values
    for i in range(length_pixels):
        if i % pixels_per_cm == 0:
            cv2.line(ruler_image, (i, 20), (i, 80), (255, 255, 255, 255), 2)
        elif i % (pixels_per_cm // 2) == 0:
            cv2.line(ruler_image, (i, 40), (i, 60), (255, 255, 255, 255), 1)

    # Add text indicating length
    cv2.putText(ruler_image, f'{length_cm} cm', (10, 95), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), 2)

    # Rotate the ruler image
    center = (length_pixels // 2, 50)
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1)
    ruler_image = cv2.warpAffine(ruler_image, rotation_matrix, (length_pixels, 100))

    # Extract alpha channel
    alpha_channel = ruler_image[:, :, 3]

    # Add ruler to the original image at the specified position with transparency
    image[ruler_position_y:ruler_position_y + 100, ruler_position_x:ruler_position_x + length_pixels, :] = (
        image[ruler_position_y:ruler_position_y + 100, ruler_position_x:ruler_position_x + length_pixels, :] *
        (1 - alpha_channel[:, :, None] / 255) +
        ruler_image[:, :, :3] * (alpha_channel[:, :, None] / 255)
    )

    return image




def mouse_callback(event, x, y, flags, param):
    global ruler_position_x, ruler_position_y, dragging, rotation_angle

    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the mouse click is within the ruler region
        if ruler_position_x <= x <= ruler_position_x + length_pixels and ruler_position_y <= y <= ruler_position_y + 100:
            dragging = True
            offset_x = x - ruler_position_x
            offset_y = y - ruler_position_y
            param['offset'] = (offset_x, offset_y)
        else:
            dragging = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            ruler_position_x = x - param['offset'][0]
            ruler_position_y = y - param['offset'][1]
            update_image()

    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False


def key_callback(key):
    global rotation_angle
    if key ==81:
        rotation_angle += 0.5 # Rotate clockwise by 0.5 degrees
    elif key == 83:
        rotation_angle -= 0.5 # Rotate counterclockwise by 0.5 degrees

    elif key == ord('a'):
        rotation_angle += 2

    elif key == ord('d'):
        rotation_angle -= 2   


    elif key == ord('l'):
        rotation_angle += 5

    elif key == ord('k'):
        rotation_angle -= 5


    update_image()

def update_image():
    global example_image, ruler_length_cm, pixels_per_cm, ruler_position_x, ruler_position_y, length_pixels, rotation_angle

    # Check if the ruler is out of bounds on the x-axis
    if ruler_position_x < 0:
        ruler_position_x = 0
    elif ruler_position_x + length_pixels > example_image.shape[1]:
        ruler_position_x = example_image.shape[1] - length_pixels

    # Check if the ruler is out of bounds on the y-axis
    if ruler_position_y < 0:
        ruler_position_y = 0
    elif ruler_position_y + 100 > example_image.shape[0]:
        ruler_position_y = example_image.shape[0] - 100

    # Draw the virtual ruler on the image at the specified position and rotation angle
    result_image = draw_ruler(example_image.copy(), ruler_length_cm, pixels_per_cm, ruler_position_x, ruler_position_y, rotation_angle)
 

    # Display the result
    cv2.namedWindow('Virtual Ruler', cv2.WINDOW_NORMAL)  # Create a resizable window



    cv2.imshow('Virtual Ruler', result_image)


# Load an example image
example_image = cv2.imread('images/testing.png')




# Set the length of the virtual ruler in centimeters
ruler_length_cm = 50

# Set the number of pixels per centimeter
pixels_per_cm = 10  # You can adjust this value based on your image resolution

# Set the initial position where you want to place the ruler (in pixels)
ruler_position_x = 100
ruler_position_y = 50  # Adjust the initial y-axis position as needed
length_pixels = int(ruler_length_cm * pixels_per_cm)

# Set the initial rotation angle
rotation_angle = 0

# Initialize dragging variable
dragging = False

# Draw the virtual ruler on the image at the specified position and rotation angle
update_image()




# Set up mouse callback
cv2.setMouseCallback('Virtual Ruler', mouse_callback, {'offset': (0, 0)})

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break
    key_callback(key)

cv2.destroyAllWindows()
