class emissionType: # constructor
    def __init__(self, token_quantity, start_month, lock_period, unlock_period):
        self.token_quantity = token_quantity
        self.start_month = start_month
        self.lock_period = lock_period
        self.unlock_period = unlock_period

def namestr(obj, namespace): # name of a variable
    return [name for name in namespace if namespace[name] is obj]

# generate objects
private_sale = emissionType(15,0,12,24)
marketing = emissionType(4,0,0,12)
team = emissionType(14,0,12,36)

public_sale = emissionType(10,2,12,18)

community = emissionType(24,4,0,1)

ecosystem = emissionType(6,24,0,12)
chain = emissionType(6,24,0,48)

# list the objects
emissionSources = [team,community,private_sale,public_sale,marketing,ecosystem,chain]

f = open("emission.txt", "w+")

# create header
header = []
for c in emissionSources:
    header.append(namestr(c,globals())[0])
header.append('total')
f.write(str(header)[1:-1]+'\n')

start_monthTotal = 60

# create cumsum values
for i in range(start_monthTotal):
    cumEmission = []
    DV = 0
    for j in emissionSources:
        if(j.start_month+j.lock_period>i):
            cumEmission.append(0)
        elif(j.start_month+j.lock_period+j.unlock_period>=i):
            cumEmission.append((j.token_quantity/j.unlock_period)*(i-(j.start_month+j.lock_period)))
        else:
            cumEmission.append(j.token_quantity)
        DV += cumEmission[-1]
    cumEmission.append(DV)

    f.write(str(cumEmission)[1:-1]+'\n')

f.close()