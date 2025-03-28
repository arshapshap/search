# Задание 5

Пример векторного поиска по таблицам из [4-го задания](https://drive.google.com/drive/u/0/folders/1QebVj3CNpLLcuBk4AFLOePWrNmpJ-WlC) и с использованием индекса из [1-го задания](https://drive.google.com/drive/u/0/folders/1K6z3IutgJiTFi8bsJlXVCGZ6BFR6BPuo):

```
>>> python3 index.py ../task4/ ../task1/index.txt
Vector search engine ready

Search query (or 'exit'): космос
Found documents:
score: 0.0502   86      https://ru.wikipedia.org/wiki/Пояс_Койпера
score: 0.0493   45      https://ru.wikipedia.org/wiki/Астрофотография
score: 0.0425   91      https://ru.wikipedia.org/wiki/Земля
score: 0.0378   23      https://ru.wikipedia.org/wiki/Телескоп
score: 0.0363   90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
score: 0.0214   29      https://ru.wikipedia.org/wiki/Юпитер
score: 0.0203   30      https://ru.wikipedia.org/wiki/(2)_Паллада
score: 0.0192   16      https://ru.wikipedia.org/wiki/Солнечная_система
score: 0.0186   17      https://ru.wikipedia.org/wiki/Солнце
score: 0.0170   27      https://ru.wikipedia.org/wiki/Пояс_астероидов
score: 0.0150   18      https://ru.wikipedia.org/wiki/Планета
score: 0.0139   35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
score: 0.0133   37      https://ru.wikipedia.org/wiki/Астрономическая_единица
score: 0.0131   83      https://ru.wikipedia.org/wiki/Меркурий
score: 0.0110   7       https://ru.wikipedia.org/wiki/(433)_Эрос
score: 0.0106   50      https://ru.wikipedia.org/wiki/Лёд
score: 0.0103   28      https://ru.wikipedia.org/wiki/Марс
score: 0.0102   13      https://ru.wikipedia.org/wiki/Луна
score: 0.0073   24      https://ru.wikipedia.org/wiki/Звезда
score: 0.0073   33      https://ru.wikipedia.org/wiki/Уран_(планета)
score: 0.0062   52      https://ru.wikipedia.org/wiki/Комета
score: 0.0049   46      https://ru.wikipedia.org/wiki/2010_год
score: 0.0039   80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
score: 0.0031   93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
score: 0.0021   22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
Total: 25 documents.

Search query (or 'exit'): космос птица
Found documents:
score: 0.0253   91      https://ru.wikipedia.org/wiki/Земля
score: 0.0241   86      https://ru.wikipedia.org/wiki/Пояс_Койпера
score: 0.0239   2       https://ru.wikipedia.org/wiki/Созвездие
score: 0.0237   45      https://ru.wikipedia.org/wiki/Астрофотография
score: 0.0182   23      https://ru.wikipedia.org/wiki/Телескоп
score: 0.0182   57      https://ru.wikipedia.org/wiki/(101955)_Бенну
score: 0.0175   90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
score: 0.0143   80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
score: 0.0103   29      https://ru.wikipedia.org/wiki/Юпитер
score: 0.0098   30      https://ru.wikipedia.org/wiki/(2)_Паллада
score: 0.0092   16      https://ru.wikipedia.org/wiki/Солнечная_система
score: 0.0090   17      https://ru.wikipedia.org/wiki/Солнце
score: 0.0082   27      https://ru.wikipedia.org/wiki/Пояс_астероидов
score: 0.0072   18      https://ru.wikipedia.org/wiki/Планета
score: 0.0067   35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
score: 0.0064   37      https://ru.wikipedia.org/wiki/Астрономическая_единица
score: 0.0063   83      https://ru.wikipedia.org/wiki/Меркурий
score: 0.0053   7       https://ru.wikipedia.org/wiki/(433)_Эрос
score: 0.0051   65      https://ru.wikipedia.org/wiki/Цвет
score: 0.0051   50      https://ru.wikipedia.org/wiki/Лёд
score: 0.0049   28      https://ru.wikipedia.org/wiki/Марс
score: 0.0049   13      https://ru.wikipedia.org/wiki/Луна
score: 0.0045   92      https://ru.wikipedia.org/wiki/Атомные_бомбардировки_Хиросимы_и_Нагасаки
score: 0.0041   47      https://ru.wikipedia.org/wiki/США
score: 0.0035   24      https://ru.wikipedia.org/wiki/Звезда
score: 0.0035   33      https://ru.wikipedia.org/wiki/Уран_(планета)
score: 0.0033   49      https://ru.wikipedia.org/wiki/Бразилия
score: 0.0030   52      https://ru.wikipedia.org/wiki/Комета
score: 0.0024   46      https://ru.wikipedia.org/wiki/2010_год
score: 0.0015   93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
score: 0.0010   22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
Total: 31 documents.

Search query (or 'exit'): космос птица река
Found documents:
score: 0.0267   2       https://ru.wikipedia.org/wiki/Созвездие
score: 0.0256   91      https://ru.wikipedia.org/wiki/Земля
score: 0.0239   93      https://ru.wikipedia.org/wiki/Тунгусский_метеорит
score: 0.0211   49      https://ru.wikipedia.org/wiki/Бразилия
score: 0.0209   86      https://ru.wikipedia.org/wiki/Пояс_Койпера
score: 0.0206   45      https://ru.wikipedia.org/wiki/Астрофотография
score: 0.0158   23      https://ru.wikipedia.org/wiki/Телескоп
score: 0.0158   57      https://ru.wikipedia.org/wiki/(101955)_Бенну
score: 0.0152   90      https://ru.wikipedia.org/wiki/Защита_от_астероидов
score: 0.0147   80      https://ru.wikipedia.org/wiki/Древнегреческая_мифология
score: 0.0125   28      https://ru.wikipedia.org/wiki/Марс
score: 0.0113   47      https://ru.wikipedia.org/wiki/США
score: 0.0092   40      https://ru.wikipedia.org/wiki/1807_год
score: 0.0089   29      https://ru.wikipedia.org/wiki/Юпитер
score: 0.0085   30      https://ru.wikipedia.org/wiki/(2)_Паллада
score: 0.0080   16      https://ru.wikipedia.org/wiki/Солнечная_система
score: 0.0078   17      https://ru.wikipedia.org/wiki/Солнце
score: 0.0076   50      https://ru.wikipedia.org/wiki/Лёд
score: 0.0072   92      https://ru.wikipedia.org/wiki/Атомные_бомбардировки_Хиросимы_и_Нагасаки
score: 0.0071   27      https://ru.wikipedia.org/wiki/Пояс_астероидов
score: 0.0063   87      https://ru.wikipedia.org/wiki/Импактное_событие
score: 0.0063   13      https://ru.wikipedia.org/wiki/Луна
score: 0.0063   18      https://ru.wikipedia.org/wiki/Планета
score: 0.0059   39      https://ru.wikipedia.org/wiki/1801_год
score: 0.0059   4       https://ru.wikipedia.org/wiki/(21)_Лютеция
score: 0.0058   35      https://ru.wikipedia.org/wiki/Цах,_Франц_Ксавер_фон
score: 0.0055   37      https://ru.wikipedia.org/wiki/Астрономическая_единица
score: 0.0055   83      https://ru.wikipedia.org/wiki/Меркурий
score: 0.0046   7       https://ru.wikipedia.org/wiki/(433)_Эрос
score: 0.0044   65      https://ru.wikipedia.org/wiki/Цвет
score: 0.0043   42      https://ru.wikipedia.org/wiki/1945_год
score: 0.0043   48      https://ru.wikipedia.org/wiki/Испания
score: 0.0033   79      https://ru.wikipedia.org/wiki/Древнеримская_религия
score: 0.0031   24      https://ru.wikipedia.org/wiki/Звезда
score: 0.0031   33      https://ru.wikipedia.org/wiki/Уран_(планета)
score: 0.0026   52      https://ru.wikipedia.org/wiki/Комета
score: 0.0022   67      https://ru.wikipedia.org/wiki/Углерод
score: 0.0021   46      https://ru.wikipedia.org/wiki/2010_год
score: 0.0015   22      https://ru.wikipedia.org/wiki/Гершель,_Уильям
Total: 39 documents.
```