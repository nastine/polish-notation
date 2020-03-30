class LengthError(Exception):
  def __init__(self, number):
    self = "Введено неверное количество операндов:"
    print(self)

def polish_notation(user_list):
  try:
    assert user_list[0] in ["+", "-", "*", "/"], "Данной операции нет среди доступных!"
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
  except AssertionError as error:
    print(error)
  except LengthError as error:
    print(error)
  except ZeroDivisionError:
    print("Деление на ноль невозможно!")
  except ValueError:
    print("В качестве операндов введены не числа!")

polish_notation(input("Введите операцию: ").split())