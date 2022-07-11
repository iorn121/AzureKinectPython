from pyk4a import PyK4A
import numpy as np

# Load camera with the default config
pyk4a = PyK4A()

pyk4a.start()
pyk4a.whitebalance=6000

capture = pyk4a.get_capture()
depth=capture.depth
from matplotlib import pyplot as plt
plt.figure(figsize=(6,6))
plt.title("my room depth")
plt.imshow(depth)
plt.savefig("./image/depth.png",cmap="gray")

import cv2
print(type(depth),depth.shape)
print(np.amax(depth),np.amin(depth))