#conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imtáveis e primitivos
#str, int, float, bool

'''print(1 + 1)
print('a' + 'b') #Aqui aconteceu um concatenação por ser duas strings'''

#Aqui não será concatenado, pois só é psossivel concatenar uma string com outra string

#print('1' + 1) 
print(int('1'), type('1')) 

print(int('1'), type(int('1'))) #Convertendo a str '1' em um tipo int

#Asim eu consigo fazer a soma de uma string com um inteiro
print(int('1') +1)
print(float('1') +1) #covertendo para float
print(bool('  ')) #Convertendo ums str para bool

print(str(11) +'b') #convertendo um int para str
