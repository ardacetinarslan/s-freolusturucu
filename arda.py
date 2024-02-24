import random
sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("sifreniz ne kadar uzun olsun?:"))
sonuç =  ""
for i in range(uzunluk):
    sonuç += random.choice(sifre)

print(sonuç)
