class emissionType: # constructor
    def __init__(self, token_number, month, vest, unvest):
        self.token_number = token_number
        self.month = month
        self.vest = vest
        self.unvest = unvest

def namestr(obj, namespace): # name of a variable
    return [name for name in namespace if namespace[name] is obj]

# generate objects
privateRoundOne = emissionType(7.5,0,24,6)
privateRoundTwo = emissionType(7.5,6,24,6)
publicRound = emissionType(10,12,24,6)
team = emissionType(20,0,36,12)

# list the objects
emissionSources = [privateRoundOne,privateRoundTwo,publicRound,team]

f = open("emission.txt", "w+")

# create header
header = []
for c in emissionSources:
    header.append(namestr(c,globals())[0])
header.append('total')
f.write(str(header)[1:-1]+'\n')

monthTotal = 60

# create cumsum values
for i in range(monthTotal):
    cumEmission = []
    DV = 0
    for j in emissionSources:
        if(j.month+j.vest>i):
            cumEmission.append(0)
        elif(j.month+j.vest+j.unvest>=i):
            cumEmission.append((j.token_number/j.unvest)*(i-(j.month+j.vest)))
        else:
            cumEmission.append(j.token_number)
        DV += cumEmission[-1]
    cumEmission.append(DV)

    f.write(str(cumEmission)[1:-1]+'\n')

f.close()