def lists_name(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
nums = ['Sergey', 'Lika', 'kay', 'gErda']
lists_name(nums)


def full_print(lod_print, com_print):
    while lod_print:
        currend_print = lod_print.pop()
        print(f"Печать эскиза: {currend_print}")
        com_print.append(currend_print)
        

def full_completed(com_print):
    for co_print in com_print:
        print(co_print)
    
lod_print = ['1', '2', '3']
com_print = []

full_print(lod_print[:], com_print)
full_completed(com_print)