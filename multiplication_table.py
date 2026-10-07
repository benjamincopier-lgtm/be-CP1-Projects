#benjamin copier

numbmultipier=0
for numb1 in range(1, 13):
    numbmultipier+=1
    for numb1 in range(numbmultipier, 13 * numbmultipier, numbmultipier):
        print(numb1, end = "\t" )