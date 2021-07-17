class Logica:
    def __init__(self, lista=None):
        self.__lista = lista

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, valor):
        self.__lista = valor

    def par_impar(self, numero):
        rec = numero % 2
        if rec == 0:
            print('{} es par.'.format(numero))
        else:
            print('{} es impar.'.format(numero))

    def perfecto(self, num):
        cont = 0
        for contador in range(1, num):
            rec = num % contador
            if rec == 0:
                cont += contador
        if cont == num:
            print('{} es perfecto.'.format(num))
        else:
            print('{} no es perfecto.'.format(num))


class Ejercicio(Logica):
    def __init__(self, lista, num):
        super().__init__(lista)
        self.dato = num

    def suma(self, n1, n2):
        return n1 + n2

    def par_impar(self, numero):
        super().par_impar(numero)
        return numero % 2


e = Ejercicio([1, 3, 5], 20)
if e.par_impar(6) == 0:
    print('Par')
else:
    print('Impar')
print(e.lista)