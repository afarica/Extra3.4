# Напишите функцию которая будет определять полигдром ли введенная строка. Если да 2
# то печатать “True”, если нет “False”.
a=str(input("Enter your word:"))
b=str(a[::-1])
if a==b: 
	print(True)
else:
	print(False)
