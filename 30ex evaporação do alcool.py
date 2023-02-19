


#30. Elabore um programa que verifique a evaporação do álcool (78,37ºC) na destilaria. Leia a
#temperatura do álcool. Em seguida verifique:
#Se temperatura for de 0 a 75°, imprima “a temperatura está baixa”.
#Se a temperatura estiver entre 75 e 88, imprima “a temperatura está ideal”.
#De 85 até 100, imprima “passou do ponto”.


Temperatura = float(input("Qual a Temperatura: "))

if Temperatura <=75:  
        print ("a temperatura está baixa\n")
elif Temperatura <=88:
    print ("a temperatura está ideal\n")
elif Temperatura <=10000:
    print ("passou do ponto\n")