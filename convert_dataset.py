import cv2
import sys
import glob
import os
from os.path import join

input_dir = sys.argv[1]
output_dir = sys.argv[2]

files = glob.glon("*.png")

for file in files:
    img = cv2.imread(join(input_dir, file))
    out_img = cv2.resize(img, (128, 128))
    out_img = cv2.cvtColor(out_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(join(output_dir, file), out_img[:, :, 1])
    print("Writing ", join(output_dir, file))
