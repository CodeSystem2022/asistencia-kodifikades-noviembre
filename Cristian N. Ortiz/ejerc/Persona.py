class Persona:

    contador_personas = 0

    def __init__(self, nombre, edad):
        Persona.contador_personas +=1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona = {self.id_persona} = {self.nombre} {self.edad}'

persona1 = Persona('Leo', 85)
print(persona1)
persona2 = Persona('Cristiano', 95)
print(persona2)
print(f'Contador personas: {Persona.contador_personas}')