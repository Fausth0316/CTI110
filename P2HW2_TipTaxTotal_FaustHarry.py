# CTI-110
# P2HW2-Tip Tax Total
# Harry Faust
# 2/26/2018

foodcost = float( input( "Please enter the cost of the food: " ) )

tip = 0.15 * foodcost

saletax = 0.07 * foodcost

total = foodcost + tip + saletax

print( "Food Cost: $" + format( foodcost, ",.2f"), "Tip: $" + \
       format( tip, ",.2f" ), "Sale Tax: $" + format( saletax, ",.2f"), \
       "Total: $" + format( total, ",.2f") )
