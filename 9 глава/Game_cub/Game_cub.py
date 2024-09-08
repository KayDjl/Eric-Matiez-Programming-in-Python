
from random import randint
from di import Die

my_cub = Die()
for _ in range(10):
    print(f"{my_cub.roll_die()}")
    
my_cub.set_roll_die(10)
print("\n")
for _ in range(10):
    print(f"{my_cub.roll_die()}")
    
my_cub.set_roll_die(20)
print("\n")
for _ in range(10):
    print(f"{my_cub.roll_die()}")
    
