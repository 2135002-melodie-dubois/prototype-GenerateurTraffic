import random;
class PrototypeVehicule:
    def clone(self):
        pass
    def seDeplacer(self):
        pass

class Voiture(PrototypeVehicule):
    def __init__(self, couleur, vitesse):
        self.couleur = couleur
        self.vitesse = vitesse

    def klaxonner(self):
        print("BEEP BEEP!")
    
    def clone(self):
            new = self.__class__(
            self.couleur, self.vitesse
            )
            new.__dict__.update(self.__dict__)

            return new

    def seDeplacer(self):
        print(f"Une voiture {self.couleur} passe a {self.vitesse} km/h")


if __name__ == "__main__":
        vehicules = [Voiture("Rouge",50),Voiture("Bleue",70),Voiture("Rouge",90)]
           
        traffic = []
        for i in range(0, random.randint(1, 5)):
            traffic.append(vehicules[random.randint(0, len(vehicules)-1)])
   
        for i in range(len(traffic)):
            traffic[i].seDeplacer()
            if random.randint(0, 1):
                 traffic[i].klaxonner()
