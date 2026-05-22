import cv2

def show_image(img_path: str):
    image = cv2.imread(img_path)

    if image is None:
        print("Error in image load")
        return

    cv2.imshow("Vanilla Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_image("dataset/train/images/0001_png.rf.7a80e671adb728551c6c2e1e2254c797.jpg")