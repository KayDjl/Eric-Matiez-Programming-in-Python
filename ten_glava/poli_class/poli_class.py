f_absolyt = '../text_file/poli.txt'
try:
    with open(f_absolyt, encoding = 'utf-8') as f:
        con = f.read()
except FileNotFoundError:
    print(f"Неверный путь к {f_absolyt}")
else:
    split_file = con.split()
    lens = len(split_file)
    print(f"В файле poli.txt содержится {lens} слов")
