print("Symptom Checker")
print("This is a student project, not a doctor.")
print("Answer with y for yes or n for no.")
print()

fever = input("Do you have a fever? ")
cough = input("Do you have a cough? ")
sneezing = input("Are you sneezing? ")
headache = input("Do you have a headache? ")
vomiting = input("Are you vomiting? ")
chest = input("Do you have chest pain? ")

print()

if chest == "y":
    print("Chest pain can be serious. Get medical help now.")
elif fever == "y" and cough == "y":
    print("Possible: Flu. Rest, drink water, stay home.")
elif sneezing == "y" and cough == "y":
    print("Possible: Common cold. Rest and drink warm fluids.")
elif sneezing == "y":
    print("Possible: Allergy. Avoid dust and pollen.")
elif headache == "y":
    print("Possible: Headache. Rest in a dark room and drink water.")
elif vomiting == "y":
    print("Possible: Stomach bug. Sip water and eat light food.")
else:
    print("No match found. See a doctor if you feel worse.")
