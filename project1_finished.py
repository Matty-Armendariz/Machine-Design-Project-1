# Uses Python 3.9.0
# The import wasn't working so I made a variable pi
pi = 3.14159265359

# ENTER THE MATERIALS BELOW!!
# LINES 8-41 are the only lines you need to change in the whole code!
# Material: 1045 Cold Rolled Steel
S_y = 77  # kpsi
S_ut = 91  # kpsi
E = 30  # MPsi Young's Modulus
material_type = 'steel'  # make sure this is either iron or steel
# options are: Ground, Machined , Cold-rolled, Hot-rolled, or As-forged
material_finish = 'Cold-rolled'
system_temp = 120.0  # ENTER IN DEG F this is the temp the system is subjected to
system_reliability = 99  # % refer to table 6-4 for acceptable values
# just a temporary diameter to calculate preliminary Se to find needed diameter
diameter_temp = 1

# Minimum FOS for most stress intensive part (Bearing 2) but bearing 1 is also optimized to meet this
FOS_min = 1.5
Nd = FOS_min

# Desired FOS for lesser stress concentrated areas (both bearings). You can change these as you see fit
FOS_other = 1.7

# IF YOU WANT THE PROGRAM TO RUN AUTONIMOUSLY YOU NEED TO PUT IN NEUBER CONSTANT for your material
# SQRT(a)  DON'T SQUARE IT THE CODE WILL DO EVERYTHING ELSE
neuber_a = 0.06920
# + 20 of material Sut
neuber_a_torsion = 0.054400000000000004

# %%
# Below are the calculations for the reaction forces, shear and moment at the bearings
# ENTER THE VARIABLES BELOW ONLY TO gear2_diam (LINE 48)
# Below are the gear forces in both directions and distance from bearing 1
# radial
g1fr = -197.0  # lbf
g2fr = -885.0  # lbf
# torsional
g1ft = -540.0  # lbf
g2ft = 2431.0  # lbf
# distances from bearing 1 (centerpoint to centerpoint)
dist_g1 = 2.0  # in
dist_g2 = 7.75  # in
dist_b1 = 0.0  # in
dist_b2 = 10  # in
# Diameter for the two gears
gear1_diam = 12  # in
gear2_diam = 2.67  # in

# NOTHING BELOW THIS LINE NEEDS TO BE THOUCHED PERIOD.!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reaction force y direction
# from Sum of Moment equation about b1:
r2y = (((g1fr * dist_g1) + (g2fr * dist_g2)) / dist_b2) * -1  # lbf
formatted_r2y = format(r2y, '.3f')

# Force balance equation
r1y = (g1fr + g2fr + r2y) * -1  # lbf
formatted_r1y = format(r1y, '.3f')


# Reaction forces in the z direction
# From sum of the moment in the z direction about bearing 1
r2z = (((g1ft * dist_g1) + (g2ft * dist_g2)) / dist_b2) * -1  # lb*ft
formatted_r2z = format(r2z, '.3f')

# From sum of the forces in the z direction
r1z = (g1ft + g2ft + r2z) * -1   # lb*ft
formatted_r1z = format(r1z, '.3f')

# Finding the total reaction force of the system PATHAG THEOREM ON Y AND Z COMPONENTS
r1 = ((r1y ** 2) + (r1z ** 2)) ** 0.5
formatted_r1 = format(r1, '.3f')
# print(r1)

r2 = ((r2y ** 2) + (r2z ** 2)) ** 0.5
formatted_r2 = format(r2, '.3f')


# let's the user know all the values they just calculated
print('Reaction Forces:')
print('R1: ' + str(formatted_r1) + ', ' + 'R1y: ' +
      str(formatted_r1y) + ', ' + 'R1z: ' + str(formatted_r1z))
print('')
print('R2: ' + str(formatted_r2) + ', ' + 'R2y: ' +
      str(formatted_r2y) + ', ' + 'R2z: ' + str(formatted_r2z))
print('')

# %%
# Below Calculates the shear forces for the shear diagram/points of interest
# YX Plane
shear_gear1_y = r1y + g1fr
shear_gear2_y = r1y + g1fr + g2fr

# ZX Plane
shear_gear1_z = r1z + g1ft
shear_gear2_z = r1z + g1ft + g2ft
# print(shear_gear2_z)
# Total Shear of system using Pathag theorem on the y and z components
temp1 = abs(shear_gear1_y)
temp2 = abs(shear_gear1_z)

shear_gear1_total = ((abs(shear_gear1_y) ** 2) +
                     (abs(shear_gear1_z) ** 2)) ** 0.5

shear_gear2_total = ((abs(shear_gear2_y) ** 2) +
                     (abs(shear_gear2_z) ** 2)) ** 0.5

# Below calculates the moment at all of the points of interest (gear 1 and 2)
# YX Plane
moment_gear_1_y = (r1y * dist_g1)
moment_gear_2_y = (r1y * dist_g1) + \
    (abs(shear_gear1_y * (dist_g2 - dist_g1)))

# ZX Plane
moment_gear_1_z = (r1z * dist_g1)
moment_gear_2_z = (r1z * dist_g1) + (shear_gear1_z * (dist_g2-dist_g1))

# Calculates total moment values using pathag theorem
moment_gear_1_total = ((abs(moment_gear_1_y) ** 2) +
                       (abs(moment_gear_1_z) ** 2)) ** 0.5
moment_gear_2_total = ((abs(moment_gear_2_y) ** 2) +
                       (abs(moment_gear_2_z) ** 2)) ** 0.5

print('Gear 1:')
print('Total Moment: ' + str(moment_gear_1_total) + ' lbf*ft')
print('Moment y: ' + str(moment_gear_1_y) + ' lbf*ft')
print('Moment z: ' + str(moment_gear_1_z) + ' lbf*ft')
print('')
print('Gear 2:')
print('Total Moment: ' + str(moment_gear_2_total) + ' lbf*ft')
print('Moment y: ' + str(moment_gear_2_y) + ' lbf*ft')
print('Moment z: ' + str(moment_gear_2_z) + ' lbf*ft')
print('')


# %%
# Solving for the Torque in gear 1 and gear 2.
torque_gear1 = g1ft * (gear1_diam/2)
torque_gear2 = g2ft * (gear2_diam/2)
print('Torques: ')
print('Torque gear 1: ' + str(torque_gear1))
print('Torque gear 2: ' + str(torque_gear2))
# ASSUME THAT BOTH TORQUES WILL BE EQUIVALENT (DIFFERENCE IS NEGLAGIBLE)

# ASSUME TORQUES WILL BE THE SAME (THEY ARE CLOSE ENOUGH)
torque_max = torque_gear2
torque_min = torque_gear1
print('Max Torque: ' + str(torque_gear2))
print('Min Torque: ' + str(torque_gear1))

torque_a = 0
torque_m = (torque_max + abs(torque_max)) / 2
# ALTERNATING = T_gear1 - T_gear_2 / 2 = 0/2 = 0
print('Alternating Torque: ' + str(torque_a))
# MEAN = T_gear1 + T_gear_2 / 2 = T_gear1 or T_gear2 (because they are the same)
print('Mean Torque: ' + str(torque_gear2))
print('')


# %%
# Finding the Se value
s_ut = S_ut
s_y = S_y
shaft_diameter = diameter_temp


# ALL THE STATEMENTS BELOW WILL AUTOMATICALLY POPULATE C VALUES NEEDED (DON'T TOUCH):
# Calculates the theoretical/lab se value
if s_ut < 200 and material_type == 'steel':
    se_lab = 0.5 * s_ut  # ksi
elif s_ut >= 200 and material_type == 'steel':
    se_lab = 100  # ksi
elif s_ut < 60 and material_type == 'iron':
    se_lab = 0.4 * s_ut  # ksi
elif s_ut >= 60 and material_type == 'iron':
    se_lab = 24  # ksi
else:
    print('Either an invalid Sut value or material type was entered.')

# Calculates the C_surf from material_finish_variable
if material_finish == 'Ground':
    a = 2.411
    b = -0.085
elif material_finish == 'Machined' or material_finish == 'Cold-rolled':
    a = 16.841
    b = -0.265
elif material_finish == 'Hot-rolled':
    a = 2052.9
    b = -0.718
elif material_finish == 'As-forged':
    a = 38545.0
    b = -0.995
else:
    print('An invalid material finish was entered check spelling/capitalization.')
# the 1000 turns ksi to psi which is necessary for the formula
c_surf = a * ((s_ut * 1000) ** b)

# Calculates the C_temp value form the system_temp variable
# Turns system_temp from deg F to deg C for the math necessary to calc c_temp
temp_c = ((system_temp - 32) * (5/9))

if system_temp < 840:
    c_temp = 1
elif temp_c <= 550:
    temp_c = 1 - (.0058 * (temp_c - 450))
elif temp_c <= 1020:
    temp_c = 1 - (.0032 * (temp_c - 840))
else:
    print('You put in an invalid system temp (remember it is in farenheight')

# Calculates the desired C_reliability for the system from system_reliability variable
if system_reliability == 50:
    c_reliab = 1.000
elif system_reliability == 90:
    c_reliab = 0.897
elif system_reliability == 95:
    c_reliab = 0.868
elif system_reliability == 99:
    c_reliab = 0.814
elif system_reliability == 99.9:
    c_reliab = 0.753
elif system_reliability == 99.99:
    c_reliab = 0.702
elif system_reliability == 99.999:
    c_reliab = 0.659
elif system_reliability == 99.9999:
    c_reliab = 0.620
else:
    print('You chose an invalid system_reliability, please refer to table 6-4 for valid numbers')

# Assuming that you have a solid circular shaft it calculates C_size using shaft diameter given above
if shaft_diameter <= 0.3:  # inches
    c_size = 1
elif shaft_diameter <= 10:  # inches
    c_size = 0.869 * (shaft_diameter ** -0.097)
elif shaft_diameter > 10:
    c_size = 0.6

c_load = 1

# Below Calculates the se real and prints it to the user
se_real = c_load * c_size * c_surf * c_temp * c_reliab * se_lab
formatted_se_real = format(se_real, '.4f')

print('C_load: ' + str(c_load))
print('C_size: ' + str(c_size))
print('C_surf: ' + str(c_surf))
print('C_temp: ' + str(c_temp))
print('C_reliab: ' + str(c_reliab))
print('')
print('Your real life endurance strength (Se): ' +
      str(formatted_se_real) + ' ksi')


# Above is  all the preliminary calculations for the diameter calculations
# -------------------------------------------------------------------------------------------------

# Below is all of the calculations for the diameter gear 2-----------------------------------------

# Gear 2
# %%
# SOLVING for diameter with all values calculated above (THIS IS ONLY USED TO GET ACCURATE SE REVISED)
# Design Factor of Safety

a = (32 * Nd) / pi
b = ((((moment_gear_2_total) ** 2) +
      ((3/4) * (torque_a) ** 2)) ** .5) / (se_real*1000)
c = ((3/4) ** .5) * ((torque_m) / (S_ut*1000))
diameter_new = (a * ((b + c))) ** (1/3)
print('New diameter: ' + str(diameter_new))
# THIS DIAMETER NEW WILL BE USED AS A BASELINE FOR THE REST OF THE CALCULATIONS

# %%
# Redoing the Se value calculations with new revised diameter
# ALL THE STATEMENTS BELOW WILL AUTOMATICALLY POPULATE C VALUES NEEDED (DON'T TOUCH):
# DON'T TOUCH CODE BELOW THIS
# Assuming that you have a solid circular shaft it calculates C_size using shaft diameter given above
shaft_diameter = diameter_new
if shaft_diameter <= 0.3:  # inches
    c_size = 1
elif shaft_diameter <= 10:  # inches
    c_size = 0.869 * (shaft_diameter ** -0.097)
elif shaft_diameter > 10:
    c_size = 0.6
# DON'T TOUCH ANY CODE ABOVE THIS

# Below Calculates the new se real and prints it to the user
se_real = c_load * c_size * c_surf * c_temp * c_reliab * se_lab
formatted_se_real = format(se_real, '.4f')

print('Revised values with new diameter: ')
print('C_size: ' + str(c_size))
print('Your new real life endurance strength (Se): ' +
      str(formatted_se_real) + ' ksi')

# %%
# GEAR 2 KEY
# iterates through q values to get the optimum diameter to
# Assuming r/d = .02
Kt = 2.14
Kts = 3.0

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))

Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# SOLVING for diameter with all values calculated above
# Using equation from figure A
a = (32 * Nd) / pi
b = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear2Key_diameter = (a * ((b + c))) ** (1/3)


q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear2Key_diameter ** 3) / 32
y = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear2_key = x * ((y + z) ** (-1))
notch_radius = gear2Key_diameter * .02

# GEAR 2 AT KEY
print('Values at Gear 2 key:')
print('Diameter: ' + str(gear2Key_diameter))
print('Corresponding Notch Radius: ' + str(notch_radius))
print('FOS value: ' + str(N_gear2_key))

# ~~~~~~~~ SNAP RING ~~~~~~~~~~~~~~~~~~~~
# %%
# FOR THE SNAP RING
Kt = 5
Kts = 3.0

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure A
a = (32 * Nd) / pi
b = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear2SnapRing_diameter = (a * ((b + c))) ** (1/3)

q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear2SnapRing_diameter ** 3) / 32
y = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear2_SnapRing = x * ((y + z) ** (-1))


# GEAR 2 AT SNAP RING
print('Values at Gear 2 Snap Ring:')
print('Diameter: ' + str(gear2SnapRing_diameter))
print('FOS value: ' + str(N_gear2_SnapRing))

# ~~~~~~~~SHOULDER~~~~~~~~~~~~~~~
# %%
# FOR THE SHOULDER
Kt = 2.7
Kts = 2.2

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure A
a = (32 * Nd) / pi
b = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear2shoulder_diameter = (a * ((b + c))) ** (1/3)

q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear2shoulder_diameter ** 3) / 32
y = ((((Kf * moment_gear_2_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear2 = x * ((y + z) ** (-1))
notch_radius = gear2shoulder_diameter * .02

# GEAR 2 AT Shoulder
print('Values at Gear 2 Shoulder:')
print('Diameter: ' + str(gear2shoulder_diameter))
print('Shoulder Radius: ' + str(gear2shoulder_diameter * 0.02))
print('FOS value: ' + str(N_gear2))


# GEAR 1 ----------------------------------------------

# %%
# SOLVING for diameter with all values calculated above (THIS IS ONLY USED TO GET ACCURATE SE REVISED)
# Design Factor of Safety

a = (32 * Nd) / pi
b = ((((moment_gear_1_total) ** 2) +
      ((3/4) * (torque_a) ** 2)) ** .5) / (se_real*1000)
c = ((3/4) ** .5) * ((torque_m) / (S_ut*1000))
diameter_new = (a * ((b + c))) ** (1/3)
print('New diameter: ' + str(diameter_new))

# %%
# Redoing the Se value calculations with new revised diameter
# ALL THE STATEMENTS BELOW WILL AUTOMATICALLY POPULATE C VALUES NEEDED (DON'T TOUCH):
# DON'T TOUCH CODE BELOW THIS
# Assuming that you have a solid circular shaft it calculates C_size using shaft diameter given above
shaft_diameter = diameter_new
if shaft_diameter <= 0.3:  # inches
    c_size = 1
elif shaft_diameter <= 10:  # inches
    c_size = 0.869 * (shaft_diameter ** -0.097)
elif shaft_diameter > 10:
    c_size = 0.6
# DON'T TOUCH ANY CODE ABOVE THIS

# Below Calculates the se real and prints it to the user
se_real = c_load * c_size * c_surf * c_temp * c_reliab * se_lab
formatted_se_real = format(se_real, '.4f')

print('Revised values with new diameter: ')
print('C_size: ' + str(c_size))
print('Your new real life endurance strength (Se): ' +
      str(formatted_se_real) + ' ksi')

# ~~~~~~~~ GEAR 1 KEY ~~~~~~~~~~~~~~~~~~
# %%
# GEAR 1 KEY
# iterates through q values to get the optimum diameter to
# Assuming r/d = .02
Kt = 2.14
Kts = 3.0

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# SOLVING for diameter with all values calculated above
a = (32 * Nd) / pi
b = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear1Key_diameter = (a * ((b + c))) ** (1/3)

q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear1Key_diameter ** 3) / 32
y = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear1_key = x * ((y + z) ** (-1))
notch_radius = gear1Key_diameter * .02

# GEAR 1 AT KEY
print('Values at Gear 1 key:')
print('Diameter: ' + str(gear1Key_diameter))
print('Corresponding Notch Radius: ' + str(notch_radius))
print('FOS value: ' + str(N_gear1_key))

# ~~~~~~~~~~GEAR 1 SNAP RING~~~~~~~~~~~~~
# %%
# FOR GEAR 1 SNAP RING
Kt = 5
Kts = 3.0

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

a = (32 * Nd) / pi
b = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear1SnapRing_diameter = (a * ((b + c))) ** (1/3)

q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear1SnapRing_diameter ** 3) / 32
y = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear1_SnapRing = x * ((y + z) ** (-1))

# GEAR 1 AT SNAP RING
print('Values at Gear 1 Snap Ring:')
print('Diameter: ' + str(gear1SnapRing_diameter))
print('FOS value: ' + str(N_gear1_SnapRing))

# ~~~~~~~~ GEAR 1 SHOULDER ~~~~~~~~~~
# %%
# FOR GEAR 1 SHOULDER
Kt = 2.7
Kts = 2.2

# Using the notch sensitivity equation under the assumption r/d = 0.02
# Therefore r = d*.02
q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure A
a = (32 * Nd) / pi
b = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
c = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
gear1shoulder_diameter = (a * ((b + c))) ** (1/3)

q_bending = 1 / (1 + ((neuber_a)/((diameter_new*.02) ** 0.5)))
q_shear = 1 / (1 + ((neuber_a_torsion)/((diameter_new*.02) ** 0.5)))
Kf = 1 + (q_bending*(Kt - 1))
Kfs = 1 + (q_shear*(Kts - 1))
Kfsm = Kfs

# Using equation from figure B
x = (pi * gear1shoulder_diameter ** 3) / 32
y = ((((Kf * moment_gear_1_total) ** 2) +
      ((3/4) * ((Kfs * torque_a) ** 2))) ** .5) / (se_real*1000)
z = ((3/4) ** 2) * (Kfsm * (torque_m/(S_ut*1000)))
N_gear1_shoulder = x * ((y + z) ** (-1))

# GEAR 1 AT Shoulder
print('Values at Gear 1 Shoulder:')
print('Diameter: ' + str(gear1shoulder_diameter))
print('Shoulder Radius: ' + str(gear1shoulder_diameter * .02))
print('FOS value: ' + str(N_gear1_shoulder))


# FINDING BEST DIAMETER FOR BOTH GEAR 1 AND 2
# %% This section finds the diameter for both sections

# GEAR 1
best_gear1_diam = max(
    gear1Key_diameter, gear1SnapRing_diameter, gear2shoulder_diameter)

# GEAR 2
best_gear2_diam = max(
    gear2Key_diameter, gear2SnapRing_diameter, gear1shoulder_diameter)

print('The best Gear 1 diameter is: ' + str(best_gear1_diam))
print('The best Gear 2 diameter is: ' + str(best_gear2_diam))


# FINDING KEY LENGTHS FOR GEAR 1 AND 2
# %% This section finds the key lengths for both rods
# Both will use the same force value because the Torque is equivalent but use a different d value
F_1 = torque_gear2 / (best_gear1_diam / 2)
F_2 = torque_gear2 / (best_gear2_diam / 2)

# Gear 1
width_key_1 = 0.500
key_length_g1shear = (F_1 * Nd) / (width_key_1 * (S_ut * 1000))
key_length_g1bending = (F_1 * Nd) / ((width_key_1 / 2) * (S_y * 1000))

# Gear 2
width_key_2 = 0.500
key_length_g2shear = (F_2 * Nd) / (width_key_2 * (S_ut * 1000))
key_length_g2bending = (F_2 * Nd) / ((width_key_2 / 2) * (S_y * 1000))

key_1 = max(key_length_g1bending, key_length_g1shear)
key_2 = max(key_length_g2shear, key_length_g2bending)

print('Gear 1:')
print('Key Length in bending: ' + str(key_length_g1bending))
print('Key Length in shear: ' + str(key_length_g1shear))
print('Use Key length of : ' + str(key_1))
print('')
print('Gear 2:')
print('Key Length in bending: ' + str(key_length_g2bending))
print('Key Length in shear: ' + str(key_length_g2shear))
print('Use Key length of: ' + str(key_2))

# -------------------BEARINGS---------------------------------
# %%
# NOTE: ALL VALUES FOR BEARINGS ARE CALCULATED FROM YOUR OTHER VARIABLE ENTERED AT THE BEGINNING USING A BRUTE FORCE ALGORITHM!!!
# ~~~~~~~~ BEARING 1 SHOULDER/Notch ~~~~~~~~~~
# %%
# FOR BEARING 1 SHOULDER/NOTCH

# r/d Assumed 0.02
# D/d Assumed 1.2 from recommendations on project slides

# This is a brute force algorithm to solve for the FOS_other vlaue the user input
# The algorithm will increase the diameter before the bearing by 1 millionth each iteration
N_bearing1 = 0
prior_diameter = 0.1  # diam of the shaft before bearing
while N_bearing1 < FOS_other:
    prior_diameter += .0001
    new_diam = prior_diameter / 1.2
    # new_diam = 1.5 * prior_diameter
    A = 0.97098
    B = - 0.21796

    # If you change anything to optimize bearing diameter only adjust values above
    # From project slide bearing equation
    Kt = A * (((new_diam * 0.02) / new_diam) ** B)

    # Using the notch sensitivity equation under the assumption r/d = 0.02
    # Therefore r = d*.02
    q_bending = 1 / (1 + ((neuber_a)/((new_diam * .02) ** 0.5)))
    Kf = 1 + (q_bending*(Kt - 1))
    # Uses Formula from Figure B simplified
    x = (pi * new_diam ** 3) / 32
    y = (((Kf * r1) ** 2) ** .5) / (se_real*1000)
    N_bearing1 = x * (y ** (-1))

# Saving these values for deflection
prior_diameter_1 = prior_diameter
new_diam_1 = new_diam

# BEARING 1 AT SHOULDER
print('Values at Gear 1 Shoulder:')
print('Diameter Before bearing: ' + str(prior_diameter))
print('Diameter: ' + str(new_diam))
print('Shoulder/Notch Radius: ' + str(new_diam * .02))
print('FOS value: ' + str(N_bearing1))

# ~~~~~~~~ BEARING 2 SHOULDER/NOTCH ~~~~~~~~~~
# %%
# FOR BEARING 2 SHOULDER/NOTCH

# r/d Assumed 0.02
# D/d Assumed 1.2 from recommendations on project slides

# This is a brute force algorithm to solve for the FOS_other vlaue the user input
# The algorithm will increase the diameter before the bearing by 1 millionth each iteration
N_bearing2 = 0
prior_diameter = 0.1  # diam of the shaft before bearing
while N_bearing2 < FOS_other:
    prior_diameter += .0001
    new_diam = prior_diameter / 1.2
    A = 0.97098
    B = - 0.21796

    # If you change anything to optimize bearing diameter only adjust values above
    # From project slide bearing equation
    Kt = A * (((new_diam * 0.02) / new_diam) ** B)

    # Using the notch sensitivity equation under the assumption r/d = 0.02
    # Therefore r = d*.02
    q_bending = 1 / (1 + ((neuber_a)/((new_diam * .02) ** 0.5)))
    Kf = 1 + (q_bending*(Kt - 1))
    # Uses Formula from Figure B simplified
    x = (pi * new_diam ** 3) / 32
    y = (((Kf * r2) ** 2) ** .5) / (se_real*1000)
    N_bearing2 = x * (y ** (-1))

# Saving these values for deflection
prior_diameter_2 = prior_diameter
new_diam_2 = new_diam

# BEARING 2 AT SHOULDER/NOTCH
print('Values at Bearing 2 Shoulder/Notch:')
print('Diameter Before bearing: ' + str(prior_diameter))
print('Diameter: ' + str(new_diam))
print('Shoulder/Notch Radius: ' + str(new_diam * .02))
print('FOS value: ' + str(N_bearing2))

# The commented out code is the code used for my original deflection that only used 1 cross sectional area
# # %%
# # Deflection GEAR 1 Look at Appendix for equation
# # Using the actual solved for gear diameters
# I_g1 = (pi/64) * (best_gear1_diam ** 4)  # in^4
# x = dist_g1
# a = 2.0
# b = 7.75
# c = 10

# # Deflection Singularity Look at Appendix for equation (div by 1000000 is to get out of MPsi)
# def_y = (1/(E*I_g1)) * ((r1y / 2)*(x ** 2) - (g1fr / 2)*((x - a) ** 2) -
#                         (g2fr / 2)*((x - b) ** 2) + (r2y / 2)*((x - c) ** 2)) / 1000000
# def_z = (1/(E*I_g1)) * ((r1z / 2)*(x ** 2) - (g1ft / 2)*((x - a) ** 2) -
#                         (g2ft / 2)*((x - b) ** 2) + (r2z / 2)*((x - c) ** 2)) / 1000000
# def_total = ((def_y ** 2) + (def_z ** 2)) ** 0.5

# print(def_y)
# print(def_z)
# print(def_total)


# # %%
# # Deflection GEAR 2 Look at Appendix ofr equation
# # Using the actual solved for gear diameters
# I_g2 = (pi/64) * (best_gear2_diam ** 4)  # in^4
# x = dist_g2
# a = 2.0
# b = 7.75
# c = 10

# # Deflection Singularity Look at Appendix for equation (div by 1000000 is to get out of MPsi)
# def_y = (1/(E*I_g2)) * ((r1y / 2)*(x ** 2) - (g1fr / 2)*((x - a) ** 2) -
#                         (g2fr / 2)*((x - b) ** 2) + (r2y / 2)*((x - c) ** 2)) / 1000000
# def_z = (1/(E*I_g2)) * ((r1z / 2)*(x ** 2) - (g1ft / 2)*((x - a) ** 2) -
#                         (g2ft / 2)*((x - b) ** 2) + (r2z / 2)*((x - c) ** 2)) / 1000000
# def_total = ((def_y ** 2) + (def_z ** 2)) ** 0.5

# print(def_y)
# print(def_z)
# print(def_total)

# %%
# G1 Total Deflection using individual cross section I values
I_g1 = (pi/64) * (best_gear1_diam ** 4)  # in^4
I_g2 = (pi/64) * (best_gear2_diam ** 4)  # in^4
I_b1 = (pi/64) * (new_diam_1 ** 4)  # in^4
I_b2 = (pi/64) * (new_diam_2 ** 4)  # in^4

x = dist_g1
a = 2.0
b = 7.75
c = 10

# Total force at the gear points
g1_Ftotal = ((g1fr ** 2) + (g1ft ** 2)) ** 0.5
g2_Ftotal = ((g2fr ** 2) + (g2ft ** 2)) ** 0.5

# Deflection Singularity Look at Appendix for equation (div by 1000000 is to get out of MPsi)
def_real_final = (1/(E*I_b1)) * ((r1 / 2)*(x ** 2) - (1/(E*I_g1)) * (g1_Ftotal / 2)*((x - a) ** 2) -
                                 (1/(E*I_g2)) * (g2_Ftotal / 2)*((x - b) ** 2) + (1/(E*I_g1)) * (r2 / 2)*((x - c) ** 2)) / 1000000

print('The total deflection at gear 1 is: ' + str(def_real_final) + ' in')

# %%
# G2 Total Deflection using individual cross section I values
I_g1 = (pi/64) * (best_gear1_diam ** 4)  # in^4
I_g2 = (pi/64) * (best_gear2_diam ** 4)  # in^4
I_b1 = (pi/64) * (new_diam_1 ** 4)  # in^4
I_b2 = (pi/64) * (new_diam_2 ** 4)  # in^4

x = dist_g2
a = 2.0
b = 7.75
c = 10

# Total force at the gear points
g1_Ftotal = ((g1fr ** 2) + (g1ft ** 2)) ** 0.5
g2_Ftotal = ((g2fr ** 2) + (g2ft ** 2)) ** 0.5

# g1_total and g2_total were found as a substitution for running a y and z then using pathag theorem
# Deflection Singularity Look at Appendix for equation (div by 1000000 is to get out of MPsi)
def_real_final = (1/(E*I_b1)) * ((r1 / 2)*(x ** 2) - (1/(E*I_g1)) * (g1_Ftotal / 2)*((x - a) ** 2) -
                                 (1/(E*I_g2)) * (g2_Ftotal / 2)*((x - b) ** 2) + (1/(E*I_g1)) * (r2 / 2)*((x - c) ** 2)) / 1000000

print('The total deflection at gear 2 is: ' + str(def_real_final) + ' in')
# %%
