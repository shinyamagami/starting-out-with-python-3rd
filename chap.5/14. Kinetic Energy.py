# Chapter.5
# 14. Kinetic Energy

mass = float(input('Enter the object\'s mass in kilograms: '))
velocity = float(input('Enter the object\'s velocity in meters per second: '))
def kinetic_energy(mass, velocity):
    KE = (1/2) * mass * (velocity ** 2)
    print('The amount of kinetic energy that the object has', KE)
    return KE

kinetic_energy(mass, velocity)
