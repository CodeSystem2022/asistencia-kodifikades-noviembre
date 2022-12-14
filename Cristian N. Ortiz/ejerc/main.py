class MiClase:

    variable_clase = 'Esto es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2=MiClase('otra variable instancia')