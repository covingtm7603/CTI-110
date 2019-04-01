#Calculate amount of food tip precentages
#April 1/2019
#CTI-110 PSHW2 - Meal Tip Calculator
#Marcella Covington
#

#15%
total_charge = float(input("Enter the amount of meal: "))

#add tip to meal amount

tip = total_charge * .15
amount = total_charge + tip

#Display total

print ("The amount of meal $", format(amount, ",.2f"))

#18%
total_charge = float(input("Enter the amount of meal: "))

#add tip to meal amount
tip = total_charge * .18
amount = total_charge + tip

#Display total
print ("The amount of meal $", format(amount, ",.2f"))

#20%
total_charge = float(input("Enter the amount of meal: "))

#add tip to meal amount
tip = total_charge *.20
amount = total_charge + tip

#Display total
print ("The amount of meal $", format(amount, ",.2f"))
