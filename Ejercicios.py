"EJERCISIO 19"

cadena=input("Escriba cadena: ")			
# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
lista=cadena.split(" ")
for palabra in lista:
	print (palabra[0],)
print ("")
# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
for palabra in lista:
    print (palabra.capitalize(),)
print ("")			
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print (palabra,)


"EJERCISIO 21"

cadena=input("Ingrese el número binario: ")		
cont=0
decimal=0
for num in cadena[::-1]:
    if num=="1":
        decimal=decimal+(2**cont)
    cont=cont+1
print (decimal)
