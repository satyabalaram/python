list1 = []

def max_of_three(a, b, c):
        max =0;
        if (a > b):
                if(a>c):
                        max =a
                else:
                        max =c
        else:
                if(b>c):
                        if (b>a):
                                max = b
                        else:
                                max =a
                else:
                        max =c
               

        return max

a = raw_input("First number:")
b = raw_input("Second number:")
c = raw_input("Third number:")

max = max_of_three(a, b, c)

print max


        
        
