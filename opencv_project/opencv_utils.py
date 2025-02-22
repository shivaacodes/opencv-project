# A separate file for OpenCV-related logic to keep app.py clean and modular.

import cv2
import numpy as np


def process_image(file):
    # Read the uploaded image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Example processing: Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Save or return the result (e.g., as a file path or base64 string)
    cv2.imwrite('static/uploads/processed_image.jpg', gray_img)
    return '/static/uploads/processed_image.jpg'
