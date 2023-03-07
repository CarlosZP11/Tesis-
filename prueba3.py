from pulp import *

n1 = int(input("Escribe número de tiendas: "))
i = int(1)
s = (float(input("Escribe recursos totales dentro del almacen: ")))
costes = []
demandas = []
variables = []

while (i < n1 + 1):
    costes.append(input("Costo transporte del almacen a la tienda " + str(i) +":"))
    demandas.append(float(input("Demanda tienda " + str(i) + ":")))
    variables.append("x_" + str(i))
    i=i+1


print(costes)
print(demandas)
print(variables)


# c1 = float(costes[0])
# c2 = float(costes[1])
# c3 = float(costes[2])
# d1 = float(demandas[0])
# d2 = float(demandas[1])
# d3 = float(demandas[2])


# print(c1)
# print(c2)
# print(c3)
# print(s)


variablespl = []
problema = LpProblem("Problema_Ruteo_Vehiculos", LpMinimize)
for j in range(0,n1):
    variablespl.append(LpVariable("X_" + str(j), lowBound=0))
    j = j + 1

print(variablespl)

# x1 = variablespl[0]
# x2 = variablespl[1]
# x3 = variablespl[2]


# producto = []
# for el1, el2 in zip(costes, variablespl):
#     producto.append(el1*el2)

# print(producto)


##Funcion objetivo 
#problema += c1*x1 + c2*x2 + c3*x3
for i in range(len(costes)):
    problema += float(costes[i])*variablespl[i]
    
    problema += variablespl[i] >= float(demandas[i])

##Restricciones
# problema += x1 >= d1
# problema += x2 >= d2
# problema += x3 >= d3
# problema += x1 + x2 + x3 <= s



problema.solve()

for i in range(len(costes)):
    print("x_" + str(i + 1), variablespl[i].varValue)
#print("x1=", x1.varValue, "x2=", x2.varValue, "x3=", x3.varValue)



# if x1 != math.trunc(x1):
    
#     ##Funcion objetivo 
#     problema += c1*x1 + c2*x2 + c3*x3

#     ##Restricciones
#     problema += x1 >= d1
#     problema += x2 >= d2
#     problema += x3 >= d3
#     problema += x1 <= math.trunc(x1)
#     problema += x1 + x2 + x3 <= s






