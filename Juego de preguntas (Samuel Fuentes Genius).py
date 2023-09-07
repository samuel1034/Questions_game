print ("Bienvenidos al juego de preguntas");
respuesta1 = input ("¿Quieres ir a la izquierda o a la derecha?. Escribe 'Izquierda' o 'derecha'")
if respuesta1 == "izquierda":
    print ("Respuesta erronea. Te has caido en un agujero y has perdido. Puedes volver a intentarlo");

else:
   respuesta2 = input ("Tienes que cruzar a una isla. ¿Quieres ir nadando o quieres esperar un barco para cruzar?. Escribe 'nadar' o 'esperar'")
   respuesta2 = respuesta2.lower()

if respuesta2 == 'nadar':
    print ("Respuesta erronea. Había tiburones. Has perdido. Puedes volver a intentarlo");

else:
    respuesta3= input ("Has llegado a una casa que tiene 3 puertas. Una puerta de color azul, otra de color rojo y otra puerta de color verde. ¿Qué puerta quieres abrir?. Escribe 'azul', 'rojo' o 'verde'")
    respuesta3= respuesta3.lower()

if respuesta3 == 'rojo' or respuesta3 == 'azul':
    print ("Respuesta erronea. Has perdido. Puedes volver a intentarlo");

else:
    print ("¡Enhorabuena has ganado!")

   


