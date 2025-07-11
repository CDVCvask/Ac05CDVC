class Student:
    def __init__(self,name,id,Carrer,fnote):
        self.name = name
        self.ID = id
        self.Carrer = Carrer
        self.Fnote = fnote
    def Show(self):
        print(f" El/La estudiante {self.name} de la carrera {self.Carrer} carnet: {self.ID} Nota final: {self.Fnote}")
        print(" ")
def MENU():
    print("Menu de estudiantes")
    print("1.Agregar estudiantes")
    print("2.Mostrar lista de estudiantes")
    print("3.Buscar estudiante por su carnet")
    print("4.Mostrar promedio de notas de estudiantes")
    print("5.Salir")
allow = False
students = []
check = 0
try:
    while allow == False:
        MENU()
        opt = int(input("Seleccione la opcion que desee: "))
        match opt:
            case 1:
                repeat = 0
                name = input("Ingrese el nombre del estudiante: ")
                id = input("Ingrese el carnet del estudiante: ")
                for student in students:
                    if id == student.ID:
                        repeat = 1
                if repeat == 1:
                    print("Ese numero de carnet ya existe, no se pueden repetir")
                else:
                    carrer = input("Ingrese la carrera del estudiante: ")
                    fnote = int(input("Ingrese la nota final del estudiante: "))
                    if fnote <0 or fnote > 100:
                        print("El valor ingresado no es valido")
                    else:
                        student = Student(name,id,carrer,fnote)
                        students.append(student)
            case 2:
                if check == 0:
                    print("Aún no se a ingresado ningún estudiante")
                else:
                    for student in students:
                        student.Show()
            case 3:
                find = False
                if check == 0:
                    print("Aún no se a ingresado ningún estudiante")
                else:
                    look = input("Ingrese el carnet del estudiante que desea encontrar:")
                    for student in students:
                        if student.ID == look:
                            find = True
                    if find == True:
                        for student in students:
                             if student.ID == look:
                                print("El estudiante que busca es: ")
                                student.Show()
                    else:
                        print("No hay ningún estudiante que coincida")
            case 4:
                avarage = 0
                if check == 0:
                    print("Aún no se a ingresado ningún estudiante")
                else:
                    for student in students:
                        avarage = avarage + student.Fnote
                    Tavarage = avarage / students.count()
                    print(f"El promedio de todos los estudiantes es: {Tavarage}")
            case 5:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("A ocurrido un error, no se ha ingresado el tipo de valor correcto")