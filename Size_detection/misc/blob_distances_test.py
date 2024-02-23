import cv2 as cv
import numpy as np

# Read image
image1 = cv.imread("images/test2.jpg")
im = cv.cvtColor(image1, cv.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector_create()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv.drawKeypoints(im, keypoints, np.array([]), (255, 255, 255, 0.8), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Known parameters

calibration_factor = 0.121

# Adjust pixels_to_cm with the calibration factor
pixels_to_cm = calibration_factor
#pixels_to_cm = 0.1  # Adjust this value based on your actual conversion factor
camera_distance_cm = 102.5  # Distance from the camera to the objects
focal_length_mm = 26  # Focal length of the camera in millimeters
sensor_size_inches = 1/1.72  # Sensor size in inches

# Convert the sensor size to inches
sensor_size_mm = sensor_size_inches / 0.0393701  # Convert inches to millimeters

# Calculate the conversion factor from focal length and sensor size to pixels
focal_length_pixels = (focal_length_mm * im.shape[1]) / (sensor_size_mm * 10)  # Convert mm to cm

# Calculate distances between blobs in centimeters
for i in range(len(keypoints)):
    for j in range(i+1, len(keypoints)):
        pt1 = keypoints[i].pt
        pt2 = keypoints[j].pt
        distance_pixels = np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

        # Use the formula to calculate distance in centimeters
        distance_cm = (focal_length_pixels * pixels_to_cm * camera_distance_cm) / distance_pixels
        print(f"Distance between blob {i+1} and blob {j+1}: {distance_cm:.2f} cm")

        # Display the distance on the image
        font = cv.FONT_HERSHEY_SIMPLEX
        text_position = ((int(pt1[0]) + int(pt2[0])) // 2, (int(pt1[1]) + int(pt2[1])) // 2)
        cv.putText(im_with_keypoints, f"{distance_cm:.2f} cm", text_position, font, 0.5, (255, 255, 255), 1, cv.LINE_AA)

        # Label blobs on the image
        cv.putText(im_with_keypoints, f"Blob {i+1}", (int(pt1[0]), int(pt1[1])), font, 0.5, (255, 255, 255), 1, cv.LINE_AA)
        cv.putText(im_with_keypoints, f"Blob {j+1}", (int(pt2[0]), int(pt2[1])), font, 0.5, (255, 255, 255), 1, cv.LINE_AA)

cv.namedWindow('Keypoints', cv.WINDOW_NORMAL)

# Show keypoints
cv.imshow("Keypoints", im_with_keypoints)

while True:
    key = cv.waitKey(1) & 0xFF

    # Check if the 'ESC' key is pressed or the window is closed
    if key == 27 or cv.getWindowProperty('Keypoints', cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()
