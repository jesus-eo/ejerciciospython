def escribir_fecha(dia, numero, mes, año):
    #escribir_fecha en orden
    dia_letras = ("LMXJVSD")
    dia_1 = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')
    mes_v = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre','octubre', 'noviembre', 'diciembre')

    año_v = ('19') + str(año)

    def day(dia):
        return dia_1[dia_letras.index(dia)]

    def mes_n(mes):
        return mes_v[mes]

    return day(dia) + ',' + str(numero) + ' de ' + mes_n(mes) + ' de ' + año_v

print(escribir_fecha('M', 18, 9, 60))
