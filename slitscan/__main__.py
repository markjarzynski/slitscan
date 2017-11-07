import argparse
import sys
import imageio
from .slitscan import slitscan

def main():

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
    parser.add_argument('-w', '--width', action='store', dest='width', default=1, help='width')
    parser.add_argument('-h', '--height', action='store', dest='height', default=1080, help='height')
    parser.add_argument('-x', action='store', dest='x', default=960, help='x position')
    parser.add_argument('-y', action='store', dest='y', default=0, help='y position')
    parser.add_argument('-vx', '--velocity-x', action='store', dest='vx', default=0, help='x velocity')
    parser.add_argument('-vy', '--velocity-y', action='store', dest='vy', default=0, help='y velocity')
    parser.add_argument('-ow', '--out-width', action='store', dest='out_width', default=1, help='width')
    parser.add_argument('-oh', '--out-height', action='store', dest='out_height', default=1080, help='height')
    parser.add_argument('-ox', '--out-x', action='store', dest='out_x', default=0, help='x position')
    parser.add_argument('-oy', '--out-y', action='store', dest='out_y', default=0, help='y position')
    parser.add_argument('-ovx', '--out-velocity-x', action='store', dest='out_vx', default=1, help='x velocity')
    parser.add_argument('-ovy', '--out-velocity-y', action='store', dest='out_vy', default=0, help='y velocity')
    parser.add_argument('-i', '--input', action='store', nargs='+', dest='input')
    parser.add_argument('-o', '--output', action='store', dest='output', default='out.jpg')

    results=parser.parse_args()

    x = int(results.x)
    y = int(results.y)
    width = int(results.width)
    height = int(results.height)
    velocity_x = int(results.vx)
    velocity_y = int(results.vy)
    out_x = int(results.out_x)
    out_y = int(results.out_y)
    out_width = int(results.out_width)
    out_height = int(results.out_height)
    out_velocity_x = int(results.out_vx)
    out_velocity_y = int(results.out_vy)


    images = results.input
    out_file = results.output

    out = slitscan(images, width, height, x, y, velocity_x, velocity_y, out_width, out_height, out_x, out_y, out_velocity_x, out_velocity_y)
    imageio.imwrite(out_file, out)

if __name__ == "__main__":
    main()
