import cv2 as cv 
import numpy as np 



if __name__ == '__main__':

    image1 = cv.imread('images/test2.jpg')

    gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    edges = cv.Canny(blurred, 50, 150)
    contours, _ = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    # Iterate through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv.contourArea(contour)

        # If the area is larger than a certain threshold (to filter out small contours)
        if area > 100:
            # Draw the contour on the original image1
            cv.drawContours(image1, [contour], -1, (0, 255, 0), 2)

            # Get the bounding box of the contour
            x, y, w, h = cv.boundingRect(contour)

            # Draw a rectangle around the object
            cv.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Print the dimensions of the object
            print(f"Width: {w}, Height: {h}")


    cv.namedWindow('Measured Objects', cv.WINDOW_NORMAL)           

    # Display the result
    cv.imshow('Measured Objects', image1)
    #cv.waitKey(0)

    while True:
        key = cv.waitKey(1) & 0xFF

        # Check if the 'ESC' key is pressed or the window is closed
        if key == 27 or cv.getWindowProperty('Measured Objects', cv.WND_PROP_VISIBLE) < 1:
            break


    cv.destroyAllWindows()
