class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {
            "edad": 0,
            "ingresos": 0,
            "deudas": 0,
            "trabajo": ""
        }

    def obtener_datos(self):
        self.base_conocimiento["edad"] = int(input("Ingrese su edad: "))
        self.base_conocimiento["ingresos"] = int(input("Ingrese sus ingresos mensuales: "))
        self.base_conocimiento["deudas"] = int(input("Ingrese sus deudas mensuales: "))
        self.base_conocimiento["trabajo"] = input("Ingrese su tipo de trabajo (empleo, freelance, desempleado): ")

    def evaluar_aprobacion_prestamo(self):
        puntaje = 0
        if self.base_conocimiento["edad"] >= 18 and self.base_conocimiento["edad"] <= 65:
            puntaje += 1
        if self.base_conocimiento["ingresos"] >= 1000:
            puntaje += 1
        if self.base_conocimiento["deudas"] <= 500:
            puntaje += 1
        if self.base_conocimiento["trabajo"] == "empleo":
            puntaje += 1

        if puntaje >= 3:
            print("¡Felicidades! Usted es apto para obtener un préstamo bancario.")
        else:
            print("Lo siento, no cumple con los requisitos para obtener un préstamo bancario.")


# Uso del sistema experto
sistema = SistemaExperto()
sistema.obtener_datos()
sistema.evaluar_aprobacion_prestamo()
