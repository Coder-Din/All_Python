import random
effector = ['Wasya','Bear','Tiger','Dan']
verb = ['ate','liked','helped','killed']
adjective = ['awful','ugly','beautiful','gigantic']
noun = ['Trump','dragon','diamond','Obama']
def sengen():
    print(effector[random.randint(0,3)] + ' ' + verb[random.randint(0,3)] + ' ' + adjective[random.randint(0,3)] + ' ' + noun[random.randint(0,3)])
sengen()
