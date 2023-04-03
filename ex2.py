class I:
    def msg(self):
        print("msg")

class A(I):
    def msg(self):
        print("another msg")

class T(A):
    pass

class B(T):
    def msg(self):
        super().msg()
        print("Called from B")

class D(I):
    def msg(self):
        super().msg()
        print("Called from D")

class C(I):
    def msg(self):
        super().msg()
        print("Called from C")

class E(C,B):
    def msg(self):
        super().msg()
        print("Called from E")

class H(D):
    pass

class F(H,E,D):
    pass

"""
Seguindo a ordem do MRO, procura-se pela primeira ocorrência da definição de um método condizente com a chamada e
ao encontrá-la, o método é aplicado. No exemplo, em ambos os casos, F() e E(), a definição encontrada se encontra na classe E.

Quando se chama um método de uma classe pai através de super(), o que ocorre 
é que a ordem seguida ainda é a do MRO da classe mais concreta do objeto que fez a chamada original, por isso, é possível 
alterar os efeitos da chamada com super() ao se alterar o MRO em uma classe filha. Nesse exemplo, ao se introduzir D como classe 
da qual F herda, essa é resolvida como prioritária no MRO de F em relação a C, que no MRO de E vem logo depois da própria.
Por isso, quando é feita a chamada do método por F, super().msg() na definição de E encontra D.msg(), causando a diferença na ordem
das mensagens printadas (D entre C e E).

Finalmente, ainda que existam definições do método em classes mais abstratas, essas não são usadas se o método pôde ser resolvido 
pela definição em uma classe mais concreta. Desse modo, o método definido em I foi sobrescrito pelo método definido em A.
"""

print("Metodo msg para classe F")
f = F()
f.msg()
print("Metodo msg para classe E")
e = E()
e.msg()

#print(e.__class__.mro())
#print(f.__class__.mro())