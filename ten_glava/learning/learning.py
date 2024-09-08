absolut_path = "../text_file/learning_python.txt"
with open(absolut_path, encoding = 'utf-8') as file:
    contecst = file.read()
print(contecst)
print("\n")


with open(absolut_path, encoding = 'utf-8') as file1:
    for line in file1:
        print(line.rstrip())
print("\n")

with open(absolut_path, encoding = 'utf-8') as file2:
    contecst = file2.readlines()
folder = ''
for lines in contecst:
    folder += lines.rstrip()
folder = folder.replace("Python", "C")
print(folder)
