import csv
import os

#Preparation
catalog = []
with open(r"C:\Users\Lena\Desktop\Программирование на Питон\LW2\books-en.csv") as books_file:
    next(books_file)
    books_reader = csv.reader(books_file, delimiter=';')
    for book in books_reader:
        catalog.append(book)    

#ISBN;Book-Title;Book-Author;Year-Of-Publication;Publisher;Downloads;Price
#task_1: Название > 30 символов
print("Task_1")
ans_1 = 0
for book in catalog:
    if len(book[1]) > 30: 
        ans_1 += 1
print("The number of records where the string in the\
       Name field is longer than 30 characters:", ans_1, end='\n\n')

#task_2: Поиск книг по автору. 
print("Task_2", "Please enter the author’s name:", sep='\n')
search_author = input()
not_found = 1
ans_2 = []
for book in catalog:
    if float(book[6].replace(',','.')) >= 150 and book[2] == search_author:
        not_found = 0
        ans_2.append(book)
if not_found:
    print("There are no results for your query.")
else:
    print("Based on your request, the following was found:")
    for book in ans_2:
        print(*book)
print()

#task_3 
print("Task_3")
with open("ans_3.txt", "w", encoding="utf-8") as ans_3:
    for i, book in enumerate(catalog[:20], start=1):
        author = book[2]
        title = book[1]
        year = book[3]
        ans_3.write(f"{i}. {author}. {title} - {year}"+'\n')
print("Done")
print("The file will be saved here:", os.getcwd(), end='\n\n')

#add_task_1 перечень издательств без повторений
print("Additional_task_1", "All publishers:", end='\n')
ans_add_1 = []
for book in catalog:
    if not book[4] in ans_add_1: ans_add_1.append(book[4])
ans_add_1.sort()
for publisher in ans_add_1:
    print(publisher)
print()

#add_task_2 the most popular books
print("Additional_task_2", "The most popular books:", sep='\'n')
catalog.sort(key = lambda x: - int(x[5]))
for i, book in enumerate(catalog[:20],start=1):
    print(f"{i})", *book)
