class Caso:
    def __init__(self, clima, temperatura, actividad):
        self.clima = clima
        self.temperatura = temperatura
        self.actividad = actividad


class SistemaExperto:
    def __init__(self):
        self.base_de_casos = []

    def agregar_caso(self, clima, temperatura, actividad):
        self.base_de_casos.append(Caso(clima, temperatura, actividad))

    def recomendar_actividad(self, clima_actual, temperatura_actual):
        # Buscar casos similares en la base de casos
        casos_similares = [caso for caso in self.base_de_casos
                           if caso.clima == clima_actual and caso.temperatura == temperatura_actual]

        if casos_similares:
            # Tomar la actividad del primer caso similar encontrado
            return casos_similares[0].actividad
        else:
            return "No se encontró una recomendación para estas condiciones"


# Crear un sistema experto
sistema = SistemaExperto()

# Agregar casos a la base de casos
sistema.agregar_caso("soleado", 30, "ir a la playa")
sistema.agregar_caso("soleado", 25, "jugar al tenis")
sistema.agregar_caso("nublado", 20, "salir a correr")

# Consultar el sistema experto
clima_actual = "soleado"
temperatura_actual = 30
actividad_recomendada = sistema.recomendar_actividad(clima_actual, temperatura_actual)

print(f"Para un clima {clima_actual} y una temperatura de {temperatura_actual}°C, se recomienda: {actividad_recomendada}")

