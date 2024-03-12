from datetime import date, datetime

today = date.today()
print(f"Today is: {today}")
print(f"A day is: {today.day}")
print(f"A month is: {today.month}")
print(f"A year is: {today.year}\n")

todayDate = today.strftime("Today is %A, %dth %B %Y")
print(todayDate)

todayDateShort = today.strftime("Today is %a, %dth %b %y")
print(todayDateShort)

tomorrow = today.replace(day=today.day+1)
print(f"The date tomorrow will be: {tomorrow}")

yesterday = today.replace(day=today.day-1)
print(f"The date yesterday will be: {yesterday}")

nextYear = today.replace(year=today.year+1)
print(f"The next year will be: {nextYear.year}\n")

startNewYear = date(2025,1,1)
difference = abs(startNewYear - today)
print(f"Only {difference.days} days until the next year")

randomDate = date(1965, 8, 29)
print(f"It was in number weekday a {randomDate.weekday()}th day\n")

nowTime = datetime.now()
print(f"Right now is {nowTime.hour} hours {nowTime.minute} minutes, A date is {nowTime.day}th {nowTime.month}rd month, {nowTime.year} year\n")

firstAstronaut= datetime.fromisoformat("1961-04-12 09:07")
print(firstAstronaut)

gagarinFly = firstAstronaut.strftime("%A,%B, %dth, %Y at %X")
print(f"Gagarin became the first human to journey into outer space, the spaceflight was at {gagarinFly}")