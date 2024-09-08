path = "../text_file/programming.txt"
with open(path, 'w') as file:
    file.write('Hello, i love programming.\n')
    
with open(path, 'a') as file:
    file.write('I am live in Russia')
    
