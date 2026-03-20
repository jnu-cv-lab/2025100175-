import cv2
import numpy as np
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, 'test.jpg')
output_dir = os.path.join(current_dir, 'output')


if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Output directory created: {output_dir}")


if os.path.exists(img_path):
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is not None:
        print("Image loaded successfully.")

        
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_save_path = os.path.join(output_dir, 'gray_test.jpg')
        cv2.imwrite(gray_save_path, gray_img)
        print(f"Grayscale image saved: {gray_save_path}")

        
        crop_img = gray_img[0:200, 0:200]
        crop_img[180:190, 180:190] = 255
        crop_save_path = os.path.join(output_dir, 'crop_test.jpg')
        cv2.imwrite(crop_save_path, crop_img)
        print(f"Cropped image saved: {crop_save_path}")

      
        cv2.imshow('Original', img)
        cv2.imshow('Gray Result', gray_img)
        cv2.imshow('Cropped Result', crop_img)
        print("Press any key to exit...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to decode image.")
else:
    print("test.jpg not found.")