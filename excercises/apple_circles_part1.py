''' Algorithm to find out if any overlapping circles
and eliminating the small circles '''
from math import sqrt

def overlap (first_circle,second_circle):
    x1,y1,r1 = first_circle
    x2,y2,r2 = second_circle
    d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    if r1 + r2 <= d:
        return (0,0,0)
    elif r1 < r2:
        return first_circle
    else:
        return second_circle

circles = [(2,2,1.0),(2,2,2.0),(8,8,3.0)]
print 'actual circles:',circles
remove_circles = []

s1 = overlap(circles[0],circles[1])
if s1 != (0,0,0):
    remove_circles.append(s1)
s2 = overlap(circles[0],circles[2])
if s2 != (0,0,0):
    remove_circles.append(s1)
s3 = overlap(circles[1],circles[2])
if s3 != (0,0,0):
    remove_circles.append(s1)
print 'overlaping circles:', remove_circles
for n in remove_circles:
    if n in circles:
        circles.pop(circles.index(n))
print 'final circles:', circles 








