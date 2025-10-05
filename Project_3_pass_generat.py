import random
import string

print("\n            PASSWORD GENERATOR           \n")

len=int(input("Enter password length: "))


up=string.ascii_uppercase
down=string.ascii_lowercase
num=string.digits
punc=string.punctuation

str=up+num+punc+down

pwd=random.sample(str,len)
password="".join(pwd)
print(password)

