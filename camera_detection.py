import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import os
import cv2
import pyrealsense2 as rs
import numpy as np
from yolo import YOLO
from PIL import Image

if __name__ == "__main__":
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    # Start streaming
    pipeline.start(config)
    num = 0
    yolo = YOLO()
    try:
        while True:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            rgb_image = np.asanyarray(color_frame.get_data())
            image = Image.fromarray(cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB))
            rgb_img = yolo.detect_image(image)
            img = cv2.cvtColor(np.asarray(rgb_img), cv2.COLOR_RGB2BGR)
            cv2.imshow('my webcam', img)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('s'):   # Press 's' to save the image
                num += 1
                cv2.imwrite(str(num) + '.png', img)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
    finally:
        # Stop streaming
        pipeline.stop()
