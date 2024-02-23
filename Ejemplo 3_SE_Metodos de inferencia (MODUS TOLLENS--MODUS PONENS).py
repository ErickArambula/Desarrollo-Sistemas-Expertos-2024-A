#  Erick Alejandro Arambula Saldana    21110401     23/FEB/24
# Sistemas expertos metodos de inferencia 
#*************************  EJEMPLO MODUS TOLLENS  *****************************

def modus_tollens(premisa_condicional, negacion_consecuente, consecuente):
    if premisa_condicional and not consecuente:
        return not negacion_consecuente
    else:
        return "No se puede aplicar Modus Tollens"

# Premisa condicional: Si hay humo, entonces hay fuego
premisa_condicional = True

# Negación del consecuente: No hay fuego
negacion_consecuente = True

# Consecuente: No hay humo
consecuente = False

resultado = modus_tollens(premisa_condicional, negacion_consecuente, consecuente)
print("Resultado de aplicar Modus Tollens:", resultado)

#******************************************************************************

#*************************  EJEMPLO MODUS PONENS  *****************************

def modus_ponens(premisa_condicional, antecedente):
    if premisa_condicional and antecedente:
        return True
    else:
        return "No se puede aplicar Modus Ponens"

# Premisa condicional: Si llueve, entonces las calles estarán mojadas
premisa_condicional = True

# Antecedente: Está lloviendo
antecedente = True

resultado = modus_ponens(premisa_condicional, antecedente)
print("Resultado de aplicar Modus Ponens:", resultado)

#**********************************************************************************
