class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones
        self.conclusion = conclusion


class SistemaExperto:
    def __init__(self):
        self.base_de_reglas = []

    def agregar_regla(self, condiciones, conclusion):
        self.base_de_reglas.append(Regla(condiciones, conclusion))

    def diagnosticar_enfermedad(self, sintomas):
        for regla in self.base_de_reglas:
            if all(condicion in sintomas for condicion in regla.condiciones):
                return regla.conclusion
        return "No se pudo diagnosticar la enfermedad"


# Crear un sistema experto
sistema = SistemaExperto()

# Agregar reglas a la base de reglas
sistema.agregar_regla(["fiebre", "tos"], "resfriado")
sistema.agregar_regla(["fiebre", "dolor de cabeza"], "gripe")
sistema.agregar_regla(["dolor de garganta"], "amigdalitis")

# Consultar el sistema experto con los síntomas del paciente
sintomas_paciente = ["fiebre", "dolor de cabeza"]
enfermedad_diagnosticada = sistema.diagnosticar_enfermedad(sintomas_paciente)

print(f"Los síntomas del paciente son: {sintomas_paciente}")
print(f"El sistema experto diagnostica: {enfermedad_diagnosticada}")
