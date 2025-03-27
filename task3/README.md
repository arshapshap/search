Пример результата поиска по документам из [2-го задания](https://drive.google.com/drive/u/0/folders/1U4hL69VzJtFlG1u5Sl9or6gpd9_NkTO7):

```
>>> python3 index.py ../task2/docs
Inverted index saved to inverted_index.txt

Query examples:
apple & banana | !orange
(linux | windows) & !error
network & security | firewall

Enter query (or 'exit' to quit): космос & солнце | человек
Found 54 documents:
13 14 16 17 18 2 20 22 23 24 25 27 28 29 30 31 33 35 36 37 39 40 41 42 44 46 47 48 49 5 50 52 53 58 65 67 69 7 70 71 73 76 77 79 80 83 84 86 87 9 90 91 92 93

Enter query (or 'exit' to quit): космос | солнце | человек
Found 84 documents:
1 10 100 11 12 13 14 15 16 17 18 19 2 20 22 23 24 25 27 28 29 3 30 31 33 34 35 36 37 39 4 40 41 42 44 45 46 47 48 49 5 50 51 52 53 55 57 58 6 60 62 63 65 66 67 69 7 70 71 73 74 76 77 78 79 8 80 81 82 83 84 85 86 87 9 90 91 92 93 95 96 97 98 99

Enter query (or 'exit' to quit): космос & солнце & человек
Found 20 documents:
13 16 17 18 22 24 27 28 29 33 35 37 52 7 80 83 86 90 91 93

Enter query (or 'exit' to quit): космос & !солнце | !человек
Found 50 documents:
1 10 100 11 12 15 19 21 23 26 3 30 32 34 38 4 43 45 46 50 51 54 55 56 57 59 6 60 61 62 63 64 66 68 72 74 75 78 8 81 82 85 88 89 94 95 96 97 98 99

Enter query (or 'exit' to quit): космос | !солнце | !человек
Found 89 documents:
1 10 100 11 12 13 15 16 17 18 19 20 21 22 23 24 26 27 28 29 3 30 32 33 34 35 36 37 38 39 4 40 41 42 43 44 45 46 47 49 50 51 52 53 54 55 56 57 59 6 60 61 62 63 64 65 66 68 69 7 70 72 73 74 75 76 77 78 8 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
```

### [Google Drive](https://drive.google.com/drive/u/0/folders/1-ZFaIF2hOmc875qyMZVIqg_sTwcRAVEo)