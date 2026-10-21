import numpy as np

califas=np.array([60,70,90])
print(" ----------  ej 1 imprimir califas ----------")
print(califas) # imprime las listas de califas
print(type(califas)) # muestra el tipo de arreglo
print("-------------- ej 0 dimensiones de un array---------")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)
print("-------------- ej 1 dimensiones de un array---------")
califas =np.array([60,70,90])
print(califas)
print("dimension :", califas.ndim)
print("-------------- ej 2 dimensiones de un array---------")
califas=np.array([
    [60,70,90],
    []
    ])
print(califas)
print("dimension :", califas.ndim)