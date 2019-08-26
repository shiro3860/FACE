import argparse
from pathlib import Path
from tqdm import tqdm
import numpy as np
import scipy.io
import cv2


def get_args():
    parser = argparse.ArgumentParser(description="This script creates asian dataset  from the UTKFace dataset.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input", "-i", type=str, required=True,
                        help="path to the UTKFace image directory")
    parser.add_argument("--output", "-o", type=str, default="asian",
                        help="path to output database asian file")
    parser.add_argument("--img_size", type=int, default=64,
                        help="output image size")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    image_dir = Path(args.input)
    output_path = args.output
    img_size = args.img_size

    for i, image_path in enumerate(tqdm(image_dir.glob("*.jpg"))):
        image_name = image_path.name  # [age]_[gender]_[race]_[date&time].jpg
        
        asian = image_name.split("_")[2] 
        if(int(asian)==2):
            img = cv2.imread(str(image_path))
            cv2.imwrite(output_path+'/{}'.format(image_name),img)

       
        
if __name__ == '__main__':
    main()