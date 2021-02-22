# 3 Friends went to pizza shop and ordered pizza,and each one ate different number of slices
# so we have to find out who need to pay how much

P1=input("what is the name of 1st friend? :")
P2=input("What is the name of 2nd friend? :")
P3=input("What is the name of 3rd friend? :")

Pizza_Price=input("Pizza Cost? :")
Slices= input("Number of slices? :")

P1S= input("How many slices "+P1+" ate? :")
P2S= input("How many slices "+P2+" ate? :")
P3S= input("How many slices "+P3+" ate? :")

#here we are calculating price of one slice
#since input we got was in string therefore we used float function to convert it into number
per_slice_cost = float(Pizza_Price)/float(Slices)

print(P1+ " have to pay :" + str(per_slice_cost*float(P1S)))
print(P2+ " have to pay :" + str(per_slice_cost*float(P2S)))
print(P3+ " have to pay :" + str(per_slice_cost*float(P3S)))