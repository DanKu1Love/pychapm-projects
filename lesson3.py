def main_function():
	action = input('\nВведите операцию: ')
	count_of_actions = int(input('Введите количество операндов: '))
	answer = 0
	count_numbers = ''

	if action == '+':
		for plus in range(count_of_actions):
			number = int(input('Введите число: '))
			answer += number
			if plus - count_of_actions == -1:
				count_numbers += str(number) + ' ='
			else:
				count_numbers += str(number) + ' + '
		print(count_numbers, answer)

	
	elif action == '-':
		for plus in range(count_of_actions):
			number = int(input('Введите число: '))
			if plus == 0:
				answer = number
			else:
				answer -= number
			if plus - count_of_actions == -1:
				count_numbers += str(number) + ' ='
			else:
				count_numbers += str(number) + ' - '
		print(count_numbers, answer)

	elif action == '*':
		answer = 1
		for plus in range(count_of_actions):
			number = int(input('Введите число: '))
			answer *= number
			if plus - count_of_actions == -1:
				count_numbers += str(number) + ' ='
			else:
				count_numbers += str(number) + ' * '
		print(count_numbers, answer)

	elif action == '/':
		for plus in range(count_of_actions):
			number = int(input('Введите число: '))
			if plus == 0:
				answer = number
			else:
				answer /= number
			if plus - count_of_actions == -1:
				count_numbers += str(number) + ' ='
			else:
				count_numbers += str(number) + ' / '
		print(count_numbers, answer)

	else:
		print('Ошибка ввода. Попробуйте снова:')
		main_function()

main_function()