actually_sick = str('actually_sick')
kinda_sick = str('kinda_sick')
hate_your_job = str('hate_your_job')
condition = str(input('What is your condition? '))
sick_days_remaining = int(input('sick_days_remaining= '))
if actually_sick and sick_days_remaining >= 8 < 10:
    print("You are actually sick and get rest!")
elif kinda_sick and sick_days_remaining >= 4 < 6:
    print("You are kinda sick!")
else:
    print("You are lying!")


