from db import add_user, get_user_all, get_to_age
from random import randint, choice

gl = "оуеияа"
sg = "цкншщглдпрв"
name = ''
for i in range(3):
    name+= choice(gl)
    name+=choice(sg)

x = randint(14, 90)
balance = randint(0, 1000)
age = randint(14, 90)


print(get_to_age(140))