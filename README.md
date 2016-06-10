# PochaCompetition

[![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/Rsilnav/PochaCompetition)

## Introducción
Competición de Inteligencias Artificiales jugando a la [Pocha](https://es.wikipedia.org/wiki/Pocha_%28juego_de_naipes%29), un juego de cartas bastante común en España.

## Normas
Se pide juego limpio en base a las siguientes normas:

- Todos los jugadores deben seguir el palo de inicio, y superando a la carta más alta que haya de ese palo sobre la mesa, si es posible.

- Si un jugador no tiene ninguna carta del palo de inicio, debe echar triunfo (lo que comúnmente se conoce como fallar).

- En caso de no tener ninguna carta ni del palo de inicio ni de triunfo, se puede echar cualquier carta de cualquiera de los dos palos restantes.

- Si un jugador ha fallado previamente, los demás tienen que seguir el palo de inicio aunque ya no es preciso que superen ninguna carta ya que no optan a ganar la baza.

- Si un jugador ha fallado previamente y nosotros tampoco tenemos ninguna carta del palo de inicio, estamos obligados a fallar, solo si tenemos un triunfo superior al más alto que haya sobre la mesa. En caso contrario, no se está obligado a desperdiciar el triunfo (aunque se podría hacer si al jugador le interesara).

## Entornos
Habrá dos tipos distintos de situaciones jugables no diferenciables internamente (el programa no debería cambiar según sea una u otra):

- Cuatro jugadores. Posiciones aleatorias al inicio de la partida. Baraja aleatoria en cada ronda. Número de bazas variables, comenzando en una cubierta, llegando a diez cartas cubiertas, y volviendo a bajar a una. Solo se juega una ronda de diez cartas. 

- Cuatro jugadores. Baraja estática durante X partidas, al igual que las posiciones; ambas se aleatorizan una vez inicial. Bazas no variables, se reparten siempre el mismo número de cartas. El número de rondas a jugar será de mínimo 100 para permitir el aprendizaje.

En ambos experimentos, los jugadores pueden mantener memoria de las partidas anteriores y tomar decisiones en base a ello.

## Puntuaciones
Los puntos se dan de la siguiente manera:
- 10 puntos si se acierta en el número de bazas, incluido si no se pidió nada.
- 5 más por cada baza acertado en caso de haber coincidido.
- -5 por cada baza de diferencia con las apostadas si no ha coincidido (y evitando sumar lo anterior).

## Programación
El jugador solo podrá acceder a los datos que en una partida real podría ver, cartas sobre la mesa (jugadas), apuestas realizadas y bazas ganadas; así como los puntos de cada jugador.

__Se supone que nadie tratará de hacer trampas (Aunque podrá comprobarse y penalizar al infractor)__

El código de los jugadores debe implementar la interfaz dada y todas sus funciones, así como solamente hacer uso de la información pasada como parámetros. Debe devolver estructuras de datos acordes a la documentación de la misma.

Se permite todo tipo de acercamientos y algoritmos (Aleatorios, Tontos, Voraces, Redes neuronales, etc.) mientras cumpla las normas especificadas.

## Terminología
El código esqueleto está en inglés, y se usa la siguiente terminología:
- Round: Cada una de las rondas del juego.
- Turn: Cada una de las bazas de una ronda, es comenzada por el jugador ganador de la baza anterior, salvo en el caso de la primera baza, que se va rotando por rondas.
- Trump: Triunfo o pinte, carta que marca el palo que se sigue en la ronda.