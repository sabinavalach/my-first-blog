print('Ahoj', 'Djangogirls')
if 3 > 2:
    print('Funguje to!')

if 5 > 2:
    print('5 je naozaj viac ako 2') 
else:
    print('5 nie je viac ako 2')

def ahoj():
    print('Ahoj!')
    print('Ako sa mas?')

ahoj()

def ahoj(meno):
    if meno == 'Ola':
        print('Ahoj Ola!')
    elif meno == 'Sona':
        print('Ahoj Sona!')
    else:
        print('Ahoj neznama!')

ahoj("Ola")

dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
for meno in dievcata:
    def ahoj(meno):
    print('Ahoj ' + meno + '!')

dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
for meno in dievcata:
    ahoj(meno)
    print('Dalsie dievca')