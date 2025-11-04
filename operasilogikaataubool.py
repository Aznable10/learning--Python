#operasi logika dan boolean


# not,or,and,xor
print("==========NOT========== ") #kebalikan data awal/variabel pertama
a = False
b = not a
print("a =", a)
print("------------NOT")
print("b =", b)


print("==========OR========== ") #jika salah satu true maka hasilnya true
a = False
b = False
c = a or b
print(a, 'OR',b, '=' ,c)
a = True
b = False
c = a or b
print(a, 'OR',b, '=' ,c)
a = False
b = True
c = a or b
print(a, 'OR',b, '=' ,c)
a = True
b = True
c = a or b
print(a, 'OR',b, '=' ,c)

print("==========AND========== ") #jika salah satu false maka hasilnya false
a = True
b = True
c = a and b
print(a, 'and',b, '=' ,c)
a = True
b = False
c = a and b
print(a, 'and',b, '=' ,c)
a = False
b = True
c = a and b
print(a, 'and',b, '=' ,c)
a = False
b = False
c = a and b
print(a, 'and',b, '=' ,c)

print("==========XOR========== ") #jika true nya ganjil true , kalau true nya genap false 
a = True
b = True
c = a ^ b
print(a, 'XOR',b, '=' ,c)
a = True
b = False
c = a ^ b
print(a, 'XOR',b, '=' ,c)
a = False
b = True
c = a ^ b
print(a, 'XOR',b, '=' ,c)
a = False
b = False
d = True
c = a ^ b ^ d
print(a, 'XOR',b, 'XOR',c,' =',c)
a = False
b = False
d = False
c = a ^ b ^ d
print(a, 'XOR',b, 'XOR',d,' =',c)
a = True
b = True
c = True
d = True
e = True
f= a ^ b ^ c ^ d ^ e 
print(a, 'XOR',b, 'XOR',c,'XOR',d,'XOR',e, '=',f)