# Задание 5

Пример векторного поиска по таблицам из [4-го задания](https://drive.google.com/drive/u/0/folders/1QebVj3CNpLLcuBk4AFLOePWrNmpJ-WlC) и с использованием индекса из [1-го задания](https://drive.google.com/drive/u/0/folders/1K6z3IutgJiTFi8bsJlXVCGZ6BFR6BPuo):

```
>>> python3 index.py ../task4/ ../task1/index.txt
Vector search engine ready

Search query (or 'exit'): космос
--------------------
score   doc_id  url
0.0502  86      https://ru.wikipedia.org/wiki/Пояс_Койпера
0.0493  45      https://ru.wikipedia.org/wiki/Астрофотография
0.0425  91      https://ru.wikipedia.org/wiki/Земля
0.0378  23      https://ru.wikipedia.org/wiki/Телескоп
0.0363  90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
0.0214  29      https://ru.wikipedia.org/wiki/Юпитер
0.0203  30      https://ru.wikipedia.org/wiki/(2)_Паллада
0.0192  16      https://ru.wikipedia.org/wiki/Солнечная_система
0.0186  17      https://ru.wikipedia.org/wiki/Солнце
0.0170  27      https://ru.wikipedia.org/wiki/Пояс_астероидов
0.0150  18      https://ru.wikipedia.org/wiki/Планета
0.0139  35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
0.0133  37      https://ru.wikipedia.org/wiki/Астрономическая_единица
0.0131  83      https://ru.wikipedia.org/wiki/Меркурий
0.0110  7       https://ru.wikipedia.org/wiki/(433)_Эрос
0.0106  50      https://ru.wikipedia.org/wiki/Лёд
0.0103  28      https://ru.wikipedia.org/wiki/Марс
0.0102  13      https://ru.wikipedia.org/wiki/Луна
0.0073  24      https://ru.wikipedia.org/wiki/Звезда
0.0073  33      https://ru.wikipedia.org/wiki/Уран_(планета)
0.0062  52      https://ru.wikipedia.org/wiki/Комета
0.0049  46      https://ru.wikipedia.org/wiki/2010_год
0.0039  80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
0.0031  93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
0.0021  22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
--------------------
Total: 25 documents.

Search query (or 'exit'): космос вода
--------------------
score   doc_id  url
0.0722  50      https://ru.wikipedia.org/wiki/Лёд
0.0673  91      https://ru.wikipedia.org/wiki/Земля
0.0487  100     https://ru.wikipedia.org/wiki/(24)_Фемида
0.0477  51      https://ru.wikipedia.org/wiki/Фемида_(астероид)
0.0459  86      https://ru.wikipedia.org/wiki/Пояс_Койпера
0.0418  45      https://ru.wikipedia.org/wiki/Астрофотография
0.0384  23      https://ru.wikipedia.org/wiki/Телескоп
0.0381  75      https://ru.wikipedia.org/wiki/Карбонаты
0.0380  1       https://ru.wikipedia.org/wiki/Астероид
0.0346  13      https://ru.wikipedia.org/wiki/Луна
0.0308  28      https://ru.wikipedia.org/wiki/Марс
0.0308  90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
0.0288  29      https://ru.wikipedia.org/wiki/Юпитер
0.0286  27      https://ru.wikipedia.org/wiki/Пояс_астероидов
0.0284  71      https://ru.wikipedia.org/wiki/Ультрафиолетовое_излучение
0.0278  16      https://ru.wikipedia.org/wiki/Солнечная_система
0.0230  17      https://ru.wikipedia.org/wiki/Солнце
0.0228  96      https://ru.wikipedia.org/wiki/(13)_Эгерия
0.0204  56      https://ru.wikipedia.org/wiki/Грунт
0.0180  97      https://ru.wikipedia.org/wiki/(16)_Психея
0.0176  83      https://ru.wikipedia.org/wiki/Меркурий
0.0172  30      https://ru.wikipedia.org/wiki/(2)_Паллада
0.0152  18      https://ru.wikipedia.org/wiki/Планета
0.0145  73      https://ru.wikipedia.org/wiki/Железо
0.0118  35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
0.0113  37      https://ru.wikipedia.org/wiki/Астрономическая_единица
0.0111  12      https://ru.wikipedia.org/wiki/Церера
0.0111  33      https://ru.wikipedia.org/wiki/Уран_(планета)
0.0093  7       https://ru.wikipedia.org/wiki/(433)_Эрос
0.0076  74      https://ru.wikipedia.org/wiki/Хондриты
0.0073  52      https://ru.wikipedia.org/wiki/Комета
0.0073  67      https://ru.wikipedia.org/wiki/Углерод
0.0070  87      https://ru.wikipedia.org/wiki/Импактное_событие
0.0068  58      https://ru.wikipedia.org/wiki/Галилео_(КА)
0.0062  24      https://ru.wikipedia.org/wiki/Звезда
0.0058  93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
0.0058  88      https://ru.wikipedia.org/wiki/Потенциально_опасные_объекты
0.0045  69      https://ru.wikipedia.org/wiki/Металлы
0.0044  77      https://ru.wikipedia.org/wiki/Металл
0.0044  70      https://ru.wikipedia.org/wiki/Минерал
0.0042  46      https://ru.wikipedia.org/wiki/2010_год
0.0038  57      https://ru.wikipedia.org/wiki/(101955)_Бенну
0.0037  76      https://ru.wikipedia.org/wiki/Кремний
0.0033  80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
0.0032  72      https://ru.wikipedia.org/wiki/Оливин
0.0031  54      https://ru.wikipedia.org/wiki/Углеводород
0.0027  59      https://ru.wikipedia.org/wiki/XIX_век
0.0021  65      https://ru.wikipedia.org/wiki/Цвет
0.0020  49      https://ru.wikipedia.org/wiki/Бразилия
0.0018  22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
0.0012  94      https://ru.wikipedia.org/wiki/Царь-бомба
0.0006  48      https://ru.wikipedia.org/wiki/Испания
--------------------
Total: 52 documents.

Search query (or 'exit'): космос вода жизнь
--------------------
score   doc_id  url
0.0812  91      https://ru.wikipedia.org/wiki/Земля
0.0649  50      https://ru.wikipedia.org/wiki/Лёд
0.0479  100     https://ru.wikipedia.org/wiki/(24)_Фемида
0.0469  51      https://ru.wikipedia.org/wiki/Фемида_(астероид)
0.0437  86      https://ru.wikipedia.org/wiki/Пояс_Койпера
0.0420  28      https://ru.wikipedia.org/wiki/Марс
0.0380  29      https://ru.wikipedia.org/wiki/Юпитер
0.0376  45      https://ru.wikipedia.org/wiki/Астрофотография
0.0368  1       https://ru.wikipedia.org/wiki/Астероид
0.0345  23      https://ru.wikipedia.org/wiki/Телескоп
0.0342  75      https://ru.wikipedia.org/wiki/Карбонаты
0.0328  13      https://ru.wikipedia.org/wiki/Луна
0.0318  16      https://ru.wikipedia.org/wiki/Солнечная_система
0.0309  17      https://ru.wikipedia.org/wiki/Солнце
0.0308  90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
0.0265  71      https://ru.wikipedia.org/wiki/Ультрафиолетовое_излучение
0.0257  27      https://ru.wikipedia.org/wiki/Пояс_астероидов
0.0205  96      https://ru.wikipedia.org/wiki/(13)_Эгерия
0.0183  56      https://ru.wikipedia.org/wiki/Грунт
0.0177  24      https://ru.wikipedia.org/wiki/Звезда
0.0175  83      https://ru.wikipedia.org/wiki/Меркурий
0.0162  97      https://ru.wikipedia.org/wiki/(16)_Психея
0.0156  18      https://ru.wikipedia.org/wiki/Планета
0.0155  30      https://ru.wikipedia.org/wiki/(2)_Паллада
0.0149  57      https://ru.wikipedia.org/wiki/(101955)_Бенну
0.0141  35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
0.0131  73      https://ru.wikipedia.org/wiki/Железо
0.0125  46      https://ru.wikipedia.org/wiki/2010_год
0.0118  33      https://ru.wikipedia.org/wiki/Уран_(планета)
0.0112  12      https://ru.wikipedia.org/wiki/Церера
0.0112  67      https://ru.wikipedia.org/wiki/Углерод
0.0101  37      https://ru.wikipedia.org/wiki/Астрономическая_единица
0.0100  93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
0.0095  88      https://ru.wikipedia.org/wiki/Потенциально_опасные_объекты
0.0089  87      https://ru.wikipedia.org/wiki/Импактное_событие
0.0086  58      https://ru.wikipedia.org/wiki/Галилео_(КА)
0.0084  7       https://ru.wikipedia.org/wiki/(433)_Эрос
0.0082  22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
0.0081  52      https://ru.wikipedia.org/wiki/Комета
0.0079  80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
0.0069  74      https://ru.wikipedia.org/wiki/Хондриты
0.0054  62      https://ru.wikipedia.org/wiki/Астероиды,_сближающиеся_с_Землёй
0.0052  47      https://ru.wikipedia.org/wiki/США
0.0046  31      https://ru.wikipedia.org/wiki/(99942)_Апофис
0.0044  59      https://ru.wikipedia.org/wiki/XIX_век
0.0042  76      https://ru.wikipedia.org/wiki/Кремний
0.0040  32      https://ru.wikipedia.org/wiki/1781_год
0.0040  69      https://ru.wikipedia.org/wiki/Металлы
0.0040  77      https://ru.wikipedia.org/wiki/Металл
0.0040  70      https://ru.wikipedia.org/wiki/Минерал
0.0038  43      https://ru.wikipedia.org/wiki/1891_год
0.0035  92      https://ru.wikipedia.org/wiki/Атомные_бомбардировки_Хиросимы_и_Нагасаки
0.0029  34      https://ru.wikipedia.org/wiki/Правило_Тициуса_—_Боде
0.0029  72      https://ru.wikipedia.org/wiki/Оливин
0.0029  49      https://ru.wikipedia.org/wiki/Бразилия
0.0028  54      https://ru.wikipedia.org/wiki/Углеводород
0.0028  48      https://ru.wikipedia.org/wiki/Испания
0.0028  79      https://ru.wikipedia.org/wiki/Древнеримская_религия
0.0027  65      https://ru.wikipedia.org/wiki/Цвет
0.0024  55      https://ru.wikipedia.org/wiki/OSIRIS-REx
0.0014  61      https://ru.wikipedia.org/wiki/Семейство_астероидов
0.0013  2       https://ru.wikipedia.org/wiki/Созвездие
0.0011  94      https://ru.wikipedia.org/wiki/Царь-бомба
0.0009  42      https://ru.wikipedia.org/wiki/1945_год
--------------------
Total: 64 documents.
```