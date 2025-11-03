#operasi aritmatika 

a=10
b=3

#pemnjumlahan ( + )
hasil= a + b 
print( a, "+" ,b, "=", hasil)

#pengurangan ( - )
hasil= a - b
print( a," - ",b,"=",hasil)

#perkalian ( * )
hasil = a * b 
print(a," * ",b,"=",hasil)

#pembagian ( / )
hasil = a / b
print(a," / ",b," = ", hasil)

#eskponen (pangkat) ( ** )
hasil = a ** b
print(a, "**",b, "=",hasil)

#madulus(sisa bagi) ( % )
hasil = a % b
print(a,"% ",b,"=",hasil)

#floor divusion (pembagian dibulatkan ke bawah) ( // )
hasil = a // b
print(a, "//", b, "=", hasil)

#prioritas operasi.operasional precedence  "()"
x=3
y=2
z=4
#kalau di prioritaskan
hasil= x ** y + z / y // z * (x + y)
print(x,"**",y,'+',z,'/',y,'//',z,'*','(',x,'+',y,')','=',hasil)

hasil= (x+y)*z
print('(',x,'+',y,')*',z,'=' , hasil)
print("----------------------------")
#kalau tidak di prioritaskan
hasil= x ** y + z / y // z * x + y
print(x,"**",y,'+',z,'/',y,'//',z,'*',x,'+',y,'=',hasil )

hasil= x+y*z
print(x,"+",y,'*',z,'=' ,hasil)


