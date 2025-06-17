import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:

    def check_types(self, *args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Todos los argumentos deben ser de tipo int o float")

    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("No es posible la division para 0")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return math.pow(x, y)

    def sqrt(self, x):
        self.check_types(x)
        if x < 0:
            raise TypeError("No se puede sacar la raíz cuadrada de un número negativo")
        return math.sqrt(x)

    def log10(self, x):
        self.check_types(x)
        if x <= 0:
            raise TypeError("Logaritmo definido únicamente para números positivos")
        return math.log10(x)


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
