import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

xyz_coordinates = [[11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11], [11, 1, 12], [11, 1, 13], [11, 1, 14], [11, 1, 15], [11, 1, 16], [11, 1, 17], [11, 1, 18], [11, 1, 19], [11, 1, 20], [11, 1, 21], [10, 1, 1], [10, 1, 2], [10, 1, 3], [10, 1, 4], [10, 1, 5], [10, 1, 6], [10, 1, 7], [10, 1, 8], [10, 1, 9], [10, 1, 10], [10, 1, 11], [10, 1, 12], [10, 1, 13], [10, 1, 14], [10, 1, 15], [10, 1, 16], [10, 1, 17], [10, 1, 18], [10, 1, 19], [10, 1, 20], [10, 1, 21], [9, 1, 1], [9, 1, 2], [9, 1, 3], [9, 1, 4], [9, 1, 5], [9, 1, 6], [9, 1, 7], [9, 1, 8], [9, 1, 9], [9, 1, 10], [9, 1, 11], [9, 1, 12], [9, 1, 13], [9, 1, 14], [9, 1, 15], [9, 1, 16], [9, 1, 17], [9, 1, 18], [9, 1, 19], [9, 1, 20], [9, 1, 21], [8, 1, 1], [8, 1, 2], [8, 1, 3], [8, 1, 4], [8, 1, 5], [8, 1, 6], [8, 1, 7], [8, 1, 8], [8, 1, 9], [8, 1, 10], [8, 1, 11], [8, 1, 12], [8, 1, 13], [8, 1, 14], [8, 1, 15], [8, 1, 16], [8, 1, 17], [8, 1, 18], [8, 1, 19], [8, 1, 20], [8, 1, 21], [7, 1, 1], [7, 1, 2], [7, 1, 3], [7, 1, 4], [7, 1, 5], [7, 1, 6], [7, 1, 7], [7, 1, 8], [7, 1, 9], [7, 1, 10], [7, 1, 11], [7, 1, 12], [7, 1, 13], [7, 1, 14], [7, 1, 15], [7, 1, 16], [7, 1, 17], [7, 1, 18], [7, 1, 19], [7, 1, 20], [7, 1, 21], [6, 1, 1], [6, 1, 2], [6, 1, 3], [6, 1, 4], [6, 1, 5], [6, 1, 6], [6, 1, 7], [6, 1, 8], [6, 1, 9], [6, 1, 10], [6, 1, 11], [6, 1, 12], [6, 1, 13], [6, 1, 14], [6, 1, 15], [6, 1, 16], [6, 1, 17], [6, 1, 18], [6, 1, 19], [6, 1, 20], [6, 1, 21], [5, 1, 1], [5, 1, 2], [5, 1, 3], [5, 1, 4], [5, 1, 5], [5, 1, 6], [5, 1, 7], [5, 1, 8], [5, 1, 9], [5, 1, 10], [5, 1, 11], [5, 1, 12], [5, 1, 13], [5, 1, 14], [5, 1, 15], [5, 1, 16], [5, 1, 17], [5, 1, 18], [5, 1, 19], [5, 1, 20], [5, 1, 21], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 1, 4], [4, 1, 5], [4, 1, 6], [4, 1, 7], [4, 1, 8], [4, 1, 9], [4, 1, 10], [4, 1, 11], [4, 1, 12], [4, 1, 13], [4, 1, 14], [4, 1, 15], [4, 1, 16], [4, 1, 17], [4, 1, 18], [4, 1, 19], [4, 1, 20], [4, 1, 21], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 1, 4], [3, 1, 5], [3, 1, 6], [3, 1, 7], [3, 1, 8], [3, 1, 9], [3, 1, 10], [3, 1, 11], [3, 1, 12], [3, 1, 13], [3, 1, 14], [3, 1, 15], [3, 1, 16], [3, 1, 17], [3, 1, 18], [3, 1, 19], [3, 1, 20], [3, 1, 21], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 1, 5], [2, 1, 6], [2, 1, 7], [2, 1, 8], [2, 1, 9], [2, 1, 10], [2, 1, 11], [2, 1, 12], [2, 1, 13], [2, 1, 15], [2, 1, 16], [2, 1, 17], [2, 1, 18], [2, 1, 19], [2, 1, 20], [2, 1, 21], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 1, 6], [1, 1, 7], [1, 1, 8], [1, 1, 
9], [1, 1, 10], [1, 1, 11], [1, 1, 12], [1, 1, 13], [1, 1, 14], [1, 1, 15], [1, 1, 16], [1, 1, 17], [1, 1, 18], [1, 1, 19], [1, 1, 20], [1, 1, 21], [11, 2, 6], [11, 2, 7], [11, 2, 8], [11, 2, 9], [11, 2, 10], [11, 2, 11], [11, 2, 12], [11, 2, 13], [11, 2, 14], [11, 2, 15], [11, 2, 16], [10, 2, 6], [10, 2, 7], [10, 2, 8], [10, 2, 9], [10, 2, 10], [10, 2, 11], [10, 2, 12], [10, 2, 13], [10, 2, 14], [10, 2, 15], [10, 2, 16], 
[9, 2, 6], [9, 2, 7], [9, 2, 8], [9, 2, 9], [9, 2, 10], [9, 2, 13], [9, 2, 14], [9, 2, 15], [9, 2, 16], [8, 2, 6], [8, 2, 7], [8, 2, 8], [8, 2, 9], [8, 2, 10], [8, 2, 13], [8, 2, 14], [8, 2, 15], [8, 2, 16], [7, 2, 6], [7, 2, 7], [7, 2, 8], [7, 2, 9], [7, 2, 10], [7, 2, 13], [7, 2, 14], [7, 2, 15], [7, 2, 16], [6, 2, 15], [6, 2, 16], [5, 2, 6], [5, 2, 7], [5, 2, 8], [5, 2, 9], [5, 2, 10], [5, 2, 13], [5, 2, 14], [5, 2, 15], [5, 2, 16], [4, 2, 6], [4, 2, 7], [4, 2, 13], [4, 2, 14], [4, 2, 15], [4, 2, 16], [3, 2, 6], [3, 2, 7], [3, 2, 8], [3, 2, 9], [3, 2, 10], [3, 2, 13], [3, 2, 14], [3, 2, 15], [3, 2, 16], [2, 2, 6], [2, 2, 7], [2, 2, 8], [2, 2, 9], [2, 2, 10], [2, 2, 11], [2, 2, 12], [2, 2, 13], [2, 
2, 14], [2, 2, 15], [2, 2, 16], [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 2, 10], [1, 2, 11], [1, 2, 12], [1, 2, 13], [1, 2, 14], [1, 2, 15], [1, 2, 16], [11, 3, 7], [11, 3, 10], [11, 3, 11], [11, 3, 12], [11, 3, 15], [10, 3, 6], [10, 3, 7], [10, 3, 8], [10, 3, 9], [10, 3, 10], [10, 3, 11], [10, 3, 12], [10, 3, 13], [10, 3, 14], [10, 3, 15], [10, 3, 16], [9, 3, 7], [9, 3, 8], [9, 3, 9], [9, 3, 10], [9, 3, 15], [8, 3, 7], [8, 3, 8], [8, 3, 9], [8, 3, 13], [8, 3, 15], [7, 3, 6], [7, 3, 7], [7, 3, 8], [7, 3, 13], [7, 3, 15], [7, 3, 16], [6, 3, 15], [6, 3, 16], [5, 3, 6], [5, 3, 7], [5, 3, 13], [5, 3, 15], [5, 3, 16], [4, 3, 7], [4, 3, 13], [4, 3, 15], [3, 3, 7], [3, 3, 15], [2, 3, 6], [2, 3, 7], [2, 3, 8], [2, 3, 9], [2, 3, 10], [2, 3, 11], [2, 3, 12], [2, 3, 13], [2, 3, 14], [2, 3, 15], [2, 3, 16], [1, 3, 7], [1, 3, 10], [1, 3, 11], [1, 3, 12], [1, 3, 15], [11, 4, 7], [11, 4, 10], [11, 4, 12], [11, 4, 15], [10, 4, 6], [10, 4, 7], [10, 4, 8], [10, 4, 9], [10, 4, 10], [10, 4, 11], [10, 4, 12], [10, 4, 13], [10, 4, 14], [10, 4, 15], [10, 4, 16], [9, 4, 7], [9, 4, 8], [9, 4, 9], [9, 4, 10], [9, 4, 12], [9, 4, 13], [9, 
4, 14], [9, 4, 15], [8, 4, 7], [8, 4, 9], [8, 4, 14], [8, 4, 15], [7, 4, 6], [7, 4, 7], [7, 4, 14], [7, 4, 15], [7, 4, 16], [6, 4, 7], [6, 4, 
8], [6, 4, 15], [5, 4, 6], [5, 4, 7], [5, 4, 8], [5, 4, 14], [5, 4, 15], [5, 4, 16], [4, 4, 7], [4, 4, 8], [4, 4, 14], [4, 4, 15], [3, 4, 7], 
[3, 4, 8], [3, 4, 9], [3, 4, 10], [3, 4, 12], [3, 4, 13], [3, 4, 14], [3, 4, 15], [2, 4, 6], [2, 4, 7], [2, 4, 8], [2, 4, 9], [2, 4, 10], [2, 
4, 11], [2, 4, 12], [2, 4, 13], [2, 4, 14], [2, 4, 15], [2, 4, 16], [1, 4, 7], [1, 4, 10], [1, 4, 12], [1, 4, 15], [11, 5, 6], [11, 5, 7], [11, 5, 8], [11, 5, 9], [11, 5, 10], [11, 5, 11], [11, 5, 12], [11, 5, 13], [11, 5, 14], [11, 5, 15], [11, 5, 16], [10, 5, 6], [10, 5, 7], [10, 5, 8], [10, 5, 9], [10, 5, 10], [10, 5, 11], [10, 5, 12], [10, 5, 13], [10, 5, 14], [10, 5, 15], [10, 5, 16], [9, 5, 6], [9, 5, 7], [9, 5, 10], [9, 5, 11], [9, 5, 12], [9, 5, 13], [9, 5, 14], [9, 5, 15], [9, 5, 16], [8, 5, 6], [8, 5, 7], [8, 5, 9], [8, 5, 10], [8, 5, 11], [8, 5, 12], 
[8, 5, 13], [8, 5, 14], [8, 5, 15], [8, 5, 16], [7, 5, 6], [7, 5, 7], [7, 5, 9], [7, 5, 10], [7, 5, 11], [7, 5, 12], [7, 5, 13], [7, 5, 14], [7, 5, 15], [7, 5, 16], [6, 5, 6], [6, 5, 7], [6, 5, 8], [6, 5, 9], [6, 5, 10], [6, 5, 11], [6, 5, 12], [6, 5, 13], [6, 5, 14], [6, 5, 15], [6, 5, 16], [5, 5, 6], [5, 5, 7], [5, 5, 8], [5, 5, 9], [5, 5, 10], [5, 5, 11], [5, 5, 12], [5, 5, 13], [5, 5, 14], [5, 5, 15], [5, 5, 16], [4, 5, 6], [4, 5, 7], [4, 5, 8], [4, 5, 9], [4, 5, 10], [4, 5, 11], [4, 5, 12], [4, 5, 13], [4, 5, 14], [4, 5, 15], [4, 5, 16], [3, 5, 6], [3, 5, 7], [3, 5, 8], [3, 5, 9], [3, 5, 10], [3, 5, 11], [3, 5, 12], [3, 5, 13], [3, 5, 14], [3, 5, 15], [3, 5, 16], [2, 5, 6], [2, 5, 7], [2, 5, 8], 
[2, 5, 9], [2, 5, 10], [2, 5, 11], [2, 5, 12], [2, 5, 13], [2, 5, 14], [2, 5, 15], [2, 5, 16], [1, 5, 6], [1, 5, 7], [1, 5, 8], [1, 5, 9], [1, 5, 10], [1, 5, 11], [1, 5, 12], [1, 5, 13], [1, 5, 14], [1, 5, 15], [1, 5, 16], [11, 6, 6], [11, 6, 7], [11, 6, 8], [11, 6, 9], [11, 6, 10], 
[11, 6, 11], [11, 6, 12], [11, 6, 13], [11, 6, 14], [11, 6, 15], [11, 6, 16], [10, 6, 6], [10, 6, 7], [10, 6, 8], [10, 6, 9], [10, 6, 10], [10, 6, 11], [10, 6, 12], [10, 6, 13], [10, 6, 14], [10, 6, 15], [10, 6, 16], [9, 6, 6], [9, 6, 7], [9, 6, 11], [9, 6, 12], [9, 6, 13], [9, 6, 14], [9, 6, 15], [9, 6, 16], [8, 6, 6], [8, 6, 7], [8, 6, 12], [8, 6, 13], [8, 6, 14], [8, 6, 15], [8, 6, 16], [7, 6, 6], [7, 6, 7], [7, 6, 8], 
[7, 6, 14], [7, 6, 15], [7, 6, 16], [6, 6, 6], [6, 6, 7], [6, 6, 8], [6, 6, 10], [6, 6, 12], [6, 6, 13], [6, 6, 14], [6, 6, 15], [6, 6, 16], [5, 6, 6], [5, 6, 7], [5, 6, 8], [5, 6, 10], [5, 6, 15], [5, 6, 16], [4, 6, 6], [4, 6, 7], [4, 6, 8], [4, 6, 10], [4, 6, 12], [4, 6, 13], [4, 6, 14], [4, 6, 15], [4, 6, 16], [3, 6, 6], [3, 6, 7], [3, 6, 8], [3, 6, 9], [3, 6, 10], [3, 6, 11], [3, 6, 12], [3, 6, 13], [3, 6, 14], [3, 6, 
15], [3, 6, 16], [2, 6, 6], [2, 6, 7], [2, 6, 8], [2, 6, 9], [2, 6, 10], [2, 6, 11], [2, 6, 12], [2, 6, 13], [2, 6, 14], [2, 6, 15], [2, 6, 16], [1, 6, 6], [1, 6, 7], [1, 6, 8], [1, 6, 9], [1, 6, 10], [1, 6, 11], [1, 6, 12], [1, 6, 13], [1, 6, 14], [1, 6, 15], [1, 6, 16], [11, 7, 11], [10, 7, 6], [10, 7, 7], [10, 7, 8], [10, 7, 9], [10, 7, 10], [10, 7, 11], [10, 7, 12], [10, 7, 13], [10, 7, 14], [10, 7, 15], [10, 7, 16], [9, 7, 6], [9, 7, 7], [9, 7, 8], [9, 7, 11], [9, 7, 12], [9, 7, 13], [9, 7, 14], [9, 7, 15], [9, 7, 16], [8, 7, 6], [8, 7, 7], [8, 7, 12], [8, 
7, 13], [8, 7, 14], [8, 7, 15], [8, 7, 16], [7, 7, 7], [7, 7, 14], [7, 7, 15], [6, 7, 6], [6, 7, 7], [6, 7, 14], [6, 7, 15], [6, 7, 16], [5, 7, 7], [5, 7, 15], [4, 7, 6], [4, 7, 7], [4, 7, 8], [4, 7, 15], [4, 7, 16], [3, 7, 6], [3, 7, 7], [3, 7, 8], [3, 7, 9], [3, 7, 10], [3, 7, 11], [3, 7, 12], [3, 7, 13], [3, 7, 14], [3, 7, 15], [3, 7, 16], [2, 7, 6], [2, 7, 7], [2, 7, 8], [2, 7, 9], [2, 7, 10], [2, 7, 11], [2, 7, 12], [2, 7, 13], [2, 7, 14], [2, 7, 15], [2, 7, 16], [1, 7, 11], [9, 8, 6], [9, 8, 7], [9, 8, 8], [9, 8, 9], [9, 8, 10], [9, 8, 11], [9, 8, 12], [9, 8, 13], [9, 8, 14], [9, 8, 15], [9, 8, 16], [8, 8, 6], [8, 8, 7], [8, 8, 13], [8, 8, 14], [8, 8, 15], [8, 8, 16], [7, 8, 7], [7, 8, 15], [6, 
8, 6], [6, 8, 7], [6, 8, 15], [6, 8, 16], [5, 8, 7], [5, 8, 15], [4, 8, 6], [4, 8, 7], [4, 8, 15], [4, 8, 16], [3, 8, 6], [3, 8, 7], [3, 8, 8], [3, 8, 9], [3, 8, 10], [3, 8, 11], [3, 8, 12], [3, 8, 13], [3, 8, 14], [3, 8, 15], [3, 8, 16], [10, 9, 6], [10, 9, 7], [10, 9, 8], [10, 9, 9], [10, 9, 10], [10, 9, 11], [10, 9, 12], [10, 9, 13], [10, 9, 14], [10, 9, 15], [10, 9, 16], [9, 9, 5], [9, 9, 6], [9, 9, 7], [9, 9, 8], [9, 
9, 9], [9, 9, 10], [9, 9, 11], [9, 9, 12], [9, 9, 13], [9, 9, 14], [9, 9, 15], [9, 9, 16], [9, 9, 17], [8, 9, 6], [8, 9, 7], [8, 9, 8], [8, 9, 9], [8, 9, 10], [8, 9, 12], [8, 9, 13], [8, 9, 14], [8, 9, 15], [8, 9, 16], [7, 9, 6], [7, 9, 7], [7, 9, 8], [7, 9, 14], [7, 9, 15], [7, 9, 16], [6, 9, 6], [6, 9, 7], [6, 9, 15], [6, 9, 16], [5, 9, 6], [5, 9, 7], [5, 9, 8], [5, 9, 14], [5, 9, 15], [5, 9, 16], [4, 9, 6], [4, 9, 7], [4, 9, 8], [4, 9, 9], [4, 9, 10], [4, 9, 12], [4, 9, 13], [4, 9, 14], [4, 9, 15], [4, 9, 16], [3, 9, 5], [3, 9, 6], [3, 9, 7], [3, 9, 8], [3, 9, 9], [3, 9, 10], [3, 9, 11], [3, 9, 12], [3, 9, 13], [3, 9, 14], [3, 9, 15], [3, 9, 16], [3, 9, 17], [2, 9, 6], [2, 9, 7], [2, 9, 8], [2, 9, 
9], [2, 9, 10], [2, 9, 11], [2, 9, 12], [2, 9, 13], [2, 9, 14], [2, 9, 15], [2, 9, 16], [9, 10, 5], [9, 10, 6], [9, 10, 7], [9, 10, 8], [9, 10, 9], [9, 10, 10], [9, 10, 11], [9, 10, 12], [9, 10, 13], [9, 10, 14], [9, 10, 15], [9, 10, 16], [9, 10, 17], [8, 10, 5], [8, 10, 6], [8, 10, 
7], [8, 10, 8], [8, 10, 9], [8, 10, 10], [8, 10, 11], [8, 10, 12], [8, 10, 13], [8, 10, 14], [8, 10, 15], [8, 10, 16], [8, 10, 17], [7, 10, 6], [7, 10, 7], [7, 10, 8], [7, 10, 9], [7, 10, 10], [7, 10, 11], [7, 10, 12], [7, 10, 13], [7, 10, 14], [7, 10, 15], [7, 10, 16], [6, 10, 6], [6, 10, 7], [6, 10, 8], [6, 10, 9], [6, 10, 10], [6, 10, 11], [6, 10, 12], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 16], [5, 10, 6], [5, 
10, 7], [5, 10, 8], [5, 10, 9], [5, 10, 10], [5, 10, 11], [5, 10, 12], [5, 10, 13], [5, 10, 14], [5, 10, 15], [5, 10, 16], [4, 10, 5], [4, 10, 6], [4, 10, 7], [4, 10, 8], [4, 10, 9], [4, 10, 10], [4, 10, 11], [4, 10, 12], [4, 10, 13], [4, 10, 14], [4, 10, 15], [4, 10, 16], [4, 10, 17], [3, 10, 5], [3, 10, 6], [3, 10, 7], [3, 10, 8], [3, 10, 9], [3, 10, 10], [3, 10, 11], [3, 10, 12], [3, 10, 13], [3, 10, 14], [3, 10, 15], [3, 10, 16], [3, 10, 17], [9, 11, 5], [9, 11, 6], [9, 11, 7], [9, 11, 8], [9, 11, 9], [9, 11, 10], [9, 11, 11], [9, 11, 12], [9, 11, 13], [9, 11, 14], [9, 11, 15], [9, 11, 16], [9, 11, 17], [8, 11, 4], [8, 11, 5], [8, 11, 6], [8, 11, 7], [8, 11, 8], [8, 11, 9], [8, 11, 10], [8, 11, 11], [8, 11, 12], [8, 11, 13], [8, 11, 14], [8, 11, 15], [8, 11, 16], [8, 11, 17], [8, 11, 18], [7, 11, 5], [7, 11, 6], [7, 11, 7], [7, 11, 15], [7, 11, 16], [7, 11, 17], [6, 11, 6], [6, 11, 7], [6, 11, 15], [6, 11, 16], [5, 11, 5], [5, 11, 6], [5, 11, 7], [5, 11, 15], [5, 11, 16], [5, 11, 17], [4, 11, 4], [4, 11, 5], [4, 11, 6], [4, 11, 7], [4, 11, 8], [4, 11, 9], [4, 11, 10], [4, 11, 11], [4, 11, 12], [4, 11, 13], [4, 11, 
14], [4, 11, 15], [4, 11, 16], [4, 11, 17], [4, 11, 18], [3, 11, 5], [3, 11, 6], [3, 11, 7], [3, 11, 8], [3, 11, 9], [3, 11, 10], [3, 11, 11], [3, 11, 12], [3, 11, 13], [3, 11, 14], [3, 11, 15], [3, 11, 16], [3, 11, 17], [8, 12, 4], [8, 12, 5], [8, 12, 6], [8, 12, 7], [8, 12, 8], [8, 12, 9], [8, 12, 10], [8, 12, 11], [8, 12, 12], [8, 12, 13], [8, 12, 14], [8, 12, 15], [8, 12, 16], [8, 12, 17], [8, 12, 18], [7, 12, 4], [7, 
12, 5], [7, 12, 6], [7, 12, 7], [7, 12, 8], [7, 12, 9], [7, 12, 10], [7, 12, 11], [7, 12, 12], [7, 12, 13], [7, 12, 14], [7, 12, 15], [7, 12, 
16], [7, 12, 17], [7, 12, 18], [6, 12, 5], [6, 12, 6], [6, 12, 7], [6, 12, 15], [6, 12, 16], [6, 12, 17], [5, 12, 4], [5, 12, 5], [5, 12, 6], 
[5, 12, 7], [5, 12, 8], [5, 12, 9], [5, 12, 10], [5, 12, 11], [5, 12, 12], [5, 12, 13], [5, 12, 14], [5, 12, 15], [5, 12, 16], [5, 12, 17], [5, 12, 18], [4, 12, 4], [4, 12, 5], [4, 12, 6], [4, 12, 7], [4, 12, 8], [4, 12, 9], [4, 12, 10], [4, 12, 11], [4, 12, 12], [4, 12, 13], [4, 12, 14], [4, 12, 15], [4, 12, 16], [4, 12, 17], [4, 12, 18], [7, 13, 4], [7, 13, 5], [7, 13, 6], [7, 13, 7], [7, 13, 8], [7, 13, 9], [7, 13, 10], [7, 13, 11], [7, 13, 12], [7, 13, 13], [7, 13, 14], [7, 13, 15], [7, 13, 16], [7, 13, 17], [7, 13, 18], [6, 13, 4], [6, 13, 5], [6, 13, 6], [6, 13, 7], [6, 13, 8], [6, 13, 9], [6, 13, 10], [6, 13, 11], [6, 13, 12], [6, 13, 13], [6, 13, 14], [6, 13, 15], [6, 13, 16], [6, 13, 17], [6, 13, 18], [5, 13, 4], [5, 13, 5], [5, 13, 6], [5, 13, 7], [5, 13, 8], [5, 13, 9], [5, 13, 10], [5, 13, 11], [5, 13, 12], [5, 13, 13], [5, 13, 
14], [5, 13, 15], [5, 13, 16], [5, 13, 17], [5, 13, 18], [7, 14, 5], [7, 14, 11], [6, 14, 1], [6, 14, 2], [6, 14, 3], [6, 14, 4], [6, 14, 5], 
[6, 14, 6], [6, 14, 7], [6, 14, 8], [6, 14, 9], [6, 14, 10], [6, 14, 11], [6, 14, 12], [6, 14, 13], [6, 14, 14], [6, 14, 15], [6, 14, 16], [6, 14, 17], [5, 14, 5], [5, 14, 11], [5, 14, 17]]


# # Create axis
# axes = [1, 1, 1]

# # Create Data
# #data = np.ones(axes, dtype=np.bool_)
# data = np.array(xyz_coordinates)
# print(data.shape)
# #data = np.random.choice([0,1], size=(axes), p=[0.99, 0.01])

# # Control Transparency
# alpha = 0.9

# # Control colour
# colors = np.empty(axes + [4], dtype=np.float32)

# colors[:] = [1, 0, 0, alpha] # red

# # Plot figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')



# # Voxels is used to customizations of the
# # sizes, positions and colors.
# ax.voxels(data, facecolors=colors)

# plt.show()

X = [coord[0] for coord in xyz_coordinates]
Z = [coord[1] for coord in xyz_coordinates]
Y = [coord[2] for coord in xyz_coordinates]

#Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z)

#Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#Show plot
plt.show()





