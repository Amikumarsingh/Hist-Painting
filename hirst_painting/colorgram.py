import colorgram
""" extracting colors from image to generate hirst
     painting in the form of  r , g , b color code """
rgb_colors = []
"""to run the code , your image and file should 
    be in same folder"""
colors = colorgram.extract('hirst.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b)) 
print(code)
"""the printed color from the console is copied and paisted in main.py"""

