import threading
import random

import time

def equipo1():
    
    for i in range (1 ):
        
        
            

        print(f"jugador/a  equipo 1: juan \n ( le da el testigo a pedro)\n")
        time.sleep(1.0)

        print(f"jugador/a  equipo 1: pedro\n( recibe  el testigo de  juan )\n ( le da el testigo a pepe)\n")
        time.sleep(1.0)

        print(f"jugador/a  equipo 1: pepe \n( recibe  el testigo de pedro ) \n ( le da el testigo a fernanda )\n")
        time.sleep(1.0)

        print(f"jugador/a  equipo 1: fernanda\n ( recibe  el testigo de  pepe)\n  ")
        time.sleep(1.0)
            


def equipo2():
    for i in range (1 ):
        

        
            

        print(f"jugador/a equipo 2: ana \n( le da el testigo a vali)\n ")
        time.sleep(1.0)

        print(f"jugador/a equipo 2: vali \n( recibe el testigo de  ana )\n ( le da el testigo a carolina )\n")
        time.sleep(1.0)

        print(f"jugador/a equipo 2: carolina \n ( recibe el testigo de  vali )\n ( le da el testigo a cara )\n")
        time.sleep(1.0)

        print(f"jugador/a equipo 2: cara \n( recibe el testigo de  carolina  )\n ")
        time.sleep(1.0)
            


hilo_equipos1 = threading.Thread(target=equipo1)
hilo_equipo2 = threading.Thread(target=equipo2)


hilo_equipos1.start()
hilo_equipo2.start()

hilo_equipos1.join()
hilo_equipo2.join()

print("la carrera ha terminado ")