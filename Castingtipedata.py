#Casting
#merubah dari satu tipe ke tipe data yang lain
#tipe data=interger(int),float(float),string(str),boolean(bool)
print("====INTERGER====")
data_int=10
print("data :" , data_int , ", type :" , type(data_int))
data_float=float(data_int)
data_str  =str(data_int)
data_bool =bool(data_int) #akan false jika nilai interger=0
print("data :", data_float, " ,type :", type(data_float))
print("data :", data_str, "   ,type :", type(data_str))
print("data :", data_bool, "  ,type :", type(data_bool))

print("====FLOAT====")
data_float=3.5
print("data :" , data_float , ", type :" , type(data_float))
data_int =int(data_float)
data_str =str(data_float)
data_bool=bool(data_float) #akan false jika nilai Float=0
print("data :", data_int, "  ,type :", type(data_int))
print("data :", data_str, "  ,type :", type(data_str))
print("data :", data_bool, " ,type :", type(data_bool))

print("====STRING====")
data_str="20";
print("data :" , data_str , ",type :" ,   type(data_str))
data_int  =int  (data_str) #string harus diisi dengan angka
data_float=float(data_str) #string haerus diisi dengan angka
data_bool =bool (data_str) #akan false jika string kosong
print("data :", data_int, "  ,type :",    type(data_int))
print("data :", data_float, ",type :",    type(data_float))
print("data :", data_bool, " ,type :",    type(data_bool))

print("====BOOL====")
data_bool=True
print("data :" , data_bool , ", type :" , type(data_bool))
data_int  =int(data_bool)
data_str  =str(data_bool)
data_float=float(data_bool) #akan false jika nilai bool=false
print("data :", data_int, "    ,type :", type(data_int))
print("data :", data_str, "    ,type :", type(data_str))
print("data :", data_float, "  ,type :", type(data_float))
