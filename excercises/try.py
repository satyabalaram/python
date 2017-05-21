num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print x
print x1
print x2
print x3


print("The sum of digits in the number is", x+x1+x2+x3)

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

#volume of sphere is 4/3*pi*r**2
#area of circle is pi*r**2
#radius = 1/2diameter
#cicurmference of circle 2*pi*r
#area of triange is height*base/2
#area of rectangle is width * length
#area of square is side**2
#area of trapezoid is (base1+base2)/2*height
#greatest common divisor GCD ==>
#Least common multiple LCM ==>
#distance between 2 point (x1,y1) and (x2,y2) = math.sqrt(((x1[0]-y1[0])**2) + ((x1[1]-y1[1])**2)
#conversion height in ft & in to centimeters 1. convert all fit to in == hin += hft*12 and hcm = hin*2.54
#1 ft  = 12 in, 1yard = ft/3, 1mile = ft/5280
# 



############program1######################
#user_input = int(raw_input("Enter number:\n"))
#n1 = int("%s" % user_input)
#n2 = int("%s%s" % (user_input,user_input))
#n3 = int("%s%s%s" % (user_input,user_input,user_input))
#print( n1+n2+n3)


# program 2 #
#from datetime import date

#f_date = date(2014, 7, 2)
#l_date = date(2014, 7, 11)

#delta = l_date - f_date
#print (delta.days)


##program 3######
#from math import pi

#base1 = float(raw_input("enter base1\n"))
#base2 = float(raw_input("enter base2\n"))
#height = float(raw_input("enter height\n"))

#def vol_sphere(base1, base2,height):
 #       area = (base1+base2)/2*height
 #       return area

#print 'area of trapezhoid\t',vol_sphere(base1,base2,height)
