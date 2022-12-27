import os

import cv2
import numpy as np
 
if __name__ == '__main__' :

    for i in range(6):

        data_root = f"../../../_data/lg-ceiling/_result/LG-CEILING/"
        image_root = os.path.join(data_root, f"image_{i+1}")
        mask_root = os.path.join(data_root, f"mask_{i+1}")
        
        os.makedirs(os.path.join(data_root, f'result_{i+1}/im_dst'), exist_ok=True)
        os.makedirs(os.path.join(data_root, f'result_{i+1}/im_src'), exist_ok=True)
        os.makedirs(os.path.join(data_root, f'result_{i+1}/im_out'), exist_ok=True)
        os.makedirs(os.path.join(data_root, f'result_{i+1}/im_out_mask'), exist_ok=True)

        # for n in range(2401):
        for n in range(550):
            try:
                # = GT
                # Read source image.
                # im_src = cv2.imread(f'{image_root}/{n:05d}.png')
                im_src = cv2.imread(f'{image_root}/{n:05d}.jpg')
                resized_im_src = cv2.resize(im_src.copy(), (240,320))
                im_src_vis = resized_im_src.copy()
                im_src2 = cv2.imread(f'{mask_root}/{n:05d}.png')
                resized_im_src2 = cv2.resize(im_src2.copy(), (240,320), cv2.INTER_NEAREST)
                im_src_vis2 = resized_im_src2.copy()*255
                # input with click or stored list
                # Four corners of the book in source image
                # # pts_src = np.array([
                # #     [ 85,   6], # 1
                # #     [127,   9], # 2
                # #     [166,   4], # 3

                # #     [ 96, 142], # 4
                # #     [124, 146], # 5
                # #     [144, 140], # 6
                    
                # #     [111, 203], # 7
                # #     [124, 204], # 8
                # #     [136, 199], # 9
                # # ])
                # pts_src = np.array([
                #     [ 80,   6], # 1
                #     [120,   6], # 2
                #     [166,   6], # 3

                #     [ 96, 142], # 4
                #     [120, 142], # 5
                #     [144, 142], # 6

                #     [106, 200], # 7
                #     [120, 200], # 8
                #     [134, 200], # 9
                # ])
                pts_src = np.array([
                    [ 50,  25],
                    [120,  25],
                    [190,  25],

                    [ 70,  95],
                    [120,  95],
                    [170,  95],

                    [ 85, 143],
                    [120, 143],
                    [155, 143],
                ])
                for x, y in pts_src:
                    im_src_vis = cv2.circle(im_src_vis, (x, y), 3, (0, 0, 255), 1)
                    # im_src_vis2 = cv2.circle(im_src_vis2, (x, y), 3, (0, 0, 255), 1)
                
                # = Dest box
                # Read destination image.
                # im_dst = cv2.imread('./gt/GT.png')    # : static square
                im_dst = np.ones((320, 240, 3))*255

                # Four corners of the book in destination image.
                # pts_dst = np.array([
                #     [ 60,  12], # 1
                #     [120,  12], # 2
                #     [180,  12], # 3

                #     [ 60, 112], # 4
                #     [120, 112], # 5
                #     [180, 112], # 6

                #     [ 60, 212], # 7
                #     [120, 212], # 8
                #     [180, 212], # 9
                # ])
                pts_dst = np.array([
                    [ 60,   5],
                    [120,   5],
                    [180,   5],
                    [ 60,  60],
                    [120,  60],
                    [180,  60],
                    [ 60, 125],
                    [120, 125],
                    [180, 125],
                ])
            
                # Calculate Homography
                h, status = cv2.findHomography(pts_src, pts_dst)
            
                # Warp source image to destination based on homography
                im_out = cv2.warpPerspective(im_src_vis, h, (im_dst.shape[1], im_dst.shape[0]))
                im_out2 = cv2.warpPerspective(im_src_vis2, h, (im_dst.shape[1], im_dst.shape[0]))
            
                # Display images
                cv2.imshow("Source Image", im_src_vis)
                cv2.imshow("Destination Image", im_dst)
                cv2.imshow("Warped Source Image", im_out)
                cv2.imshow("Warped Source Image2", im_out2)
            
                cv2.waitKey(1)

                if n == 0:
                    cv2.imwrite(os.path.join(data_root, f'result_{i+1}/im_dst/{n:05d}.png'), im_dst)

                cv2.imwrite(os.path.join(data_root, f'result_{i+1}/im_src/{n:05d}.png'), im_src_vis)
                cv2.imwrite(os.path.join(data_root, f'result_{i+1}/im_out/{n:05d}.png'), im_out)
                cv2.imwrite(os.path.join(data_root, f'result_{i+1}/im_out_mask/{n:05d}.png'), im_out2)
                # cv2.imwrite(f"./result/im_dst/{0+n}_dst.png", canvas_img)
            except:
                print(f"pass ... dataset {i} - {n:05d}")
            temp_value = 0

        temp_value = 0

    temp_value = 0