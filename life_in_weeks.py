def life_in_weeks(age):
    weeks = (90-age)*52
    print(f"You have {weeks}  weeks left.")

age=int(input('enter your age'))
life_in_weeks(age)