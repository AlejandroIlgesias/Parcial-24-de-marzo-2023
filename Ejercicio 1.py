#Clase libro.

class Libro():
    
    def __init__(self,paginas,titulo,autor):
        self.paginas=paginas
        self.titulo=titulo
        self.autor=autor
    
    def propiedades(self):
        
        return {"Paginas":self.paginas,"Titulo":self.titulo,"Autor":self.autor}
    
    
