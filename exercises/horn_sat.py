# -> znalezc pojedyncze
# -> ustawic zeby byly spelnione
# -> usunac klauzule z tym co ustawilem
# -> usunac negacje tej zmiennej z innych klauzul
#dziala
def horn(formula, variables): #czy formula hornowska jest spelnialna
    k = 0
    while k < len(formula): #szukam klauzul z jedna zmienna
            if len(formula[k]) == 1: #jedna zmienna, czyli musze ja ustawic tak, zeby ta klauzula byla spelniona
                if formula[k][0] in variables: #jesli ta zmienna jest dostepna
                    v = formula[k][0]
                    if len(v) == 1: #jesli zmienna bez zaprzeczenia
                        neg = '~' + v
                    else: #jesli zaprzeczenie
                        neg = v[1]
                    for clause in formula: #szukam klauzul z ta zmienna lub jej zaprzeczeniem
                        if v in clause: #jesli v wystepuje w klauzuli, to jest ona spelniona
                            formula.remove(clause) #usuwam z listy formul
                        elif neg in clause: #jesli zanegowane v wystepuje w klauzuli, to usuwam ta zmienna z klauzuli
                            clause.remove(neg)
                    variables.remove(v) #usuwam z listy zmiennych
                    variables.remove(neg) #oraz usuwam zaprzeczenie
                else: #jesli ta zmienna nie jest dostepna, nie da sie spelnic klauzuli, czyli cala formula nie jest spelniona
                    return False
                k = 0 #szukam klauzul z jedna zmienna od nowa
            else:
                k += 1 #szukam dalej
    for clause in formula: #sprawdzam, czy z jakiejs klauzuli usunalem wszystkie zmienne (jesli tak, to jest niespelniona)
        if len(clause) == 0:
            return False
    return True #ustawiam pozostale zmienne na falsz

variables1 = ['x', '~x', 'y', '~y', 'z', '~z']
formula1 = [
    ['x'], ['~x', 'y'], ['~x', '~y', 'z'], ['x', '~y']
]
variables2 = ['x', '~x', 'y', '~y']
formula2 = [
    ['x'], ['~x', 'y'], ['~x']
]
print(horn(formula1, variables1)) #t
print(horn(formula2, variables2)) #f