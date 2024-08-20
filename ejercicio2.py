# Herencia de Libro --> Novela --> Romantica 

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descripcion(self):
        return f"{self.titulo}, escrito por {self.autor}, tiene {self.paginas} páginas."


# Clase que hereda de Libro
class Novela(Libro):
    def __init__(self, titulo, autor, paginas, genero):
        super().__init__(titulo, autor, paginas)
        self.genero = genero

    def descripcion(self):
        return f"'{self.titulo}' es una novela de {self.genero} escrita por {self.autor}, con {self.paginas} páginas."


# Clase que hereda de Novela
class Romantica(Novela):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor, paginas, "romántica")

    def descripcion(self):
        return f"'{self.titulo}' es una novela romántica escrita por {self.autor}, con {self.paginas} páginas."

# Ejemplo de uso
libro_romantico = Romantica("Orgullo y Prejuicio", "Jane Austen", 432)
print(libro_romantico.descripcion())
