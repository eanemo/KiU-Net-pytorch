import cv2
import sys
import glob
from os.path import join

input_dir = sys.argv[0]
output_dir = sys.argv[1]

files = glob.glon("*.png")

for file in files:
    img = cv2.imread(join(input_dir, file))
    out_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out_img = cv2.resize(out_img, (128, 128))
    cv2.imwrite(join(output_dir, file), out_img)
    print("Writing ", join(output_dir, file))
