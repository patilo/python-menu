sueldo=int(input("ingrese su sueldo:"))
s1=(sueldo*0.1)
s2=(sueldo*0.05)
s3=(sueldo*0.03)
if sueldo<1000 :
    sf1=(sueldo-s1)
    print(f"tu sueldo es: {sueldo}, y descuento de: {s1}")
    print("tu sueldo final es de: ",sf1)
elif sueldo>1000 and sueldo<2000:
    sf2=(sueldo-s2)
    print(f"tu sueldo es : {sueldo},y descuento de:{s2}")
    print("tu sueldo final es de:",sf2)
elif sueldo>=2000:
    sf3=(sueldo-s3)
    print(f"tu sueldo es : {sueldo}, y descuento de:{s3}")
    print("tu sueldo final es de:",sf3)
else:
    print("ingrese un sueldo correcto")
