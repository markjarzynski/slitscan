import imageio
import numpy as np

def slitscan(images, width=1, height='100%', x='50%', y=0, velocity_x=0, velocity_y=0, out_width=1, out_height='100%', out_x=0, out_y=0, out_velocity_x=1, out_velocity_y=0):

    first = imageio.imread(images[0])

    if type(width) == str:
        if width[-1] == '%':
            width = int(first.shape[1] * float(width[:-1]) * 0.01)
        else:
            width = int(width)

    if type(height) == str:
        if height[-1] == '%':
            height = int(first.shape[0] * float(height[:-1]) * 0.01)
        else:
            height = int(height)

    if type(x) == str:
        if x[-1] == '%':
            x = int(first.shape[1] * float(x[:-1]) * 0.01)
        else:
            x = int(x)

    if type(y) == str:
        if y[-1] == '%':
            y = int(first.shape[0] * float(y[:-1]) * 0.01)
        else:
            y = int(y)

    if type(velocity_x) == str:
        if velocity_x[-1] == '%':
            velocity_x = int(first.shape[1] * float(velocity_x[:-1]) * 0.01)
        else:
            velocity_x = int(velocity_x)
        
    if type(velocity_y) == str:
        if velocity_y[-1] == '%':
            velocity_y = int(first.shape[0] * float(velocity_y[:-1]) * 0.01)
        else:
            velocity_y = int(velocity_y)
    
    if type(out_width) == str:
        if out_width[-1] == '%':
            out_width = int(first.shape[1] * float(out_width[:-1]) * 0.01)
        else:
            out_width = int(out_width)

    if type(out_height) == str:
        if out_height[-1] == '%':
            out_height = int(first.shape[0] * float(out_height[:-1]) * 0.01)
        else:
            out_height = int(out_height)

    if type(out_x) == str:
        if out_x[-1] == '%':
            out_x = int(first.shape[1] * float(out_x[:-1]) * 0.01)
        else:
            out_x = int(out_x)

    if type(out_y) == str:
        if out_y[-1] == '%':
            out_y = int(first.shape[0] * float(out_y[:-1]) * 0.01)
        else:
            out_y = int(out_y)

    if type(out_velocity_x) == str:
        if out_velocity_x[-1] == '%':
            out_velocity_x = int(first.shape[1] * float(out_velocity_x[:-1]) * 0.01)
        else:
            out_velocity_x = int(out_velocity_x)
        
    if type(out_velocity_y) == str:
        if out_velocity_y[-1] == '%':
            out_velocity_y = int(first.shape[0] * float(out_velocity_y[:-1]) * 0.01)
        else:
            out_velocity_y = int(out_velocity_y)

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

