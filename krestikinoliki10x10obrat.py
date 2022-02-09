X='X'
O='0'
RAZMER_DOSKI=100
HODI=' '
NICHYA='Ничья'

def instrukciya():
    print('''
Привет! Это игра "Крестики-нолики".
Чтобы сделать ход, введи номер клетки,
куда хочешь поставить свой символ:

 0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9
-----------------------------------------------
10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19
-----------------------------------------------
20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29
-----------------------------------------------
30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39
-----------------------------------------------
40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49
-----------------------------------------------
50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59
-----------------------------------------------
60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69
-----------------------------------------------
70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79
-----------------------------------------------
80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89
-----------------------------------------------
90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99


''')
def nachalo(vopros):
    otvet=None
    while otvet not in ('да','нет'):
        otvet=input(vopros).lower()
    return otvet

def fishki():
    perviy_hod=nachalo("Вы хотите быть первым, кто сделает ход \
(да или нет)?  ")
    if perviy_hod=='да':
        print('Окей, ты играешь крестиками!')
        human=X
        comp=O
    else:
        print('ОК, я делаю первый ход крестиками')
        human=O
        comp=X
    return comp, human
        
def hod_number(low,high):
    otvet=None
    while otvet not in range(low,high):
        otvet=int(input("Делай свой ход - напиши номер поля (0-99): "))
    return otvet


def new_doska():
    doska=[]
    for i in range(RAZMER_DOSKI):
        doska.append(HODI)
    return doska

def pokaz_doski(doska):
    print('\n', doska[0], '|', doska[1], '|', doska[2], '|', doska[3], '|', doska[4], '|', doska[5], '|', doska[6], '|', doska[7], '|', doska[8], '|', doska[9])
    print('--------------------------------------')
    print('\n', doska[10], '|', doska[11], '|', doska [12], '|', doska[13], '|', doska[14], '|', doska[15], '|', doska[16], '|', doska[17], '|', doska[18], '|', doska[19])
    print('--------------------------------------')
    print('\n', doska[20], '|', doska[21], '|', doska [22], '|', doska[23], '|', doska[24], '|', doska[25], '|', doska[26], '|', doska[27], '|', doska[28], '|', doska[29])    
    print('--------------------------------------')
    print('\n', doska[30], '|', doska[31], '|', doska[32], '|', doska[33], '|', doska[34], '|', doska[35], '|', doska[36], '|', doska[37], '|', doska[38], '|', doska[39])
    print('--------------------------------------')
    print('\n', doska[40], '|', doska[41], '|', doska[42], '|', doska[43], '|', doska[44], '|', doska[45], '|', doska[46], '|', doska[47], '|', doska[48], '|', doska[49])
    print('--------------------------------------')
    print('\n', doska[50], '|', doska[51], '|', doska[52], '|', doska[53], '|', doska[54], '|', doska[55], '|', doska[56], '|', doska[57], '|', doska[58], '|', doska[59])
    print('--------------------------------------')
    print('\n', doska[60], '|', doska[61], '|', doska[62], '|', doska[63], '|', doska[64], '|', doska[65], '|', doska[66], '|', doska[67], '|', doska[68], '|', doska[69])
    print('--------------------------------------')
    print('\n', doska[70], '|', doska[71], '|', doska[72], '|', doska[73], '|', doska[74], '|', doska[75], '|', doska[76], '|', doska[77], '|', doska[78], '|', doska[79])
    print('--------------------------------------')
    print('\n', doska[80], '|', doska[81], '|', doska[82], '|', doska[83], '|', doska[84], '|', doska[85], '|', doska[86], '|', doska[87], '|', doska[88], '|', doska[89])
    print('--------------------------------------')
    print('\n', doska[90], '|', doska[91], '|', doska [92], '|', doska [93], '|', doska[94], '|', doska[95], '|', doska[96], '|', doska[97], '|', doska[98], '|', doska[99], '\n')

def dostupnie_hodi(doska):
    dostupnie_hodi=[]
    for i in range(RAZMER_DOSKI):
        if doska[i]== HODI:
            dostupnie_hodi.append(i)
    return dostupnie_hodi

def winner(doska):
    VAR_POBED=((0,1,2,3,4), (1,2,3,4,5), (2,3,4,5,6), (3,4,5,6,7), (4,5,6,7,8), (5,6,7,8,9),
               (10,11,12,13,14), (11,12,13,14,15), (12,13,14,15,16), (13,14,15,16,17), (14,15,16,17,18), (15,16,17,18,19),
               (20,21,22,23,24), (21,22,23,24,25), (22,23,24,25,26), (23,24,25,26,27), (24,25,26,27,28), (25,26,27,28,29),
               (30,31,32,33,34), (31,32,33,34,35), (32,33,34,35,36), (33,34,35,36,37), (34,35,36,37,38), (35,36,37,38,39),
               (40,41,42,43,44), (41,42,43,44,45), (42,43,44,45,46), (43,44,45,46,47), (44,45,46,47,48), (45,46,47,48,49),
               (50,51,52,53,54), (51,52,53,54,55), (52,53,54,55,56), (53,54,55,56,57), (54,55,56,57,58), (55,56,57,58,59),
               (60,61,62,63,64), (61,62,63,64,65), (62,63,64,65,66), (63,64,65,66,67), (64,65,66,67,68), (65,66,67,68,69),
               (70,71,72,73,74), (71,72,73,74,75), (72,73,74,75,76), (73,74,75,76,77), (74,75,76,77,78), (75,76,77,78,79),
               (80,81,82,83,84), (81,82,83,84,85), (82,83,84,85,86), (83,84,85,86,87), (84,85,86,87,88), (85,86,87,88,89),
               (90,91,92,93,94), (91,92,93,94,95), (92,93,94,95,96), (93,94,95,96,97), (94,95,96,97,98), (95,96,97,98,99),
               (0,11,22,33,44), (1,12,23,34,45), (2,13,24,35,46), (3,14,25,36,47), (4,15,26,37,48), (5,16,27,38,49),
               (10,21,32,43,54), (11,22,33,44,55), (12,23,34,45,56), (13,24,35,46,57), (14,25,36,47,58), (15,26,37,48,59),
               (20,31,42,53,64), (21,32,43,54,65), (22,33,44,55,66), (23,34,45,56,67), (24,35,46,57,68), (25,36,47,58,69),                
               (30,41,52,63,74), (31,42,53,64,75), (32,43,54,65,76), (33,44,55,66,77), (34,45,56,67,78), (35,46,57,68,79),
               (40,51,62,73,84), (41,52,63,74,85), (42,53,64,75,86), (43,54,65,76,87), (44,55,66,77,88), (45,56,67,78,89),
               (50,61,72,83,94), (51,62,73,84,95), (52,63,74,85,96), (53,64,75,86,97), (54,65,76,87,98), (55,66,77,88,99),
               (9,18,27,36,45), (8,17,26,35,44), (7,16,25,34,43), (6,15,24,33,42), (5,14,23,32,41), (4,13,22,31,40),
               (19,28,37,46,55), (18,27,36,45,54), (17,26,35,44,53), (16,25,34,43,52), (15,24,33,42,51), (14,23,32,41,50),
               (29,38,47,56,65), (28,37,46,55,64), (27,36,45,54,63), (26,35,44,53,62), (25,34,43,52,61), (24,33,42,51,60),
               (39,48,57,66,75), (38,47,56,65,74), (37,46,55,64,73), (36,45,54,63,72), (35,44,53,62,71), (34,43,52,61,70),
               (49,58,67,76,85), (48,57,66,75,84), (47,56,65,74,83), (46,55,64,73,82), (45,54,63,72,81), (44,53,62,71,80),
               (59,68,77,86,95), (58,67,76,85,94), (57,66,75,84,93), (56,65,74,83,92), (55,64,73,82,91), (54,63,72,81,90),
               (0,10,20,30,40), (1,11,21,31,41), (2,12,22,32,42), (3,13,23,33,43), (4,14,24,34,44), 
               (5,15,25,35,45), (6,16,26,36,46), (7,17,27,37,47), (8,18,28,38,48), (9,19,29,39,49), 
               (10,20,30,40,50), (11,21,31,41,51), (12,22,32,42,52), (13,23,33,43,53), (14,24,34,44,54), 
               (15,25,35,45,55), (16,26,36,46,56), (17,27,37,47,57), (18,28,38,48,58), (19,29,39,49,59), 
               (20,30,40,50,60), (21,31,41,51,61), (22,32,42,52,62), (23,33,43,53,63), (24,34,44,54,64), 
               (25,35,45,55,65), (26,36,46,56,66), (27,37,47,57,67), (28,38,48,58,68), (29,39,49,59,69), 
               (30,40,50,60,70), (31,41,51,61,71), (32,42,52,62,72), (33,43,53,63,73), (34,44,54,64,74), 
               (35,45,55,65,75), (36,46,56,66,76), (37,47,57,67,77), (38,48,58,68,78), (39,49,59,69,79), 
               (40,50,60,70,80), (41,51,61,71,81), (42,52,62,72,82), (43,53,63,73,83), (44,54,64,74,84), 
               (45,55,65,75,85), (46,56,66,76,86), (47,57,67,77,87), (48,58,68,78,88), (49,59,69,79,89), 
               (50,60,70,80,90), (51,61,71,81,91), (52,62,72,82,92), (53,63,73,83,93), (54,64,74,84,94), 
               (55,65,75,85,95), (56,66,76,86,96), (57,67,77,87,97), (58,68,78,88,98), (59,69,79,89,99)
               )
    for i in VAR_POBED:
        if doska[i[0]]==doska[i[1]]==doska[i[2]]==doska[i[3]]==doska[i[4]]!=HODI:
            winner=doska[i[0]]
            return winner
        if HODI not in doska:
            return NICHYA
    return None
def human_hod(doska,human):
    dostupnie=dostupnie_hodi(doska)
    hod=None
    while hod not in dostupnie:
        hod=hod_number(0,RAZMER_DOSKI)
        if hod not in dostupnie:
            print('Поле занято. Напиши другой номер: ')
    print('Супер!')
    return hod
def comp_hod(doska,comp,human):
    doska=doska[:]
    
    print('Мой ход: ')
    for i in dostupnie_hodi(doska):
        doska[i]=comp
        if winner(doska)!=comp:
            print(i)
            return i
        doska[i]=HODI
    for k in dostupnie_hodi(doska):
        print(k)
        return k
def next_ochered(ochered):
    if ochered==X:
        return O
    else:
        return X
def pozdrav_pobeditela(pobeditel,comp,human):
    if pobeditel!=NICHYA:
        print('Собрана линия ', pobeditel)
    else:
        print(NICHYA)
    if pobeditel==comp:
        print('Ты победил!')
    elif pobeditel==human:
        print('Компьютер выиграл!')
    elif pobeditel==NICHYA:
        print(NICHYA)
def main():
    instrukciya()
    comp,human=fishki()
    ochered=X
    doska=new_doska()
    pokaz_doski(doska)
    while not winner(doska):
        if ochered==human:
            hod=human_hod(doska,human)
            doska[hod]=human
        else:
            hod=comp_hod(doska,comp,human)
            doska[hod]=comp
        pokaz_doski(doska)
        ochered=next_ochered(ochered)
    pobeditel=winner(doska)
    pozdrav_pobeditela(pobeditel,comp,human)

main()
input('\n Нажми Entr, чтобы выйти')