# import skimage
# import os
# from skimage import io
# import matplotlib.pyplot as plt
# # Reading image file
# image2 = io.imread('C:\\Users\\amirkhan\\Desktop\\gla.jpg')
#
# # Setting dimensions boundaries
# x = 189 // 2
# y = 267 // 2
# r = 189 // 6
#
# # Iterating to all the pixels in the set boundaries
# for i in range(0, 189):
#     for j in range(0, 267):
#         if i in range(0, 189 // 3):
#             image2[i][j] = [255, 128, 64]  # Orange Color
#         elif i in range(189 // 3, 189 * 2 // 3):
#             image2[i][j] = [255, 255, 255]  # White Color
#         else:
#             image2[i][j] = [0, 128, 0]  # Green Color
#
#             # Equation for 2px thick ring
#         if ((pow((x - i), 2) + pow((y - j), 2)) <= pow(r + 1, 2)) and (
#                 (pow((x - i), 2) + pow((y - j), 2)) >= pow(r - 2, 2)):
#             image2[i][j] = [0, 0, 255]  # Blue Color
#
# # Iterating within the ring
# for i in range(189 // 3, 189 * 2 // 3):
#     for j in range(267 // 3, 267 * 2 // 3):
#
#         # Equation to draw 4 straight lines
#         if ((i == 189 // 2) or (j == 267 // 2) or (i + 39 == j or (i + 39 + j == 266))) and (
#                 (pow((x - i), 2) + pow((y - j), 2)) <= pow(r, 2)):
#             image2[i][j] = [0, 0, 255]  # Blue Color
#
# io.imshow(image2)  # Output
# plt.imshow(image2)
# plt.show()
#

# Indian Flag
import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

# Plotting the tri colours in flag
a = patch.Rectangle((0, 1), width=12, height=2, facecolor='green', edgecolor='grey')
b = patch.Rectangle((0, 3), width=12, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0, 5), width=12, height=2, facecolor='#FF9933', edgecolor='grey')
m, n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

#  Circle
radius = 0.8
py.plot(6, 4, marker='o', markerfacecolor='#000088ff', markersize=9.5)
chakra = py.Circle((6, 4), radius, color='#000088ff', fill=False, linewidth=7)
n.add_artist(chakra)

# 24 spokes
for i in range(0, 24):
    p = 6 + radius / 2 * np.cos(np.pi * i / 12 + np.pi / 48)
    q = 6 + radius / 2 * np.cos(np.pi * i / 12 - np.pi / 48)
    r = 4 + radius / 2 * np.sin(np.pi * i / 12 + np.pi / 48)
    s = 4 + radius / 2 * np.sin(np.pi * i / 12 - np.pi / 48)
    t = 6 + radius * np.cos(np.pi * i / 12)
    u = 4 + radius * np.sin(np.pi * i / 12)
    n.add_patch(patch.Polygon([[6, 4], [p, r], [t, u], [q, s]], fill=True, closed=True, color='#000088ff'))
py.axis('equal')
py.show()

