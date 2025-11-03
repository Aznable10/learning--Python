print("\nFahrenheit ke kelvin\n")

fahrenheit = float(input("masukkan suhu ke dalam fahrenheit = "))
print("suhu adalah ",fahrenheit, "fahrenheit")
kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam kelvin adalah ",kelvin, "kelvin")

print("\nkelvin ke fahrenheit\n")

kelvin=float(input("masukkan suhu ke dalam kelvin = "))
print("suhu adalah ",kelvin, "kelvin")
fahrenheit = (9/5) * (kelvin - 273) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "fahrenheit")