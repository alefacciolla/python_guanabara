#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

 #           (decametro)  
#    km    hm    dam    M    dm    cm    mm
#
# 0.001   0.01   0.1    1    10   100   1000 
medida = float(input('uma distância em metros: '))
cm = medida*100
mm = medida*1000
print('a medida de {}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida,cm,mm))