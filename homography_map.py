import cv2
import numpy as np
 
if __name__ == '__main__' :

    data_root = ""

    for n in range(10):
        # = GT
        # Read source image.
        im_src = cv2.imread(f'./img/{114+n}_ov.png')
        # input with click or stored list
        # Four corners of the book in source image
        # pts_src = np.array([
        #     [ 85,   6], # 1
        #     [127,   9], # 2
        #     [166,   4], # 3

        #     [ 96, 142], # 4
        #     [124, 146], # 5
        #     [144, 140], # 6
            
        #     [111, 203], # 7
        #     [124, 204], # 8
        #     [136, 199], # 9
        # ])
        pts_src = np.array([
            [ 80,   6], # 1
            [120,   6], # 2
            [166,   6], # 3

            [ 96, 142], # 4
            [120, 142], # 5
            [144, 142], # 6

            [106, 200], # 7
            [120, 200], # 8
            [134, 200], # 9
        ])
        for x, y in pts_src:
            im_src_vis = cv2.circle(im_src, (x, y), 3, (0, 0, 255), 1)
        
        # = Dest box
        # Read destination image.
        # im_dst = cv2.imread('./gt/GT.png')    # : static square
        im_dst = np.ones((320, 240, 3))*255

        # Four corners of the book in destination image.
        pts_dst = np.array([
            [ 60,  12], # 1
            [120,  12], # 2
            [180,  12], # 3

            [ 60, 112], # 4
            [120, 112], # 5
            [180, 112], # 6

            [ 60, 212], # 7
            [120, 212], # 8
            [180, 212], # 9
        ])
    
        # Calculate Homography
        h, status = cv2.findHomography(pts_src, pts_dst)
    
        # Warp source image to destination based on homography
        im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))
    
        # Display images
        cv2.imshow("Source Image", im_src)
        cv2.imshow("Destination Image", im_dst)
        cv2.imshow("Warped Source Image", im_out)
    
        cv2.waitKey(1)

        temp_value = 0

    temp_value = 0