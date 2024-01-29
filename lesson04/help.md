# Повторення

### Виведення даних

```hs 
print("Text")

print('Text1', 'Text2', 123)

print('Text: %s Number: %d' %('Text', 123))

print(f'Text {name}, Integer{num}')
```

Так неправильно:

> print "Text"

або

> print(y)
>

Буде помилка, перед виведенням змінна має бути визначена   

_NameError: name 'x' is not defined)_

### Введення даних

```hs 
name = input('Введіть імя: ')

age = int(input('Введіть ваш вік: '))

nuber = float(input('Введіть дробове чиcло: '))
```

### Введення даних
