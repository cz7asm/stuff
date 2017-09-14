def mandelbrot(x1, y1, x2, y2):
    sy = y2 - y1
    sx = x2 - x1
    MAX = 64
    width = 480
    height = 272
    matrix = [[0 for x in range(width)] for y in range(height)]
    for i in range(width):
        print(i)
        for j in range(height):
            cy = j*sy/height + y1
            cx = i*sx/width + x1
            x,y,xx,yy = [0]*4
            cyc = 0
            while cyc<=MAX and xx+yy<8:
                xx = x*x
                yy = y*y
                y = 2*x*y + cy
                x = xx-yy + cx
                cyc += 1
            matrix[j][i] = ((cyc<<4)%256, (cyc<<5)%256, cyc%256)
            #matrix[j][i] = ((cyc<<3)%256, (cyc<<6)%256, cyc%256)

    return matrix

cx = -0.086
cy = 0.85
zoom = 0.05
#cx = 0.15*0.5
#cy = 0.5*0.5

#matrix = mandelbrot(-2*cx, -1.5*cy, 2*cx, 1.5*cy)

from PIL import Image

#matrix = mandelbrot(-1.90, -1.2, 0.8, 1.2)
matrix = mandelbrot(-2.0*zoom+cx, -1.5*zoom+cy, 2.0*zoom+cx, 1.5*zoom+cy)
bm = [byte for row in matrix for color in row for byte in color]

img = Image.new('RGB', (480,272))
img.frombytes(buffer(bytearray(bm)))

img.show()
