pi = 22/7
radiusEarth = 6400 

lat_np = 90

# arc length = radius \times angle subtended 

# Task 1 : DIstance betwewen Berlin and North pole 
lat_berlin = 52.52
lat_diff = lat_np - lat_berlin
ang_rad_diff = (pi * lat_diff) / 180

arc_length = radiusEarth * ang_rad_diff

print('The distance to the North pole from Berlin is', arc_length ,' km.')

print('The great circle  distance to the North pole from Berlin is', arc_length ,' km.')
print('--')
# Task 1 : Any city input and distance 
city_name = input('Enter the name of the city : ') 
lat_city = float(input('Enter the latitude of the city : '))

lat_diff_input = lat_np - lat_city 
ang_rad_diff_input = (pi * lat_diff_input) / 180

arc_length_input = radiusEarth * ang_rad_diff_input

print('The distance to the North pole from', city_name ,'is', arc_length_input ,' km.')

print('The great circle distance to the North pole from', city_name ,'is', arc_length_input ,' km.')

print('--')

# Task 2 : Approx circumference of earth 

lat_equator = 0
lat_diff = lat_np - lat_equator
ang_rad_diff = (pi * lat_diff) / 180

arc_length = radiusEarth * ang_rad_diff

circumference_earth = 4 * arc_length 

print('The approximate circumference of earth is ', circumference_earth ,' km.')

print('--')

