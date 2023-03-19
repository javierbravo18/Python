print("This script provides a guideline for the amount of calories and protein you should consume daily aimed at fat loss. Fill out the information requested below.")
print("...")

weight = float(input('Enter your weight in pounds.\n'))
feet = float(input('Enter your height in feet. Do not include inches as we will ask for inches next. Example: if you are 5 feet and 10 inches tall only enter 5.\n'))
inches = float(input('Enter your inches. Example: if you are 5 feet and 10 inches tall only enter 10.\n'))
activity = float(input('How many days a week do you exercise? Minimum is 0, Maximum is 7.\n'))
gender = input('Are you a male? Enter y if yes and n if no.\n')
age = float(input('How old are you?\n'))
lean = input('Are you relatively lean ( Men ≤ 15% body fat, Women ≤ 25% body fat) AND resistance train ≥ 4 days per week? Enter y for yes and n for no.\n')
fat = input('Is your body fat percent relatively high? (> 25% body fat for men, > 30% body fat for women) Enter y for yes and n for no.\n')
meals = float(input('How many meals/snacks would you like to eat every day? (Aim for 3-6 meals/snacks per day).\n'))

invalid = 0

weight_kg = weight/2.2046
height = feet + (inches/12)
height_cm = height * 30.48

while invalid == 0:

	if activity == 0:

	    activity_factor = 1.2
	    invalid = 1

	elif activity >= 1 and activity <= 3:

	    activity_factor = 1.3
	    invalid = 1

	elif activity >= 4 and activity <= 5:

	    activity_factor = 1.5
	    invalid = 1

	elif activity >= 6 and activity <= 7:

	    activity_factor = 1.7
	    invalid = 1

	else:

		activity = float(input('How many days a week do you exercise? Minimum is 0, Maximum is 7.\n'))


if lean == 'y':

	basal = 24.8 * weight_kg + 10

elif lean == 'n' and gender == 'y':

	basal = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5

elif lean == 'n' and gender == 'n':

	basal = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

else:

	print('You fucked something up. Stop here and re-run the script. Can you even read?!')

total_energy = basal * activity_factor

target = total_energy * 0.8

if fat == 'y':

	protein = weight * 0.8

else:

	protein = weight

protein_per_meal = protein / meals

rounded_basal = round(basal, 2)

rounded_total_energy = round(total_energy, 2)

rounded_target = round(target, 2)

rounded_protein = round(protein, 2)

rounded_protein_per_meal = round(protein_per_meal, 2)

print("Calculating...")
print("...")
print("...")
print("...")
print(f"Basal Metabolic Rate (the number of calories you burn at rest): {rounded_basal} calories.")
print(f"Total Energy Expenditure: {rounded_total_energy} calories.")
print(f"Target Daily Caloric Intake: {rounded_target} calories.")
print(f"Daily Protein Requirement: {rounded_protein} grams.")
print(f"Protein per meal: {rounded_protein_per_meal} grams.")













