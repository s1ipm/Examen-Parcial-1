# Máquina Enigma en Python

Este proyecto es una simulación de la famosa máquina Enigma, creada con el lenguaje de programación Python. La Enigma era un dispositivo electromecánico usado para cifrar y descifrar mensajes secretos durante la Segunda Guerra Mundial. Su seguridad se basaba en un sistema complejo de rotores intercambiables y un reflector.

Nuestra versión en Python reproduce esa lógica usando matemáticas y programación orientada a objetos. El objetivo es que puedas entender paso a paso cómo funciona este sistema de cifrado y cómo se ha traducido a código.

---

## El Alfabeto en Números

Para que una computadora pueda trabajar con letras, primero tenemos que convertirlas a números. En este caso, usamos el alfabeto inglés de 26 letras mayúsculas y le asignamos a cada una un número:

| Letra | Número |
|-------|--------|
| A     | 0      |
| B     | 1      |
| C     | 2      |
| ...   | ...    |
| Z     | 25     |

Todas las operaciones de cifrado se hacen con estos números y se utiliza la **aritmética modular**. Esto significa que siempre que el resultado de una operación se salga del rango 0-25, se le da la vuelta como si fuera un reloj de 26 horas. Esto se representa con la operación **módulo 26** y nos asegura que siempre obtengamos una letra válida.

---

## Los Componentes

Imagina que la letra que quieres cifrar es un pequeño explorador que viaja por un circuito eléctrico dentro de la máquina. En su viaje, se encontrará con estos elementos:

### 1. Los Rotores
Son ruedas con 26 contactos, uno por cada letra, pero con un cableado interno que las desordena. Cada rotor tiene dos caras: la de entrada y la de salida. Cuando una letra entra al rotor, la conexión interna la transforma en una letra diferente. Además de esto, los rotores giran como el cuentakilómetros de un coche: después de cifrar cada letra, el primer rotor avanza una posición.

### 2. El Reflector
Es como un espejo especial. Al final del camino, el explorador llega al reflector, que lo devuelve por un camino diferente pero relacionado. El reflector conecta pares de letras: por ejemplo, si la letra A entra, podría salir como Z, y si entra Z, saldría como A. Esta conexión es fija y simétrica.

### 3. El Tablero de Conexiones (En nuestro caso, la clave)
Para que la máquina funcione, los rotores deben empezar en una posición concreta. Esa posición inicial es lo que llamamos **clave**. En este programa, la clave es una palabra de cuatro letras como por ejemplo **CVEA**. Cada letra indica la posición de arranque de un rotor:

- **C** define el punto de partida del Rotor I
- **V** define el punto de partida del Rotor II
- **E** define el punto de partida del Rotor III
- **A** define el punto de partida del Rotor IV

---

## El Viaje de una Letra: Paso a Paso

Vamos a seguir a nuestro explorador (la letra que queremos cifrar) en su recorrido:

1.  **Conversión:** La letra se convierte en su número correspondiente (por ejemplo, la A se convierte en 0).

2.  **A través de los rotores (Ida):** La señal entra en el primer rotor. Primero se suma la posición actual de ese rotor para saber dónde conecta. Después, el cableado interno del rotor transforma ese número en otro completamente distinto. Este proceso se repite con el segundo, tercer y cuarto rotor, en ese orden.

3.  **El Rebote en el Reflector:** Al salir del último rotor, la señal llega al reflector. El reflector intercambia el número por su pareja predefinida.

4.  **El Viaje de Vuelta (Rotores Inversos):** Ahora la señal emprende el camino de regreso, pero esta vez a través de los rotores en orden inverso: cuarto, tercero, segundo y primero. En esta dirección, primero se aplica el cableado inverso del rotor y luego se resta la posición en la que se encontraba ese rotor en ese momento.

5.  **Letra Cifrada:** El número que obtenemos al final del viaje se convierte de nuevo en una letra, y esa es la letra cifrada.

---

## La Propiedad Recíproca

Lo fascinante de este diseño es que es **recíproco**. Esto significa que el proceso es exactamente el mismo para cifrar que para descifrar. Si le das un mensaje cifrado a la máquina y usas la misma clave de inicio, el viaje que hará cada letra la devolverá a su forma original.

---

## La Rotación de los Rotores

Lo que hace a Enigma tan especial es que los rotores se mueven:

- Después de cifrar cada letra, el **primer rotor avanza una posición**.
- Cuando el primer rotor da una vuelta completa (de 26 pasos), hace que el **segundo rotor avance una posición**.
- Y así sucesivamente, como los dígitos de un cuentakilómetros.

Esto significa que la misma letra en el mensaje original se cifrará de forma diferente cada vez que aparezca, porque los rotores están en una posición distinta. Esto se conoce como **cifrado polialfabético** y era lo que hacía tan difícil descifrar los mensajes Enigma sin conocer la clave inicial.

---

## Funcionamiento

Todo el funcionamiento de la máquina está organizado dentro de una única clase en Python llamada **`EnigmaMachine`**. Esta clase guarda toda la información importante: la configuración de los rotores, la del reflector, el alfabeto y, lo más importante, la posición actual de cada rotor en cada momento.

Dentro de esta clase, hay **métodos** (funciones) que realizan tareas específicas:

- **`encrypt_char`:** Es el método que sabe exactamente cómo guiar a una **sola letra** a través de todo el viaje que hemos descrito.
- **`encrypt_message`:** Se encarga de coger un **mensaje completo**, letra por letra. Para cada letra, llama a `encrypt_char` y luego actualiza la posición de los rotores para la siguiente letra.
- **`decrypt_message`:** Hace exactamente lo mismo que `encrypt_message`. Gracias a la propiedad recíproca, cifrar y descifrar son la misma operación.

Además, el programa incluye un menú sencillo en la consola para que puedas interactuar con él: cifrar mensajes, cambiar la clave o las configuraciones de los rotores.
