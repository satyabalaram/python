tax = 0.08
print 'This program will calculate a restaurant tab for a couple with a gift certificate, with a restaurant tax of', tax* 100, '%'

gift_certificate = float(input('Enter the amount of gift certificate:'))

print 'Enter ordered items for a person 1'

appetizer1= float(input('Appetizer:'))
Entree1 = float(input('Entree:'))
Drinks1 = float(input('Drinks:'))
Dessert1 = float(input('Dessert:'))

print 'Enter ordered items for a person 2'
appetizer2= float(input('Appetizer:'))
Entree2 = float(input('Entree:'))
Drinks2 = float(input('Drinks:'))
Dessert2 = float(input('Dessert:'))

person1_total = appetizer1 + Entree1 + Drinks1 + Dessert1
person2_total = appetizer2 + Entree2 + Drinks2 + Dessert2
ordered_amount = person1_total + person2_total
restaurant_tax = ordered_amount * tax
print 'Ordered items: $', ordered_amount, '\n Restaurant tax: $',restaurant_tax 

print 'Tab: $' , ordered_amount + restaurant_tax - gift_certificate
