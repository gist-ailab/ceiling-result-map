
import cv2
import numpy as np


# ----


def mouse_click(event, x, y, flags, param):
    global im_src, canvas_img, pts_src

    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(canvas_img, (x, y), 3, (0, 0, 255), 1)
        cv2.imshow("Image", canvas_img)
        pts_src.append((x, y))
    elif event == cv2.EVENT_FLAG_RBUTTON:
        canvas_img = im_src.copy()
        pts_src = []


# ----


if __name__ == '__main__' :

    data_root = ""


    # = GT
    # Read source image.
    im_src = cv2.imread('./img/156_ov.png')

    canvas_img = im_src.copy()
    cv2.imshow("Image", canvas_img)
    key = cv2.waitKey(1)
    key = None
    # key = cv2.waitKey(1)

    cv2.setMouseCallback("Image", mouse_click)
    # input with click or stored list
    # Four corners of the book in source image
    pts_src = []

    while True:
        key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("./result/pts_img.png", canvas_img)
            print(np.array(pts_src))
        else:
            pass
    
    cv2.destroyAllWindows()

    temp_value = 0

    pts_src = np.array([
        (166,   4),
        (144, 140),
        (136, 199),
        (124, 204),
        (111, 203),
        ( 96, 142),
        ( 85,   6),
        (127,   9),
        (124, 146),
    ])