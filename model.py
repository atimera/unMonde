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

def main():
    """Notre fonction main() qui execute toutes les actions de notre programme """
    # Création des instance d'Agents à partir du fichier JSON
    for agent_attributes in json.load(open("agents-100k/agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(longitude, latitude)
        
        agent = Agent(position, **agent_attributes)
        print(agent.position.latitude)
        #print(agent.agreeableness)

main()
