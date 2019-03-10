
from CaesarShift import EncryptCaesarCypher, DecryptCaesarCypher

action = ''

def control(action):

    action = input(' >>> $control  ')
    cypher = action[:2]
    operation = action[3:5]

    action = action[6:]
    argArray = action.split(',')

    
    #text pos = 6

    if cypher == 'cc':
        if operation == 'en':
            print(EncryptCaesarCypher(argArray[0], int(argArray[1])))
            control(action)
        elif operation == 'de':
            print(DecryptCaesarCypher(argArray[0], int(argArray[1])))
            control(action)
        else:
            print('Invalid command')
            control(action)
    elif cypher == '$e':
        print('ending')
    else:
        print('Invalid command')
        control(action)
    
        
control(action)