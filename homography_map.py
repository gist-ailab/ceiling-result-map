import cv2
import numpy as np
 
if __name__ == '__main__' :

    data_root = ""


    # = GT
    # Read source image.
    im_src = cv2.imread('RGB.jpg')
    # input with click or stored list
    # Four corners of the book in source image
    pts_src = np.array([
        [141, 131],
        [480, 159],
        [493, 630],
        [ 64, 601],
    ])
    for pts_idx in pts_src:
        im_src_vis = cv2.circle(im_src, pts_idx, 3, (0, 0, 255), 1)
    
    # = Dest box
    # Read destination image.
    im_dst = cv2.imread('GT.png')    # : static square

    # Four corners of the book in destination image.
    pts_dst = np.array([
        [318, 256],
        [534, 372],
        [316, 670],
        [ 73, 473],
    ])
 
    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
 
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
 
    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)

    temp_value = 0