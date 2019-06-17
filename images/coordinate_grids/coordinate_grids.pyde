
size(640, 640)

background(128)
noFill()

nx = width / 20
ny = height / 20

stroke(0)
# manifold=R^{2,0}
for i in range(0, width):
    line(0, i*nx, width, i*nx)
for i in range(0, height):
    line(i*ny, 0, i*ny, height)
    #line(i*ny, 0, height, i*ny)

# rotated and dilated
# for i in range(0,width):
#     line(0, i*nx, width, i*nx)
# for i in range(0, height):
#     line(i*ny/2, 0, 2*i*ny, height)

# lightcone dilation
# for i in range(0, width):
#     if i == 3 or i == 5 or i == 10 or i == 13 or i == 18:
#         continue
#     else:
#         line(0, i*nx, width, i*nx)
# for i in range(0, height):
#     if i == 5 or i == 8 or i == 12 or i == 15 or i == 20:
#         continue
#     else:
#         line(i*ny, 0, i*ny, height)

# strokeWeight(3)
# line(0, height/2, width, height/2)
# line(width/2, 0, width/2, height)
