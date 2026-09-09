import sys
def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])

print(f"Soma: {somar(n1,n2)}")
print(f"Subtracao: {subtrair(n1,n2)}")
print(f"Multiplicacao: {multiplicar(n1,n2)}")
print(f"Divisao: {dividir(n1,n2)}")
