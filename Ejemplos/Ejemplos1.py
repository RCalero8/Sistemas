x,y,z = 10,20,30
print(x)
print(y)
print(z)

#Imprimir textos
text1 = 'abc\ndef' #Salto de linea
print(text1)

text1_1 = r'abc\ndef' #Al poner la r(remove) delante le da igual el salto de linea
print(text1_1)

text2 = 'a\tb\tc' #Tabula el texto
print(text2)

text2_1 = r'a\tb\tc' #Al poner la r(remove) delante le da igual el tabulador de texto
print(text2_1)

#Mas sobre print()
msg1 = '¿Sabes por qué estoy acá?'
msg2 = 'Porque me apasiona'

print(msg1, msg2)
print(msg1, msg2, sep='|')
print(msg2, end='!!')