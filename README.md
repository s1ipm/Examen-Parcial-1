# Máquina Enigma - Implementación en Python

Se implementa una simulación funcional de la máquina Enigma, el dispositivo de cifrado utilizado durante la Segunda Guerra Mundial. El programa está escrito íntegramente en Python y reproduce el comportamiento matemático y mecánico del sistema original, permitiendo cifrar y descifrar mensajes mediante un sistema de rotores y reflector.

### Objetivo del Programa
El programa permite a cualquier usuario introducir un mensaje de texto y una clave de cifrado para obtener una versión cifrada del mensaje original. Gracias a la propiedad recíproca de la máquina Enigma, el mismo procedimiento y la misma clave permiten recuperar el mensaje original a partir del texto cifrado.

### Fundamentos Matemáticos
El sistema trabaja con el alfabeto inglés de 26 letras mayúsculas. Cada letra se representa mediante un número según su posición en el alfabeto:

A = 0, B = 1, C = 2, ..., Z = 25

Todas las transformaciones utilizan aritmética modular con módulo 26, lo que garantiza que cualquier operación permanezca dentro del rango válido del alfabeto. Cuando un resultado supera el valor 25, se aplica el módulo para obtener un valor entre 0 y 25, manteniendo la coherencia del sistema.

### Estructura de la Clase EnigmaMachine
La clase EnigmaMachine encapsula toda la lógica de la máquina. Sus atributos principales son:

rotor_I, rotor_II, rotor_III, rotor_IV: Cadenas de 26 caracteres que representan el cableado interno de cada rotor. Cada posición en la cadena indica qué letra de salida corresponde a la letra de entrada en esa posición.

reflector: Cadena de 26 caracteres que define los pares de letras que se intercambian simétricamente.

alphabet: Cadena con el alfabeto en orden, utilizada para conversiones entre letras y números.

rotor_position: Lista de cuatro números que almacena la posición actual de cada rotor.

### Métodos Principales
#### Métodos de Validación
##### validate_config(self, config)
Este método verifica que una configuración de rotor o reflector sea válida. Comprueba tres condiciones:

La configuración debe tener exactamente 26 caracteres

Todos los caracteres deben ser letras

No puede haber letras repetidas

Estas validaciones son necesarias porque los rotores deben contener cada letra exactamente una vez para que el cifrado sea biyectivo.

### Métodos de Modificación
modify_rotor(self, rotor_number, new_config)
Permite cambiar la configuración interna de un rotor específico. Recibe el número del rotor (1 al 4) y la nueva configuración como cadena de texto. Antes de aplicar el cambio, valida la configuración usando el método anterior.

### modify_reflector(self, new_config)
Similar al método anterior, pero modifica la configuración del reflector. También realiza las validaciones correspondientes.

### Generación de Posiciones Iniciales
#### generate_positions_from_key(self, key)
Este método transforma la clave de texto en las posiciones iniciales de los rotores. El proceso sigue estas reglas:

- La clave puede tener cualquier longitud, pero el programa está optimizado para claves de hasta 4 caracteres

- Cada carácter se convierte a su valor numérico según el alfabeto

- La posición del rotor I se calcula sumando los valores en posiciones pares de la clave y aplicando módulo 26

- La posición del rotor II se calcula sumando los valores en posiciones impares de la clave y aplicando módulo 26

- La posición del rotor III es la suma de todos los valores de la clave módulo 26

- La posición del rotor IV es la longitud de la clave módulo 26

Este método devuelve una lista con las cuatro posiciones calculadas.

### Cifrado de un Carácter
#### encrypt_char(self, char)
Este método implementa el núcleo del algoritmo de cifrado para un solo carácter. El proceso sigue estos pasos:

- Conversión inicial: El carácter de entrada se convierte a su valor numérico según el alfabeto.

- Camino de ida a través de los rotores: Para cada rotor en orden (I, II, III, IV):

- Se suma la posición actual del rotor al valor de la letra, aplicando módulo 26. Esto simula el desplazamiento del rotor.

- Se aplica el cableado interno del rotor: el valor obtenido se usa como índice para encontrar la letra de salida en la configuración del rotor.

- Esa letra se convierte nuevamente a su valor numérico.

- Se resta la posición del rotor para compensar el desplazamiento inicial, aplicando módulo 26.

- Reflector: El valor obtenido después de pasar por todos los rotores se usa como índice para encontrar la letra correspondiente en el reflector. Esa letra se convierte a su valor numérico.

- Camino de regreso a través de los rotores: Se recorren los rotores en orden inverso (IV, III, II, I):

- Se suma la posición actual del rotor.

- Se busca la posición de la letra actual dentro de la configuración del rotor para obtener la letra equivalente en el camino inverso.

- Esa letra se convierte a su valor numérico.

- Se resta la posición del rotor.

- Resultado final: El número obtenido se convierte a su letra correspondiente en el alfabeto y se devuelve como carácter cifrado.

### Cifrado de Mensajes Completos
#### encrypt_message(self, message, key)
Este método coordina el cifrado de un mensaje completo:

- Genera las posiciones iniciales de los rotores a partir de la clave proporcionada.

- Inicializa el estado de la máquina con esas posiciones.

- Procesa cada carácter del mensaje:

- Si el carácter es una letra, primero actualiza las posiciones de los rotores según el mecanismo de avance, luego cifra el carácter individualmente.

- Si el carácter no es una letra (espacios, números, signos de puntuación), lo mantiene sin cambios en el mensaje cifrado.

- Devuelve el mensaje completo cifrado.

- El mecanismo de avance de rotores simula el funcionamiento de un odómetro:

- El rotor I avanza una posición después de cada letra cifrada

- Cuando el rotor I completa una vuelta (vuelve a posición 0), el rotor II avanza una posición

- Cuando el rotor II completa una vuelta, el rotor III avanza una posición

- Cuando el rotor III completa una vuelta, el rotor IV avanza una posición

- Este sistema de rotación progresiva es lo que hace que el cifrado sea polialfabético, produciendo diferentes resultados para la misma letra en diferentes posiciones del mensaje.

### Descifrado
#### decrypt_message(self, message, key)
Este método simplemente llama a encrypt_message con los mismos parámetros. La propiedad recíproca de la máquina Enigma garantiza que el proceso de cifrado y descifrado sea idéntico. Si se introduce un mensaje cifrado con la misma clave que se usó para cifrarlo, el resultado será el mensaje original.

### Interfaz de Usuario
#### display_menu(self)
Muestra un menú con las opciones disponibles para el usuario.

### run(self)
- Implementa el bucle principal del programa que:

- Muestra el menú

- Captura la opción seleccionada por el usuario

- Ejecuta la acción correspondiente (cifrar, descifrar, configurar rotores, salir)

- Maneja los errores de entrada y muestra los resultados

### Flujo de Ejecución
Cuando el usuario ejecuta el programa, ocurre lo siguiente:

- Se crea una instancia de la clase EnigmaMachine con las configuraciones predeterminadas de rotores y reflector.

- Se inicia el bucle del menú principal.

- El usuario selecciona una opción:

- Para cifrar o descifrar, ingresa el mensaje y la clave, y el programa muestra el resultado.

- Para configurar rotores, puede modificar cualquiera de los cuatro rotores o el reflector ingresando nuevas configuraciones.

- Para salir, termina la ejecución.

El programa continúa en bucle hasta que el usuario elige salir.

**Consideraciones Técnicas**
- Manejo de Errores
- El programa incluye validaciones para:

- Claves que contienen caracteres no alfabéticos

- Configuraciones de rotores con longitud incorrecta

- Configuraciones con caracteres repetidos

- Opciones de menú inválidas

En todos los casos, muestra mensajes descriptivos y permite al usuario intentar nuevamente sin interrumpir la ejecución.

### Preservación de Caracteres No Alfabéticos
El programa mantiene intactos los espacios, números y signos de puntuación en el mensaje cifrado. Solo las letras son transformadas, lo que permite que la estructura del mensaje original se conserve y el texto cifrado sea legible en términos de formato.

Flexibilidad de la Clave
Aunque el sistema está optimizado para claves de hasta 4 caracteres, acepta cualquier longitud. Para claves más largas, los cálculos de posición utilizan sumas y la longitud total, distribuyendo la información de la clave entre los cuatro rotores.
