import datetime

'''
now = datetime.datetime.today().strftime("%B, %d, %Y, %H:%M PM")
print(now)
'''

'''
year = int(input('Type down your birthday year: '))
month = int(input('Type down your birthday month: '))
day = int(input('Type down your birthday day: '))

today = datetime.datetime.today()
birthday = datetime.datetime(year, month, day)
days_past = today - birthday
real_days_past = days_past.days

print(str(real_days_past) + ' days past since your birth')
'''

year = int(input('Type down a year: '))
for elem in range(12):
    elem += 1
    date = datetime.datetime(year, elem, 13)
    if date.weekday() == 4:
        date = date.strftime("%Y-%d-%w")
        print('Friday 13-th found: ' + str(date))

