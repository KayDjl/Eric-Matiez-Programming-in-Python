def sandwich(*args):
    print("Сендвичи:")
    for sen in args:
        print(f"- {sen}")
    print("\n")
        
sandwich('Курица')
sandwich('Телятина', 'Свинина')
sandwich('Баранина', 'Бобрятина', 'Оленина')
