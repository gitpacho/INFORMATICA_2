rango1 = range(334, 0, -3)
rango2 = range(-5, 1000, 2)
rango3 = range(-50, -201, -5)
listaDeRangos = [rango1, rango2, rango3]


P1, P1_x, P1_y, P1_z = "P1",2, 2, 3             
P2, P2_x, P2_y, P2_z = "P2",2, 3, 4             
P3, P3_x, P3_y, P3_z = "P3",1, 1, 3             
P4, P4_x, P4_y, P4_z = "P4",0.5, 0.5, 2         
P5, P5_x, P5_y, P5_z = "P5",1, 2, 1             
P6, P6_x, P6_y, P6_z = "P6" ,1, 0.5, 1
P7, P7_x, P7_y, P7_z = "P7" ,3, 2, 0.5
P8, P8_x, P8_y, P8_z = "P8" ,3, 1, 2
P9, P9_x, P9_y, P9_z = "P9" ,0, 0, 0
P10, P10_x, P10_y, P10_z = "P10",2, 0, 0.5

parCercano = ""
ditanciaMinima = 100000

distancia = ((P1_x - P2_x)** 2 + (P1_y - P2_y)**2 + (P1_z - P2_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P2"
distancia = ((P1_x - P3_x)** 2 + (P1_y - P3_y)**2 + (P1_z - P3_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P3"
distancia = ((P1_x - P4_x)** 2 + (P1_y - P4_y)**2 + (P1_z - P4_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P4"
distancia = ((P1_x - P5_x)** 2 + (P1_y - P5_y)**2 + (P1_z - P5_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P5"
distancia = ((P1_x - P6_x)** 2 + (P1_y - P6_y)**2 + (P1_z - P6_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P6"
distancia = ((P1_x - P7_x)** 2 + (P1_y - P7_y)**2 + (P1_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P7"
distancia = ((P1_x - P8_x)** 2 + (P1_y - P8_y)**2 + (P1_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P8"
distancia = ((P1_x - P9_x)** 2 + (P1_y - P9_y)**2 + (P1_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P9"
distancia = ((P1_x - P10_x)** 2 + (P1_y - P10_y)**2 + (P1_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P1-P10"
distancia = ((P2_x - P3_x)** 2 + (P2_y - P3_y)**2 + (P2_z - P3_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P3"
distancia = ((P2_x - P4_x)** 2 + (P2_y - P4_y)**2 + (P2_z - P4_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P4"
distancia = ((P2_x - P5_x)** 2 + (P2_y - P5_y)**2 + (P2_z - P5_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P5"
distancia = ((P2_x - P6_x)** 2 + (P2_y - P6_y)**2 + (P2_z - P6_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P6"
distancia = ((P2_x - P7_x)** 2 + (P2_y - P7_y)**2 + (P2_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P7"
distancia = ((P2_x - P8_x)** 2 + (P2_y - P8_y)**2 + (P2_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P8"
distancia = ((P2_x - P9_x)** 2 + (P2_y - P9_y)**2 + (P2_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P9"
distancia = ((P2_x - P10_x)** 2 + (P2_y - P10_y)**2 + (P2_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P2-P10"
distancia = ((P3_x - P4_x)** 2 + (P3_y - P4_y)**2 + (P3_z - P4_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P4"
distancia = ((P3_x - P5_x)** 2 + (P3_y - P5_y)**2 + (P3_z - P5_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P5"
distancia = ((P3_x - P6_x)** 2 + (P3_y - P6_y)**2 + (P3_z - P6_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P6"
distancia = ((P3_x - P7_x)** 2 + (P3_y - P7_y)**2 + (P3_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P7"
distancia = ((P3_x - P8_x)** 2 + (P3_y - P8_y)**2 + (P3_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P8"
distancia = ((P3_x - P9_x)** 2 + (P3_y - P9_y)**2 + (P3_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P9"
distancia = ((P3_x - P10_x)** 2 + (P3_y - P10_y)**2 + (P3_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P3-P10"
distancia = ((P4_x - P5_x)** 2 + (P4_y - P5_y)**2 + (P4_z - P5_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P5"
distancia = ((P4_x - P6_x)** 2 + (P4_y - P6_y)**2 + (P4_z - P6_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P6"
distancia = ((P4_x - P7_x)** 2 + (P4_y - P7_y)**2 + (P4_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P7"
distancia = ((P4_x - P8_x)** 2 + (P4_y - P8_y)**2 + (P4_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P8"
distancia = ((P4_x - P9_x)** 2 + (P4_y - P9_y)**2 + (P4_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P9"
distancia = ((P4_x - P10_x)** 2 + (P4_y - P10_y)**2 + (P4_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P4-P10"
distancia = ((P5_x - P6_x)** 2 + (P5_y - P6_y)**2 + (P5_z - P6_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P5-P6"
distancia = ((P5_x - P7_x)** 2 + (P5_y - P7_y)**2 + (P5_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P5-P7"
distancia = ((P5_x - P8_x)** 2 + (P5_y - P8_y)**2 + (P5_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P5-P8"
distancia = ((P5_x - P9_x)** 2 + (P5_y - P9_y)**2 + (P5_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P5-P9"
distancia = ((P5_x - P10_x)** 2 + (P5_y - P10_y)**2 + (P5_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P5-P10"
distancia = ((P6_x - P7_x)** 2 + (P6_y - P7_y)**2 + (P6_z - P7_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P6-P7"
distancia = ((P6_x - P8_x)** 2 + (P6_y - P8_y)**2 + (P6_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P6-P8"
distancia = ((P6_x - P9_x)** 2 + (P6_y - P9_y)**2 + (P6_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P6-P9"
distancia = ((P6_x - P10_x)** 2 + (P6_y - P10_y)**2 + (P6_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P6-P10"
distancia = ((P7_x - P8_x)** 2 + (P7_y - P8_y)**2 + (P7_z - P8_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P7-P8"
distancia = ((P7_x - P9_x)** 2 + (P7_y - P9_y)**2 + (P7_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P7-P9"
distancia = ((P7_x - P10_x)** 2 + (P7_y - P10_y)**2 + (P7_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P7-P10"
distancia = ((P8_x - P9_x)** 2 + (P8_y - P9_y)**2 + (P8_z - P9_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P8-P9"
distancia = ((P8_x - P10_x)** 2 + (P8_y - P10_y)**2 + (P8_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P8-P10"
distancia = ((P9_x - P10_x)** 2 + (P9_y - P10_y)**2 + (P9_z - P10_z)**2 )**0.5
if distancia < ditanciaMinima:
    ditanciaMinima = distancia
    parCercano = "P9-P10"

print("parCercano =>", parCercano)


est1 = 0.1 * 1.0  + 0.20 * 1.1  + 0.15 * 2.3  +  0.20* 1.1  + 0.35 * 5
est2 = 0.1 * 3.1  + 0.20 * 3.1  + 0.15 * 1.2  +  0.20* 3.0  + 0.35 * 5
est3 = 0.1 * 5.0  + 0.20 * 4.0  + 0.15 * 2.5  +  0.20* 5.0  + 0.35 * 5
est4 = 0.1 * 3.1  + 0.20 * 1.0  + 0.15 * 2.6  +  0.20* 1.0  + 0.35 * 5
est5 = 0.1 * 3.2  + 0.20 * 4.0  + 0.15 * 1.1  +  0.20* 3.0  + 0.35 * 5
est6 = 0.1 * 5.0  + 0.20 * 5.0  + 0.15 * 5.0  +  0.20* 3.9  + 0.35 * 5
est7 = 0.1 * 3.4  + 0.20 * 4.0  + 0.15 * 2.6  +  0.20* 3.2  + 0.35 * 5
est8 = 0.1 * 2.0  + 0.20 * 2.2  + 0.15 * 2.1  +  0.20* 4.2  + 0.35 * 5
est9 = 0.1 * 3.7  + 0.20 * 4.1  + 0.15 * 4.7  +  0.20* 4.0  + 0.35 * 5
est10 = 0.1 * 4.1  + 0.20 * 4.7  + 0.15 * 4.4  +  0.20* 5.0  + 0.35 * 5
est11 = 0.1 * 5.0  + 0.20 * 5.0  + 0.15 * 1.0  +  0.20* 3.2  + 0.35 * 5
est12 = 0.1 * 5.0  + 0.20 * 4.2  + 0.15 * 2.1  +  0.20* 5.0  + 0.35 * 5
est13 = 0.1 * 3.2  + 0.20 * 4.1  + 0.15 * 2.2  +  0.20* 3.3  + 0.35 * 5

apruebaOReprueva1 = est1 < 3
apruebaOReprueva2 = est2 < 3
apruebaOReprueva3 = est3 < 3
apruebaOReprueva4 = est4 < 3
apruebaOReprueva5 = est5 < 3
apruebaOReprueva6 = est6 < 3
apruebaOReprueva7 = est7 < 3
apruebaOReprueva8 = est8 < 3
apruebaOReprueva9 = est9 < 3
apruebaOReprueva10 = est10 < 3
apruebaOReprueva11 = est11 < 3
apruebaOReprueva12 = est12 < 3
apruebaOReprueva13 = est13 < 3

cantidad_que_pierden = apruebaOReprueva1 + apruebaOReprueva2 + apruebaOReprueva3 + apruebaOReprueva4 + apruebaOReprueva5 + apruebaOReprueva6 + apruebaOReprueva7 + apruebaOReprueva8 + apruebaOReprueva9 + apruebaOReprueva10 + apruebaOReprueva11 + apruebaOReprueva12 + apruebaOReprueva13
print(cantidad_que_pierden)

#----------------------------------------------------------------------------------

est1 = 0.1 * 1.0  + 0.20 * 1.1  + 0.15 * 2.3  +  0.20* 1.1  + 0.35 * 0
est2 = 0.1 * 3.1  + 0.20 * 3.1  + 0.15 * 1.2  +  0.20* 3.0  + 0.35 * 0
est3 = 0.1 * 5.0  + 0.20 * 4.0  + 0.15 * 2.5  +  0.20* 5.0  + 0.35 * 0
est4 = 0.1 * 3.1  + 0.20 * 1.0  + 0.15 * 2.6  +  0.20* 1.0  + 0.35 * 0
est5 = 0.1 * 3.2  + 0.20 * 4.0  + 0.15 * 1.1  +  0.20* 3.0  + 0.35 * 0
est6 = 0.1 * 5.0  + 0.20 * 5.0  + 0.15 * 5.0  +  0.20* 3.9  + 0.35 * 0
est7 = 0.1 * 3.4  + 0.20 * 4.0  + 0.15 * 2.6  +  0.20* 3.2  + 0.35 * 0
est8 = 0.1 * 2.0  + 0.20 * 2.2  + 0.15 * 2.1  +  0.20* 4.2  + 0.35 * 0
est9 = 0.1 * 3.7  + 0.20 * 4.1  + 0.15 * 4.7  +  0.20* 4.0  + 0.35 * 0
est10 = 0.1 * 4.1  + 0.20 * 4.7  + 0.15 * 4.4  +  0.20* 5.0  + 0.35 * 0
est11 = 0.1 * 5.0  + 0.20 * 5.0  + 0.15 * 1.0  +  0.20* 3.2  + 0.35 * 0
est12 = 0.1 * 5.0  + 0.20 * 4.2  + 0.15 * 2.1  +  0.20* 5.0  + 0.35 * 0
est13 = 0.1 * 3.2  + 0.20 * 4.1  + 0.15 * 2.2  +  0.20* 3.3  + 0.35 * 0


apruebaOReprueva1 = est1 >= 3
apruebaOReprueva2 = est2 >= 3
apruebaOReprueva3 = est3 >= 3
apruebaOReprueva4 = est4 >= 3
apruebaOReprueva5 = est5 >= 3
apruebaOReprueva6 = est6 >= 3
apruebaOReprueva7 = est7 >= 3
apruebaOReprueva8 = est8 >= 3
apruebaOReprueva9 = est9 >= 3
apruebaOReprueva10 = est10 >= 3
apruebaOReprueva11 = est11 >= 3
apruebaOReprueva12 = est12 >= 3
apruebaOReprueva13 = est13 >= 3

cantidad_que_aprueban = apruebaOReprueva1 + apruebaOReprueva2 + apruebaOReprueva3 + apruebaOReprueva4 + apruebaOReprueva5 + apruebaOReprueva6 + apruebaOReprueva7 + apruebaOReprueva8 + apruebaOReprueva9 + apruebaOReprueva10 + apruebaOReprueva11 + apruebaOReprueva12 + apruebaOReprueva13
print(cantidad_que_aprueban)

#------------------------------------------------
Cantidad_con_posibilidades = 13 - cantidad_que_aprueban - cantidad_que_pierden
print(Cantidad_con_posibilidades)

#5


precioSeguro = 120_000
numeroDeSegurosVendidos = 50


if numeroDeSegurosVendidos <= 20:
    comision = precioSeguro * numeroDeSegurosVendidos * 0.2
elif numeroDeSegurosVendidos <= 120:
    comision1 = precioSeguro * 20 * 0.2
    comision = comision1 + precioSeguro * (numeroDeSegurosVendidos-20) * 0.3
else:
    comision1 =  precioSeguro * 20 * 0.2
    comision2 = comision1 + precioSeguro * 100 * 0.3
    comision  = comision2 + precioSeguro * (numeroDeSegurosVendidos-120) * 0.3





































