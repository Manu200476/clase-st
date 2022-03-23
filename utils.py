def calcular_nota(media_bachiller, lengua, ingles, historia, opcional_1, opcional_2, opcional_3):
    nota_obligatoria = (lengua + ingles + historia + opcional_1) * 0.4 / 4
    nota_bach = media_bachiller * 0.6
    nota_admision = (opcional_2 + opcional_3 ) * 0.2

    nota_final = nota_bach + nota_obligatoria + nota_admision

    return nota_final
