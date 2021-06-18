import math


with open('data.txt') as data:
  for lines in data:
    new_lines = lines.split(',')
    name = float(lines[0])
    radius = float(lines[1])
    #height = float(lines[2])
    #cost = float(lines[3])
    print (f"{name:.2f}, {radius}")

# def main():
#   for name in new_lines:

#     volume = cylinder_volume(radius,height)

#     surface_area = cylinder_surface_area(radius,height)

#     storage_efficiency = volume / surface_area

#     print(storage_efficiency)
  
  
  

# def cylinder_volume(radius, height):
#   volume = math.pi * (radius**2) * height
#   return volume


# def cylinder_surface_area(radius, height):
#   surface_area = 2 * math.pi * radius*(radius+height)
#   return surface_area
  
  
# main()