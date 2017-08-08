import json
import math

class Agent:
    """ Représente un agent caractérisé par :
        -
        -
        -
        - """
    # Constructeur utilisant un dictionnaire
    def __init__(self, position, **agent_attributes): # en parametre un dictionnaire 
        """ Le constructeur pour Agent """
        #self.agreeableness = agent_attributes["agreeableness"] # l'agreabilité
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value) # crée des attributs à partir des clés et valeur du dictionnaire

    
    def say_hello(self, first_name):
        return "Bonjour " + first_name

class Position:
    """ Reprention une position avec: une latitude et une longitude """

    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees

    @property
    def longitude(self):
        """Transforle la longitude du degré en radian
        return self.longitude_degrees * math.pi / 100 """
        return self.longitude_degrees * math.pi / 100
    @property
    def latitude(self):
        """Transforle la latitude du degré en radian
        return self.latitude_degrees * math.pi / 100 """
        return self.latitude_degrees * math.pi / 100

class Zone:
    """ Représente une zone, caractérisé par :
        - son coin inferieur gauche
        - son coin inferieur droit
        - et ses habitant """

    # les attributs de class
    ZONES = [] # liste de toute les zones créées de la grille
    MIN_LONGITUDE_DEGREES =  -180 #longitude minimale
    MAX_LONGITUDE_DEGREES = 180 #longitude maximale
    MIN_LATITUDE_DEGREES =  -90 #latitude minimale
    MAX_LATITUDE_DEGREES = 90 #latitude maximale
    WIDTH_DEGREES = 1 # l'espacement horizontal
    HEIGHT_DEGREES = 1 # l'espacement verticale

    def __init__(self, corner1, corner2):
        """ le constructeur """
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0 # une zone n'a pas d'habitant par defaut

    @classmethod #mehode de class
    def initialize_zones(cls):
        """Initialise la grille (la zone)"""
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES)) # Affiche le nombre totale de zones 
    
def main():
    """Notre fonction main() qui execute toutes les actions de notre programme """
    # Création des instance d'Agents à partir du fichier JSON
    for agent_attributes in json.load(open("agents-100k/agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(longitude, latitude)
        
        agent = Agent(position, **agent_attributes)
        Zone.initialize_zones()
        #print(agent.agreeableness)

main()
