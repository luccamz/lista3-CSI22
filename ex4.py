class C:

    def __init__(self):
        self.field = 0
    def instance_method(self, n):
        self.field = n
    @classmethod
    def class_method(cls, n):
        obj = cls()
        obj.field = n
    @staticmethod
    def static_method(self,cls):
        print(isinstance(self,cls))

obj = C()

#O metodo de instancia tem acesso a uma instancia em particular, e portanto exige que na chamada da função a instância esteja presente como argumento
obj.instance_method(20)
#ou
C.instance_method(obj,20)
print(obj.field)

#O metodo de classe pode ser chamado sem uma instância, mas não tem acesso aos campos criados com a inicialização de um objeto da classe
C.class_method(30)
#tambem pode ser chamado atraves de uma instancia
obj.class_method(30)
#o campo do objeto nao eh afetado
print(obj.field)

#O metodo estatico nao requer a classe ou uma instancia como argumento, e tambem nao tem acesso aos seus campos
C.static_method("str",float)