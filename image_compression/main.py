import cv2
from cv2 import imwrite

def image_compression(img_file):
    try:
        img = cv2.imread(img_file)
        imwrite("compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])
        print("image compressed...")
    except Exception as error:
        print('Error:',error)

if __name__ == "__main__":
    image_file = input("Enter Image i.e, mypic.jpg ")
    if image_file:
        image_compression(image_file)