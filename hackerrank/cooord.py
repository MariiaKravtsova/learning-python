
'''
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0. The image you get is known to have a single rectangle of 0s on a background of 1s. Write a function that takes in the image and returns the coordinates of the rectangle -- either top-left and bottom-right; or top-left, width, and height.

Example input:
image = [
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 0, 0, 1, 1, 1],
[1, 1, 0, 0, 1, 1, 1],
[1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
]

Example output:
[[2,3],[3,5]]
{x: 3, y: 2, width: 3, height: 2}
'''

image = [
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
]

def find_coord(image):
    """Find the foreground (0) coordinates."""
    coords = [(x,y) for x in range(len(image)) for y in range(len(image[x])) if image[x][y] == 0]
    return coords[0], coords[-1]

print(find_coord(image))
