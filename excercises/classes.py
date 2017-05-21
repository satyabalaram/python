class py_solution:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(2, -3));
print(py_solution().pow(3, 5));
print(py_solution().pow(100, 0));

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def area_rect(self):
        self.area = self.length * self.width
        return self.area

newRectangle = Rectangle(12,10)
print (newRectangle.area_rect())



class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*self.radius**2
       

    def perimeter(self):
        return 2*3.14*self.radius
        

NewCircle = Circle(8)

print NewCircle.area()
print NewCircle.perimeter()
