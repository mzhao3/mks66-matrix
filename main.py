from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14], [15,16,17,18], [19,20,21,22], [23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)
print_matrix(A)
print_matrix(B)
ident(matrix)
matrix_mult(matrix,A)
print_matrix(A)

def make_square(ulx, uly, color):
    shape = new_matrix()
    x = ulx
    while (x < ulx + 25):
        add_edge(shape, x, uly, 0, x, uly + 25, 0)
        x += 1

    draw_lines(shape, screen, color)


for x in range(-13, XRES + 100, 50):
    make_square(x, 0, color)
    make_square(x + 38 , 25, color )
    make_square(x, 50, color)
    make_square(x + 38, 75, color)
    make_square(x, 100, color)
    make_square(x + 38, 125, color)
    make_square(x, 150, color)
    make_square(x + 38, 175, color)
    make_square(x, 200, color)
    make_square(x + 38, 225, color)
    make_square(x, 250, color)
    make_square(x + 38, 275, color)
    make_square(x, 300, color)
    make_square(x + 38, 325, color)
    make_square(x, 350, color)
    make_square(x + 38, 375, color)
    make_square(x, 400, color)
    make_square(x + 38, 425, color)
    make_square(x, 450, color)
    make_square(x + 38, 475, color)
for y in range(0, YRES, 25):
    add_edge(matrix, 0, y, 0, XRES, y, 0)

draw_lines(matrix, screen, [211,211,211])

save_extension(screen, 'img.png')

display(screen)
