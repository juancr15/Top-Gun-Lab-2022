""" En un episodio de CSI un capo de la mafia diseño un 
    interesante método para evitar que en sus mensajes 
    descubrieran los números telefónicos, las direcciones 
    y los valores reales de sus transacciones. El método 
    se llamaba Saltando al 5.

    Lo que debes haces es implementar una función que codifique 
    y otra que decodifique mensajes utilizando la estrategia 
    Saltando al 5. Así que muestra un menú con las opciones.
"""

def main():
    message = input("What's your message? \n")
    action = menu()
    
    if action == "1":
        encode(message)
    else :
        decode(message)

def encode(text):
    """ Encodes the numbers in the message.
    
    Parameters:
        text (string): The message to be encoded.
    
    Returns:
        None. It prints the encoded message.
    """
    text = list(text) # Convert the string to a list
    for i in range(len(text)): # Go through the list
        if text[i].isdigit(): # If the current char is a number
            text[i] = replace_char(text[i]) # Replace the number with the jumped one
    print(''.join(text)) # Print all the items in the list joined.

def decode(text):
    """ Decodes the numbers in the message.
    
    Parameters:
        text (string): The message to be decoded.
        
    Returns:
        None. It prints the decoded message.
    """
    text = list(text)
    for i in range(len(text)):
        if text[i].isdigit():
            text[i] = replace_char(text[i])
    print(''.join(text))

def replace_char(char) :
    """ Replaces the current number with the jumped one.
    
    Parameters:
        char (string): The number to be replaced.
        
    Returns:
        string: The jumped number."""
    regular = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    skip = [9, 8, 7, 6, 0, 4, 3, 2, 1, 5]
    return str(skip[regular.index(int(char))])

def menu():
    """ Shows the menu.
        It asks the user the action and validates the input.
    
    Parameters:
        None.
        
    Returns:
        string: The option chosen by the user."""
    while True:
        action = input("Do you want to...\n1. Encode\n2. Decode\n")
        if action != "1" and action != "2" :
            print("Invalid action. Try again.")
        else :
            break
    return action
            
main()