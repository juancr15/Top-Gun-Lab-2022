'''
    El capitán del barco pirata Thousand Sunny, 
    el famoso Monkey D. Luffy te ha designado 
    para que sirva de vigía en el mástil principal.

    Crear un programa que, dada la criatura y la ubicación, 
    construya la cadena correcta. El programa se debe ejecutar 
    las veces que sea necesario hasta que el capital te diga “stop”.
'''

# Dictionary of creatures and their respective articles
dictCreatures = {'Kraken': 'un', 'Sirenas': 'unas', 
                'Ballena': 'una', 'Hipocampo': 'un', 
                'Macaraprono': 'una', 'Pulpo': 'un', 
                'Leviatanes': 'unos', 'Hidras': 'unas'}

# Dictionary of the ship steering and its preposition
dictShipSteering = {'babor': 'a', 'estribor': 'a', 'proa': 'por la', 'popa': 'por la'}

# Initialize variables
creature = ''


while creature != 'Stop':

    # Asking for the creature
    creature = input('¿Qué criatura estás viendo?\n\t')

    # Validating the if the creature is in the dictionary
    if creature.capitalize() in dictCreatures:
        ship_steering = input(f'¿Dónde estás viendo {dictCreatures[creature.capitalize()]} {creature.capitalize()}?\n\t')

        # Validating the if the ship steering is in the dictionary
        if ship_steering.lower() not in dictShipSteering:
            print('No reconozco esa dirección. Intentalo nuevamente.')
            continue
        print(f'¡Ahoy! capitán, {dictCreatures[creature.capitalize()]} {creature.capitalize()} {dictShipSteering[ship_steering.lower()]} {ship_steering.lower()}.\n')
    
    # Stopping the loop if the creature is 'Stop'
    elif creature.capitalize() == 'Stop':
        print('¡Hasta aquí llegamos, marinero! Buen viaje.')
        break
    else:
        print('Esa criatura no existe. Ingresala nuevamente!')
        continue
