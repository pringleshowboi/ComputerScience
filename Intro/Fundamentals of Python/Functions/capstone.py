# Constants
train_mass = 22680  # in kilograms
train_acceleration = 10  # in m/s^2
train_distance = 100  # in meters
bomb_mass = 1  # in kilograms

# 1. Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

# 2. Test f_to_c
f100_in_celsius = f_to_c(100)
print(f"100 Fahrenheit in Celsius is: {f100_in_celsius}")

# 3. Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp

# 4. Test c_to_f
c0_in_fahrenheit = c_to_f(0)
print(f"0 Celsius in Fahrenheit is: {c0_in_fahrenheit}")

# 5. Calculate force
def get_force(mass, acceleration):
    return mass * acceleration

# 6. Test get_force
train_force = get_force(train_mass, train_acceleration)

# 7. Print train force
print(f"The GE train supplies {train_force} Newtons of force.")

# 8. Calculate energy (default c = speed of light)
def get_energy(mass, c=3*10**8):
    return mass * c ** 2

# 9. Test get_energy
bomb_energy = get_energy(bomb_mass)

# 10. Print bomb energy
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# 11. Calculate work = force * distance
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# 12. Test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)

# 13. Print train work
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
