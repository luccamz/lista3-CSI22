class Abstract:
    def method(self):
        print("called abstract method")

class Concrete1(Abstract):
    pass

class Concrete2(Abstract):
    pass

class Unrelated:
    def method(self):
        print("completely different thing")

c1 = Concrete1()
c2 = Concrete2()
u = Unrelated()

#O polimorfismo propocionado pela herança permite que objetos de diferentes subclasses usem a mesma chamada de método

print("Polimorfismo")
for i, obj in enumerate((c1,c2)):
    print(f"\nc{i} de classe {obj.__class__}:")
    obj.method()

#Por outro lado o duck typing permite mesma chamada de método para objetos cujas classes definam os mesmos metodos

print("\nDuck typing")
for obj in (c1,u):
    print(f"\nObjeto: {obj}")
    obj.method()