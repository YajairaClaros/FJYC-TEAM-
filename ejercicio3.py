class pelicula():

    def __init__(self,cat,dur,enc,estr,nom):
    
        self.categoria=cat
        self.duracion = dur
        self.soloen= enc
        self.estreno=estr
        self.nombre=nom

    def cat(self):
        print("ciencia ficcion")

    def soloenc(self):
        print("solo en cines")


class interestelar(pelicula):
    def __init__(self,cat,dur,enc,estr,nom):
        super().__init__(cat,dur,enc,estr,nom)
    def nom(self):
        print("interestelar")
    def cat(self):
        print ("ciencia ficcion")
    def dur(self):
        print("2h 43m")
   

pelicula1=interestelar("ciencia ficcion ", "2h 43m","Solo en cines","8 octubre","interestellar")
pelicula1.cat()
pelicula1.dur()
pelicula1.nom()
pelicula1.soloenc()
pelicula1.cat()
