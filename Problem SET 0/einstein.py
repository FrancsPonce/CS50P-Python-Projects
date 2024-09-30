


def light():
    L=300000000
    calculated_L= int(L*L)
    return calculated_L

def energy():
    mass=int(input("Write a mass quantity (kg) "))
    energy_result= mass*light()
    print(energy_result)

energy()

