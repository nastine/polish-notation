class LengthError(Exception):
  def __init__(self, number):
    self = "Введено неверное количество операндов:"
    print(self)

def polish_notation(user_list):
  assert user_list[0] in ["+", "-", "*", "/"], "Данной операции нет среди доступных!"
  if int(user_list[1]) > 0 < int(user_list[2]):
    try:
      if len(user_list) != 3:
        raise LengthError(len(user_list) - 1)
      elif user_list[0] == "+":
        print(int(user_list[1]) + int(user_list[2]))
      elif user_list[0] == "-":
        print(int(user_list[1]) - int(user_list[2]))
      elif user_list[0] == "*":
        print(int(user_list[1]) * int(user_list[2]))
      elif user_list[0] == "/":
        print(int(user_list[1]) / int(user_list[2]))
    except LengthError as error:
      print(error)
    except ZeroDivisionError:
      print("Деление на ноль невозможно!")
    except ValueError:
      print("В качестве операндов введены не числа!")
  else:
    print("Программа работает только с положительными числами!")

polish_notation(input("Введите операцию, разделяя символы пробелами: ").split())