import cv2

img = cv2.imread('images/test2.jpg')

# Convert image to HSV color space for better color representation
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for orange color in HSV
lower_orange = (5, 100, 100)
upper_orange = (15, 255, 255)

# Create a mask using the inRange function to extract orange regions
orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Apply median blur to the mask to reduce noise
blur = cv2.medianBlur(orange_mask, 5)

# Find contours in the masked image
cnts = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 1
orange_dots = []

for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area:
        cv2.drawContours(img, [c], -1, (36, 255, 12), 2)
        orange_dots.append(c)

print("Orange Dots Count is:", len(orange_dots))

cv2.namedWindow('Measured Objects', cv2.WINDOW_NORMAL)           

cv2.imshow('Output image:', img)
cv2.waitKey()
