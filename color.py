from pyk4a import PyK4A

# Load camera with the default config
pyk4a = PyK4A()

pyk4a.start()
capture = pyk4a.get_capture()
color=capture.color

from matplotlib import pyplot as plt
plt.figure(figsize=(5,5))
plt.imshow(color)
plt.show()