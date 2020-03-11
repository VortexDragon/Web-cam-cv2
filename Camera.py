import cv2

def Cam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        img = cv2.flip(img, 1)
        cv2.imshow(None, img)
        if cv2.waitKey(1) == 27: #Break loop with Esc
            break
    cv2.destroyAllWindows()

def main():
    Cam()

if __name__ == "__main__":
    main()