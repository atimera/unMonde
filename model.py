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
        return self.longitude_degrees * math.pi / 180 """
        return self.longitude_degrees * math.pi / 180
    @property
    def latitude(self):
        """Transforle la latitude du degré en radian
        return self.latitude_degrees * math.pi / 180 """
        return self.latitude_degrees * math.pi / 180

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
    EARTH_RADIUS_KILOMETERS = 6371 # le rayon de la terre en kilometre

    def __init__(self, corner1, corner2):
        """ le constructeur """
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = [] # une zone n'a pas d'habitant par defaut

    @classmethod #mehode de class
    def _initialize_zones(cls):
        """Initialise la grille (la zone)"""
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
         


    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)
            
    @classmethod
    def find_zone_that_contains(cls, position):
        # Compute the index in the ZONES array that contains the given position
        if not cls.ZONES:
            cls._initialize_zones()
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone
    
    def add_inhabitant(self, inhabitant):
        """ Ajoute un agent parmis les habittant d'une zone """
        self.inhabitants.append(inhabitant)

    @property # car elle ne fait d'autre opérations que de donner le nbre d'habitant d'une zone
    def population(self):
        """ Retourne le nombre d'habitant d'une zone """
        return len(self.inhabitants)


    # pour convertir une valeur en radian en Km, on la multiplie par le rayon de la terre
    @property
    def width(self):
        """ Convertit une valeur en radian en kilometre
            en valeur absolue """
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS
    @property
    def height(self):
        """ Convertit une valeur en radian en kilometre
            en valeur absolue """
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS
    @property
    def area(self):
        """ Calcule la surface d'une zone : height * width """
        return self.height * self.width

    def average_agreeableness(self):
        """ Calcule l'agréabilité moyenne d'une zone """
        if not self.inhabitants:
            return 0 # la valeur neutre de l'agréabilité
        #agreeableness = []
        #for inhabitant in self.inhabitants:
        #    agreeableness.append(inhabitant.agreeableness)
        #return sum(agreeableness) / self.population
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population



        
    
def main():
    """Notre fonction main() qui execute toutes les actions de notre programme """
    # Création des instance d'Agents à partir du fichier JSON
    for agent_attributes in json.load(open("agents-100k/agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        print(zone.average_agreeableness())
        

main()
