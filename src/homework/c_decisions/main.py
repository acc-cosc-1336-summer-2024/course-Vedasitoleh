import decisions

option = float(input("Enter option:"))
total = float(input("Enter total:"))

ratio = decisions.get_options_ratio(option,total)

print ("Your faculty rating is: "+ decisions.get_faculty_rating(ratio))