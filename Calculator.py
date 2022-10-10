def calculate(action):

  if action == '+':
    summa = first_digit + second_digit
    print(first_digit, '+', second_digit, '=', summa)
  elif action == '-':
    difference = first_digit - second_digit
    print(first_digit, '-', second_digit, '=', difference)
  elif action == '*':
    multiplication = first_digit * second_digit
    print(first_digit, '*', second_digit, '=', multiplication)
  elif action == '/':
    division = first_digit / second_digit
    print(first_digit, '/', second_digit, '=', division)
  else:
    print('Введена неверная операция, попробуйте еще раз!')

first_digit = int(input('Введите первое число: '))
second_digit = int(input('введите второе число: '))
action = input('Введите операцию: ')

calculate(action)