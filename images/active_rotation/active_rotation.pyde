size(640, 630)

background(200)
noFill()

stroke(0)

line(0, 0.75*height, width, 0.75*height)
line(0.3*width, 0, 0.3*width, height)

fill(0)
ellipse(0.75*width, 0.5*height, 10, 10)
# ellipse(0.5*width, 0.25*height, 10, 10)
ellipse(cos(25*PI/180)*0.75*width - sin(25*PI/180)*0.5*height, 
        -sin(25*PI/180)*0.75*width + cos(25*PI/180)*0.5*height, 10, 10)

stroke(1)
