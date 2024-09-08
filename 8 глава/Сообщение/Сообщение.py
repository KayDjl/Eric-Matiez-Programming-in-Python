def display_message():
    print("В данной теме будут расматриватся функции и их параметры,\n"
          "функции служат блоком кода, который может выполнять одно\n"
          "и то же действие при каждом вызове функции")
display_message()

def favorite_book(title):
    print(f"One my favorite book is {title.title()}")
    
favorite_book('атомные привычки')