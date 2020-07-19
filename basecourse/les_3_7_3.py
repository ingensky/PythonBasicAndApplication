'''# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for _ in range(int(input()))}

# заводим пустое множество для приема текста
wrd = set()

# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd-dic), sep="\n")

Основа работы кода - свойство множеств хранить только уникальные значения.
wrd |= {...} отвечает за добавление множества {...} в единое wrd (аналог метода update)
Обращаем внимание на звездочку *, которая вытаскивает элементы на вывод, вместо того, чтобы печатать в виде множества'''

dictionary, text, res = [input().lower() for _ in range(int(input()))], [input() for _ in range(int(input()))], set()
for line in text:
    for word in line.split():
        if word.lower() not in dictionary:
            res.add(word)
print("\n".join(res))


'''Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте 
ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов,
 после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. 
Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

﻿
Sample Input:

3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:

aab
aba
c
aaa'''