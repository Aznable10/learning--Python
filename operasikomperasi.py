#operasi komparasi

#setiap hasil dari komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#lebih besar dari >
print("========== lebih besar dari > ==========")
print("a > 2 = ", a > b)
print("b > 2 = ", b > 2)
print("b > 4 = ", b > a)

#kurang dari <
print("========== kurang dari < ==========")
print("a < 2 = ", a < b)
print("b < 2 = ", b < 2)
print("b < 4 = ", b < a)

#lebih besar sama dengan >=
print("========== lebih besar sama dengan >= ==========")
print("a >= 2 = ", a >= b)
print("b >= 2 = ", b >= 2)
print("b >= 4 = ", b >= a)

#kurang dari sama dengan <=
print("========== kurang dari sama dengan <= ==========")
print("a <= 2 = ", a <= b)
print("b <= 2 = ", b <= 2)
print("b <= 4 = ", b <= a)

#sama dengan ==
print("========== sama dengan == ==========") 
print("a == 2 = ", a == b)
print("b == 2 = ", b == 2)
print("b == 4 = ", b == a)  
print("a == 4 = ", a == 4)

#tidak sama dengan !=
print("========== tidak sama dengan != ==========")
print("a != 2 = ", a != b)
print("b != 2 = ", b != 2)
print("b != 4 = ", b != a)
print("a != 4 = ", a != 4)

# 'is' sebagai komparasi object  identity
print("========== is (object identity) ==========")
x = 5   #ini berdua adalah assignment untuk  membuat objek 
y = 5
print('nilai x =',x,', id =', hex(id(x)))
print('nilai y =',y,', id =', hex(id(y)))
hasil = x is y
print('x is y =',hasil)

#is not (untuk membandingkan object identity)
print("========== is not (object identity) ==========")
x=5
y=6
print('nilai x =',x,', id =', hex(id(x)))
print('nilai y =',y,', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)