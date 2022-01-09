import sys
a = int(input())
b = int(input())
try:
  print(a / b ) # код в котором может быть ошибка
except ZeroDivisionError: # при ошибки с нулём(делением на ноль)
  print("на ноль делить нельзя", file=sys.stderr)
