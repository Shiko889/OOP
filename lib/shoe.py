class Shoe:
    def __init__(self, brand, material, size, color):
        self.brand = brand
        self.material = material
        self.size = size
        self.color = color
    
    def change_color(self, new_color):
        self.color = new_color
