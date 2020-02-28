#Постановка задачи:
#Написать функцию is_year_leap, принимающую 1 аргумент — год,
#и возвращающую True, если год високосный, и False иначе.
#
#
#Первый вариант решения задачи (сам написал)
def Leap_year1(year):
	try:
		if year % 400 == 0:
			return True
		elif year % 100 == 0:
			return False
		elif year % 4 == 0:
			return True
		else:
			return False
	except:
		print("Введённое число не является годом!")

#Второй вариант решения задачи
def Leap_year2(year):
	try:
		if year % 400 == 0:
			return True
		return year % 4 == 0 and year % 100 != 0
	except:
		print("Введённое число не является годом!")

#Третий вариант решения задачи
def is_year_leap(year):
	try:
		if year % 400 == 0:
			return True
		if year % 4 == 0 and year % 100 != 0:
			return True
		return False
	except:
		print("Введённое число не является годом!")