from PIL import Image
from functions.SquareBump import SquareBump
from functions.DistanceSquared import DistanceSquared
from functions.Hyperboloid import Hyperboloid
from functions.TrigProduct import TrigProduct

sb = Image.open('heightmap.jpg')
sb = sb.convert(mode='RGB')
# ds = Image.open('heightmap.jpg')
# hyper = Image.open('heightmap.jpg')
# trig = Image.open('heightmap.jpg')

width, height = sb.size

# Square bump
options = [0.025, 4]
height_thres = 35
for x in range(width):
    for y in range(height):
        r, g, b = sb.getpixel((x, y))
        wh = r * Hyperboloid.distance(x, y, width, height, options)
        color = (int(wh), int(wh), int(wh))

        if int(wh) < height_thres:
            wh = color = (0, 0, 255)

        sb.putpixel((x, y), color)

sb.show()
# sb.save('lake_tests/TrigProduct_35.jpg')
