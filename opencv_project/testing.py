import cv2

image_path = 'assets/uploads/Bulldog-1.jpg'
img = cv2.imread(image_path, 0)  # 0 => grayscale

if img is None:
    print("Image not loaded correctly")
else:
    # Resize the image
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # Rotate the image 90 degrees clockwise
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imwrite('new_file.jpg', img)  # create a new file with current img

    # Display the image
    cv2.imshow('Image', img)
    cv2.waitKey(0)  # wait for infinite time until a key is pressed
    cv2.destroyAllWindows()
