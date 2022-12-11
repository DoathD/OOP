from Operation import Operation


class Multiplication(Operation):
    def get_sign(self):
        return "*"

    def get_name(self):
        return "Умножение"

    def estimate(self, a, b):
        return a * b


class Addition(Operation):
    def get_sign(self):
        return "+"

    def get_name(self):
        return "Сложение"

    def estimate(self, a, b):
        return a + b


class Substraction(Operation):
    def get_sign(self):
        return "-"

    def get_name(self):
        return "Вычитание"

    def estimate(self, a, b):
        return a - b


class Division(Operation):
    def get_sign(self):
        return "/"

    def get_name(self):
        return "Деление"

    def estimate(self, a, b):
        return a / b

class Div(Operation):
    def get_sign(self):
        return "//"

    def get_name(self):
        return "Целочисленное деление"

    def estimate(self, a, b):
        return a // b

class Mod(Operation):
    def get_sign(self):
        return "%"

    def get_name(self):
        return "Остаток"

    def estimate(self, a, b):
        return a % b

class NOD(Operation):
    def get_sign(self):
        return "NOD"

    def get_name(self):
        return "The NOD of"

    def estimate(self, a, b):
        if a > b:
            smaller = a
        else:
            smaller = b
        for i in range(1, smaller + 1):
            if (a % i == 0) and (b % i == 0):
                hcf = i
        return hcf


class NOK(Operation):
    def get_sign(self):
        return "NOK"

    def get_name(self):
        return "The NOK of"

    def estimate(self, a, b):
        if a > b:
            greater = a
        else:
            greater = b
        while (True):
            if ((greater % a == 0) and (greater % b == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

