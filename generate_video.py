import os
import cv2
from tqdm import tqdm
from glob import glob

directory = "original/Campus_CCW_Clear_Day_002"
start_idx = 8004
end_idx = 9004

left_images = sorted(glob(f"{directory}/Left/*.png"))
right_images = sorted(glob(f"{directory}/Right/*.png"))

output_dir = directory.split("/")[-1]
os.makedirs(output_dir, exist_ok=True)

out_left = cv2.VideoWriter(f"{output_dir}/left.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20, (1280, 720))
out_right = cv2.VideoWriter(f"{output_dir}/right.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20, (1280, 720))

for i in tqdm(range(start_idx, end_idx)):
    left = cv2.imread(left_images[i])
    right = cv2.imread(right_images[i])

    out_left.write(left)
    out_right.write(right)


