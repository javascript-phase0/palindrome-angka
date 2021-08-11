angka = 175
angka_new = str(angka)

#Versi bahasa lain menggunakan python
# while True:
#     if(len(angka_new) <= 1):
#         print(False)
#         break
#     angka +=1
#     angka_new = str(angka)
#     l = ""
#     for j in range(len(angka_new)-1,-1,-1):
#         l += angka_new[j]
#     if(l == angka_new):
#         break
# print(angka_new)

#versi python
if(angka_new[::-1] == angka_new):
    print("This is palindrome")
else:
    while True:
        angka +=1
        angka_new = str(angka)
        if(angka_new[::-1] == angka_new):
            break
print(angka_new)  
            