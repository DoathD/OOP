class Country:
    def __init__(self, name, population, gdp, area):
        self.name = name
        self.population = population
        self.gdp = gdp
        self.area = area

    def __str__(self):
        return f" Information: {self.name}, {self.population} million people, {self.gdp} billions of dollars, {self.area} square kilometers\n"