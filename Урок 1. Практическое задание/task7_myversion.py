"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
a = int(input("Сколько километров в первый день составил результат >>> "))  # ввод км за 1 день
b = int(input("Сколько километров надо пробежать >>> "))  # ввод необходимого результата
c = 1  # дни
while a <= b:  # цикл будет повторяться, пока не будет необходимого результата
    x = (a * 10) / 100  # формула для нахождения 10% от количества км, которых пробежал спортсмен
    a = a + x  # количество километров с увеличением на 10% за каждый новый день
    c = c + 1  # увеличение количества дней
    print("Расстояние увеличелось на:" "%.2f" % x, " Расстояние составляет:" "%.2f" % a, " За", c, "дня/дней")
    # я решила вывести на экран все результаты вычислений, чтобы быть уверенной что все врено работает
print("На", c, "день спортсмен достигнет результата, пробежав не менее", b, "километров")
# вывод результата
