# Задание 3

Результат построения инвертированного индекса для документов [из 2-го задания](https://drive.google.com/drive/u/0/folders/1U4hL69VzJtFlG1u5Sl9or6gpd9_NkTO7):
### [Google Drive](https://drive.google.com/drive/u/0/folders/1-ZFaIF2hOmc875qyMZVIqg_sTwcRAVEo)

---

Пример поиска по документам из [2-го задания](https://drive.google.com/drive/u/0/folders/1U4hL69VzJtFlG1u5Sl9or6gpd9_NkTO7) и с использованием индекса из [1-го задания](https://drive.google.com/drive/u/0/folders/1K6z3IutgJiTFi8bsJlXVCGZ6BFR6BPuo):

```
>>> python3 index.py ../task2/docs/ ../task1/index.txt
Inverted index saved to inverted_index.txt

Query examples:
apple & banana | !orange
(apple | banana) & !orange
apple & banana | orange

Enter query (or 'exit' to quit): космос & птица | река
--------------------
doc_id  url
2       https://ru.wikipedia.org/wiki/Созвездие
4       https://ru.wikipedia.org/wiki/(21)_Лютеция
13      https://ru.wikipedia.org/wiki/Луна
22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
28      https://ru.wikipedia.org/wiki/Марс
39      https://ru.wikipedia.org/wiki/1801_год
40      https://ru.wikipedia.org/wiki/1807_год
42      https://ru.wikipedia.org/wiki/1945_год
47      https://ru.wikipedia.org/wiki/США
48      https://ru.wikipedia.org/wiki/Испания
49      https://ru.wikipedia.org/wiki/Бразилия
50      https://ru.wikipedia.org/wiki/Лёд
67      https://ru.wikipedia.org/wiki/Углерод
79      https://ru.wikipedia.org/wiki/Древнеримская_религия
80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
87      https://ru.wikipedia.org/wiki/Импактное_событие
91      https://ru.wikipedia.org/wiki/Земля
92      https://ru.wikipedia.org/wiki/Атомные_бомбардировки_Хиросимы_и_Нагасаки
93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
--------------------
Total: 19 documents.

Enter query (or 'exit' to quit): космос | птица | река
--------------------
doc_id  url
2       https://ru.wikipedia.org/wiki/Созвездие
4       https://ru.wikipedia.org/wiki/(21)_Лютеция
7       https://ru.wikipedia.org/wiki/(433)_Эрос
13      https://ru.wikipedia.org/wiki/Луна
16      https://ru.wikipedia.org/wiki/Солнечная_система
17      https://ru.wikipedia.org/wiki/Солнце
18      https://ru.wikipedia.org/wiki/Планета
22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
23      https://ru.wikipedia.org/wiki/Телескоп
24      https://ru.wikipedia.org/wiki/Звезда
27      https://ru.wikipedia.org/wiki/Пояс_астероидов
28      https://ru.wikipedia.org/wiki/Марс
29      https://ru.wikipedia.org/wiki/Юпитер
30      https://ru.wikipedia.org/wiki/(2)_Паллада
33      https://ru.wikipedia.org/wiki/Уран_(планета)
35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
37      https://ru.wikipedia.org/wiki/Астрономическая_единица
39      https://ru.wikipedia.org/wiki/1801_год
40      https://ru.wikipedia.org/wiki/1807_год
42      https://ru.wikipedia.org/wiki/1945_год
45      https://ru.wikipedia.org/wiki/Астрофотография
46      https://ru.wikipedia.org/wiki/2010_год
47      https://ru.wikipedia.org/wiki/США
48      https://ru.wikipedia.org/wiki/Испания
49      https://ru.wikipedia.org/wiki/Бразилия
50      https://ru.wikipedia.org/wiki/Лёд
52      https://ru.wikipedia.org/wiki/Комета
57      https://ru.wikipedia.org/wiki/(101955)_Бенну
65      https://ru.wikipedia.org/wiki/Цвет
67      https://ru.wikipedia.org/wiki/Углерод
79      https://ru.wikipedia.org/wiki/Древнеримская_религия
80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
83      https://ru.wikipedia.org/wiki/Меркурий
86      https://ru.wikipedia.org/wiki/Пояс_Койпера
87      https://ru.wikipedia.org/wiki/Импактное_событие
90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
91      https://ru.wikipedia.org/wiki/Земля
92      https://ru.wikipedia.org/wiki/Атомные_бомбардировки_Хиросимы_и_Нагасаки
93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
--------------------
Total: 39 documents.

Enter query (or 'exit' to quit): космос & птица & река
--------------------
doc_id  url
80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
91      https://ru.wikipedia.org/wiki/Земля
--------------------
Total: 2 documents.

Enter query (or 'exit' to quit): космос & !птица | !река
--------------------
doc_id  url
1       https://ru.wikipedia.org/wiki/Астероид
3       https://ru.wikipedia.org/wiki/(4)_Веста
5       https://ru.wikipedia.org/wiki/(253)_Матильда
6       https://ru.wikipedia.org/wiki/(243)_Ида
7       https://ru.wikipedia.org/wiki/(433)_Эрос
8       https://ru.wikipedia.org/wiki/(951)_Гаспра
9       https://ru.wikipedia.org/wiki/(2867)_Штейнс
10      https://ru.wikipedia.org/wiki/(25143)_Итокава
11      https://ru.wikipedia.org/wiki/Карликовая_планета
12      https://ru.wikipedia.org/wiki/Церера
13      https://ru.wikipedia.org/wiki/Луна
14      https://ru.wikipedia.org/wiki/Малая_планета
15      https://ru.wikipedia.org/wiki/Небесное_тело
16      https://ru.wikipedia.org/wiki/Солнечная_система
17      https://ru.wikipedia.org/wiki/Солнце
18      https://ru.wikipedia.org/wiki/Планета
19      https://ru.wikipedia.org/wiki/Спутник_астероида
20      https://ru.wikipedia.org/w/index.php
21      https://ru.wikipedia.org/wiki/Древнегреческий_язык
22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
23      https://ru.wikipedia.org/wiki/Телескоп
24      https://ru.wikipedia.org/wiki/Звезда
25      https://ru.wikipedia.org/wiki/XXVI_Ассамблея_Международного_астрономического_союза
26      https://ru.wikipedia.org/wiki/Международный_астрономический_союз
27      https://ru.wikipedia.org/wiki/Пояс_астероидов
28      https://ru.wikipedia.org/wiki/Марс
29      https://ru.wikipedia.org/wiki/Юпитер
30      https://ru.wikipedia.org/wiki/(2)_Паллада
31      https://ru.wikipedia.org/wiki/(99942)_Апофис
32      https://ru.wikipedia.org/wiki/1781_год
33      https://ru.wikipedia.org/wiki/Уран_(планета)
34      https://ru.wikipedia.org/wiki/Правило_Тициуса_—_Боде
35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
36      https://ru.wikipedia.org/wiki/1789_год
37      https://ru.wikipedia.org/wiki/Астрономическая_единица
38      https://ru.wikipedia.org/wiki/Угловая_секунда
41      https://ru.wikipedia.org/wiki/1830_год
43      https://ru.wikipedia.org/wiki/1891_год
44      https://ru.wikipedia.org/wiki/Вольф,_Максимилиан_Франц_Йозеф_Корнелиус
45      https://ru.wikipedia.org/wiki/Астрофотография
46      https://ru.wikipedia.org/wiki/2010_год
50      https://ru.wikipedia.org/wiki/Лёд
51      https://ru.wikipedia.org/wiki/Фемида_(астероид)
52      https://ru.wikipedia.org/wiki/Комета
53      https://ru.wikipedia.org/wiki/Изотоп
54      https://ru.wikipedia.org/wiki/Углеводород
55      https://ru.wikipedia.org/wiki/OSIRIS-REx
56      https://ru.wikipedia.org/wiki/Грунт
57      https://ru.wikipedia.org/wiki/(101955)_Бенну
58      https://ru.wikipedia.org/wiki/Галилео_(КА)
59      https://ru.wikipedia.org/wiki/XIX_век
60      https://ru.wikipedia.org/wiki/Покрытие_звёзд_астероидом
61      https://ru.wikipedia.org/wiki/Семейство_астероидов
62      https://ru.wikipedia.org/wiki/Астероиды,_сближающиеся_с_Землёй
63      https://ru.wikipedia.org/wiki/Атиры
64      https://ru.wikipedia.org/wiki/Спектральные_классы_астероидов
65      https://ru.wikipedia.org/wiki/Цвет
66      https://ru.wikipedia.org/wiki/Спектр
68      https://ru.wikipedia.org/wiki/Силикаты_(минералы)
69      https://ru.wikipedia.org/wiki/Металлы
70      https://ru.wikipedia.org/wiki/Минерал
71      https://ru.wikipedia.org/wiki/Ультрафиолетовое_излучение
72      https://ru.wikipedia.org/wiki/Оливин
73      https://ru.wikipedia.org/wiki/Железо
74      https://ru.wikipedia.org/wiki/Хондриты
75      https://ru.wikipedia.org/wiki/Карбонаты
76      https://ru.wikipedia.org/wiki/Кремний
77      https://ru.wikipedia.org/wiki/Металл
78      https://ru.wikipedia.org/wiki/Степенная_функция
81      https://ru.wikipedia.org/wiki/Орбита
82      https://ru.wikipedia.org/wiki/(1566)_Икар
83      https://ru.wikipedia.org/wiki/Меркурий
84      https://ru.wikipedia.org/wiki/Временное_обозначение_астероида
85      https://ru.wikipedia.org/wiki/Модель_Ниццы
86      https://ru.wikipedia.org/wiki/Пояс_Койпера
88      https://ru.wikipedia.org/wiki/Потенциально_опасные_объекты
89      https://ru.wikipedia.org/wiki/Туринская_шкала
90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
94      https://ru.wikipedia.org/wiki/Царь-бомба
95      https://ru.wikipedia.org/wiki/(11)_Парфенопа
96      https://ru.wikipedia.org/wiki/(13)_Эгерия
97      https://ru.wikipedia.org/wiki/(16)_Психея
98      https://ru.wikipedia.org/wiki/(20)_Массалия
99      https://ru.wikipedia.org/wiki/(22)_Каллиопа
100     https://ru.wikipedia.org/wiki/(24)_Фемида
--------------------
Total: 86 documents.

Enter query (or 'exit' to quit): космос | !птица | !река
--------------------
doc_id  url
1       https://ru.wikipedia.org/wiki/Астероид
3       https://ru.wikipedia.org/wiki/(4)_Веста
4       https://ru.wikipedia.org/wiki/(21)_Лютеция
5       https://ru.wikipedia.org/wiki/(253)_Матильда
6       https://ru.wikipedia.org/wiki/(243)_Ида
7       https://ru.wikipedia.org/wiki/(433)_Эрос
8       https://ru.wikipedia.org/wiki/(951)_Гаспра
9       https://ru.wikipedia.org/wiki/(2867)_Штейнс
10      https://ru.wikipedia.org/wiki/(25143)_Итокава
11      https://ru.wikipedia.org/wiki/Карликовая_планета
12      https://ru.wikipedia.org/wiki/Церера
13      https://ru.wikipedia.org/wiki/Луна
14      https://ru.wikipedia.org/wiki/Малая_планета
15      https://ru.wikipedia.org/wiki/Небесное_тело
16      https://ru.wikipedia.org/wiki/Солнечная_система
17      https://ru.wikipedia.org/wiki/Солнце
18      https://ru.wikipedia.org/wiki/Планета
19      https://ru.wikipedia.org/wiki/Спутник_астероида
20      https://ru.wikipedia.org/w/index.php
21      https://ru.wikipedia.org/wiki/Древнегреческий_язык
22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
23      https://ru.wikipedia.org/wiki/Телескоп
24      https://ru.wikipedia.org/wiki/Звезда
25      https://ru.wikipedia.org/wiki/XXVI_Ассамблея_Международного_астрономического_союза
26      https://ru.wikipedia.org/wiki/Международный_астрономический_союз
27      https://ru.wikipedia.org/wiki/Пояс_астероидов
28      https://ru.wikipedia.org/wiki/Марс
29      https://ru.wikipedia.org/wiki/Юпитер
30      https://ru.wikipedia.org/wiki/(2)_Паллада
31      https://ru.wikipedia.org/wiki/(99942)_Апофис
32      https://ru.wikipedia.org/wiki/1781_год
33      https://ru.wikipedia.org/wiki/Уран_(планета)
34      https://ru.wikipedia.org/wiki/Правило_Тициуса_—_Боде
35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
36      https://ru.wikipedia.org/wiki/1789_год
37      https://ru.wikipedia.org/wiki/Астрономическая_единица
38      https://ru.wikipedia.org/wiki/Угловая_секунда
39      https://ru.wikipedia.org/wiki/1801_год
40      https://ru.wikipedia.org/wiki/1807_год
41      https://ru.wikipedia.org/wiki/1830_год
42      https://ru.wikipedia.org/wiki/1945_год
43      https://ru.wikipedia.org/wiki/1891_год
44      https://ru.wikipedia.org/wiki/Вольф,_Максимилиан_Франц_Йозеф_Корнелиус
45      https://ru.wikipedia.org/wiki/Астрофотография
46      https://ru.wikipedia.org/wiki/2010_год
48      https://ru.wikipedia.org/wiki/Испания
50      https://ru.wikipedia.org/wiki/Лёд
51      https://ru.wikipedia.org/wiki/Фемида_(астероид)
52      https://ru.wikipedia.org/wiki/Комета
53      https://ru.wikipedia.org/wiki/Изотоп
54      https://ru.wikipedia.org/wiki/Углеводород
55      https://ru.wikipedia.org/wiki/OSIRIS-REx
56      https://ru.wikipedia.org/wiki/Грунт
57      https://ru.wikipedia.org/wiki/(101955)_Бенну
58      https://ru.wikipedia.org/wiki/Галилео_(КА)
59      https://ru.wikipedia.org/wiki/XIX_век
60      https://ru.wikipedia.org/wiki/Покрытие_звёзд_астероидом
61      https://ru.wikipedia.org/wiki/Семейство_астероидов
62      https://ru.wikipedia.org/wiki/Астероиды,_сближающиеся_с_Землёй
63      https://ru.wikipedia.org/wiki/Атиры
64      https://ru.wikipedia.org/wiki/Спектральные_классы_астероидов
65      https://ru.wikipedia.org/wiki/Цвет
66      https://ru.wikipedia.org/wiki/Спектр
67      https://ru.wikipedia.org/wiki/Углерод
68      https://ru.wikipedia.org/wiki/Силикаты_(минералы)
69      https://ru.wikipedia.org/wiki/Металлы
70      https://ru.wikipedia.org/wiki/Минерал
71      https://ru.wikipedia.org/wiki/Ультрафиолетовое_излучение
72      https://ru.wikipedia.org/wiki/Оливин
73      https://ru.wikipedia.org/wiki/Железо
74      https://ru.wikipedia.org/wiki/Хондриты
75      https://ru.wikipedia.org/wiki/Карбонаты
76      https://ru.wikipedia.org/wiki/Кремний
77      https://ru.wikipedia.org/wiki/Металл
78      https://ru.wikipedia.org/wiki/Степенная_функция
79      https://ru.wikipedia.org/wiki/Древнеримская_религия
80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
81      https://ru.wikipedia.org/wiki/Орбита
82      https://ru.wikipedia.org/wiki/(1566)_Икар
83      https://ru.wikipedia.org/wiki/Меркурий
84      https://ru.wikipedia.org/wiki/Временное_обозначение_астероида
85      https://ru.wikipedia.org/wiki/Модель_Ниццы
86      https://ru.wikipedia.org/wiki/Пояс_Койпера
87      https://ru.wikipedia.org/wiki/Импактное_событие
88      https://ru.wikipedia.org/wiki/Потенциально_опасные_объекты
89      https://ru.wikipedia.org/wiki/Туринская_шкала
90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
91      https://ru.wikipedia.org/wiki/Земля
93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
94      https://ru.wikipedia.org/wiki/Царь-бомба
95      https://ru.wikipedia.org/wiki/(11)_Парфенопа
96      https://ru.wikipedia.org/wiki/(13)_Эгерия
97      https://ru.wikipedia.org/wiki/(16)_Психея
98      https://ru.wikipedia.org/wiki/(20)_Массалия
99      https://ru.wikipedia.org/wiki/(22)_Каллиопа
100     https://ru.wikipedia.org/wiki/(24)_Фемида
--------------------
Total: 96 documents.
```
