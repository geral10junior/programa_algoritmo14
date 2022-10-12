#Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
hora1, hora2 = input().split(" ")
hora1 = int(hora1)
hora2 = int(hora2)
if hora1 < hora2:
    x= hora2 - hora1
    print("O JOGO DUROU",x,"HORA(S)")
elif hora1 > hora2:
    y= 24 - hora1 + hora2
    print("O JOGO DUROU",y,"HORA(S)")
elif hora1==hora2:
    print("O JOGO DUROU 24 HORA(S)")
