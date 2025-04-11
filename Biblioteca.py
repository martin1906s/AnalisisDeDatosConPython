class Libro:
    def __init__(self, titulo, autor, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"{self.titulo} - {self.autor} ({self.paginas}.pag)")

    @staticmethod
    def es_grande(paginas: int):
        return True if paginas > 300 else False
    
    @classmethod
    def total_libros(cls, libros):
        return len(libros)