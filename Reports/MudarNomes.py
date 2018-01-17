File = open("Reports\junit.xml","r")
textodoficheiro = File.read()
print(textodoficheiro)
posicaodeclassname= textodoficheiro.find('classname') 
print(posicaodeclassname)
print(textodoficheiro.index('classname') )

print(textodoficheiro[:posicaodeclassname+11])

posicaodaultimaaspa = textodoficheiro.find("\"",posicaodeclassname+11)
print(textodoficheiro.find("\"",posicaodeclassname+11))


print(textodoficheiro[posicaodaultimaaspa:])


textofinal=textodoficheiro[:posicaodeclassname+11] + "TROLOLOL" + textodoficheiro[posicaodaultimaaspa:]

with open('junit.xml', 'w') as f:
    f.write(textofinal)
