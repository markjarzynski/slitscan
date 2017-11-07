import imageio
import numpy as np

def slitscan(images, width=1, height=1080, x=960, y=0, velocity_x=0, velocity_y=0, out_width=1, out_height=1080, out_x=0, out_y=0, out_velocity_x=1, out_velocity_y=0):

    first = imageio.imread(images[0])
    out = np.zeros(first.shape, dtype=np.float32)

    for i in images:
        
        print('Processing ' + i)

        img = imageio.imread(i)

        overlap = float(out_velocity_x) / out_width
        if overlap > 1:
            overlap = 1

        out[out_y : out_y + out_height, out_x : out_x + out_width] += img[y : y + height, x : x + width] * overlap

        x += velocity_x
        y += velocity_y

        out_x += out_velocity_x
        out_y += out_velocity_y

    out = np.around(out).astype(np.uint8)

    return out

