from itertools import count


[i for i in ifilter(lambda x:x%5, islice(count(5),10))]


# a=7
# a.__str__()
# print(a)


# v1=[7,3,5]
# v2=[1,2,3]
# producto_escalar=0
# for i in range(len(v1)):
#     producto_escalar += v1[i] * v2[i]
# print(f"El producto escalar de {v1} y {v2} es {producto_escalar}.")



























# v1 = [7,3,5]
# v2 = [-5,-91,67]
# producto_escalar = 0
# for i in range(len(v2)):
#     producto_escalar += v1[i] * v2[i]
# print(f"El producto escalar de {v1} * {v2} es {producto_escalar}.")



















# v1 = [1,2,3]
# v2 = [-1,0,2]
# producto_escalar = 0

# for i in range(len(v1)):
#     producto_escalar += v1[i] * v2[i]

# print(f"El producto escalar de {v1} * {v2} es {producto_escalar}.")