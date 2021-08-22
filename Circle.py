class Circle:
    def __init__(self, x, y, radius, B, G, R):
        self.x = x
        self.y = y
        self.rgb = {
            'B': B,
            'G': G,
            'R': R
        }
        self.radius = radius
        if R > 100 and B > 100:
            colorName = 'purple'
        elif B > 150:
            colorName = 'blue'
        elif G > R and G > 100:
            colorName = 'green'
        elif R > G and G < 100:
            colorName = 'red'
        else:
            colorName = 'yellow'
        self.color = colorName
