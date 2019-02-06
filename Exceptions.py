
class UserNameError(Exception):
  pass

try:
  # code, which can raise an exception
    w = float(input('weight:'))
    res = 10/w
    print(w)
    raise UserNameError
except ValueError as e :
  # do something if an ExceptionType was raised
    print(e.args)
except ZeroDivisionError as e :
    print(e)
except EOFError as e :
    print(e)
except NameError as e :
    print(e)
except UserNameError as e :
    print(e)
except :
    print(e)
else:
  # do something if there was no Exception
    print('go on')
finally:
    print('end')
  # do something no matter if an Exception was raised or not.
  # (useful for closing DB connections, etc.)

