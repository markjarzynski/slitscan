import argparse
import sys
import imageio
from .slitscan import slitscan

def main():

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('--version', action='version', version='%(prog)s 0.3')
    parser.add_argument('-w', '--width', action='store', dest='width', default=1, help='slit width')
    parser.add_argument('-h', '--height', action='store', dest='height', default='100%', help='slit height')
    parser.add_argument('-x', action='store', dest='x', default='50%', help='Starting slit x position')
    parser.add_argument('-y', action='store', dest='y', default=0, help='Starting slit y position')
    parser.add_argument('-vx', '--velocity-x', action='store', dest='vx', default=0, help='slit x velocity')
    parser.add_argument('-vy', '--velocity-y', action='store', dest='vy', default=0, help='slit y velocity')
    parser.add_argument('-ow', '--out-width', action='store', dest='out_width', default=1, help='Output slit width')
    parser.add_argument('-oh', '--out-height', action='store', dest='out_height', default='100%', help='Output slit height')
    parser.add_argument('-ox', '--out-x', action='store', dest='out_x', default=0, help='Output slit starting x position')
    parser.add_argument('-oy', '--out-y', action='store', dest='out_y', default=0, help='Output slit starting y position')
    parser.add_argument('-ovx', '--out-velocity-x', action='store', dest='out_vx', default=1, help='Output slit x velocity')
    parser.add_argument('-ovy', '--out-velocity-y', action='store', dest='out_vy', default=0, help='Output slit y velocity')
    parser.add_argument('-i', '--input', action='store', nargs='+', dest='input')
    parser.add_argument('-o', '--output', action='store', dest='output', default='out.jpg')

    results=parser.parse_args()

    out = slitscan(results.input, results.width, results.height, results.x, results.y, results.vx, results.vy, results.out_width, results.out_height, results.out_x, results.out_y, results.out_vx, results.out_vy)
    imageio.imwrite(results.output, out)

if __name__ == "__main__":
    main()
