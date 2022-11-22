import random
import string

def generate_unit_code():
    L=[]
    for _ in range(4):
        if len(L) < 4:
            random.shuffle(string.digits.split())
            L.append(random.choice(string.digits))
            
    return "".join(L)


print(generate_unit_code())
