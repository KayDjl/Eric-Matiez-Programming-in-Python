guests = ['Jorik', 'Sema', 'Kay', 'Gerda', 'yeper']
print(f"Hello my favorite cat, сome to my place for lunch {guests[0]}. I am very you love, my small boy")
print(f"Hey my favourite, come to my place for lunch {guests[1]}. I miss you so much, i love you my boy")
print(f"Hello my sweet, come to my place for lunch {guests[2]}, I hope you and I won't break up. I can't handle it.")
print(f"Hey my small gerl, come to my place for lunch {guests[3]}, I hope you and I won't break up. I can't handle it.")

guests_poped = guests.pop(4)
print(guests_poped.title())

guests.append('Poti')
print(guests)

guests.insert(4, 'Tati')
guests.insert(5, 'Pati')
guests.insert(6, 'Eati')

print(guests)
guests.pop(4)
guests.pop(5)
print(guests)
guests.pop(4)
guests.pop(4)
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)
