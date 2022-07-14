from PIL import Image
import argparse
from functions.SquareBump import SquareBump
from functions.DistanceSquared import DistanceSquared
from functions.Hyperboloid import Hyperboloid
from functions.TrigProduct import TrigProduct

func_choices = ['SquareBump', 'DistanceSquared', 'Hyperboloid', 'TrigProduct']
func_arg_parser = {
    'SquareBump': SquareBump.parse_args,
    'DistanceSquared': DistanceSquared.parse_args,
    'Hyperboloid': Hyperboloid.parse_args,
    'TrigProduct': TrigProduct.parse_args
}

func_evals = {
    'SquareBump': SquareBump.distance,
    'DistanceSquared': DistanceSquared.distance,
    'Hyperboloid': Hyperboloid.distance,
    'TrigProduct': TrigProduct.distance
}

parser = argparse.ArgumentParser(description='Visualize distance function on an NxM image.')
parser.add_argument('w', type=int, help='image width')
parser.add_argument('h', type=int, help='image height')
parser.add_argument('f', type=str, help='Distance function', choices=func_choices, default='SquareBump')

args = parser.parse_known_args()

eargs = args[0]
width = int(eargs.w)
height = int(eargs.h)
func_name = str(eargs.f)

fargs = args[1]
func = func_evals[func_name]
opts = func_arg_parser[func_name](fargs)

print("Creating " + str(width) + "x" + str(height) + " distance map using " + func_name + " " + str(opts))

dmap = Image.new("L", size=(width, height), color=255)

for x in range(width):
    for y in range(height):
        l = func(x, y, dmap.width - 1, dmap.height - 1, opts)
        dmap.putpixel((x, y), int(l * 255))

dmap.show()
# dmap.save('lake_tests/Hyperboloid.jpg')
