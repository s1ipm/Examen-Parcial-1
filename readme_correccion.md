# Examen Máquina Enigma
Se describe la estructura y el funcionamiento del simulador de la Máquina Enigma implementado en Python. El código emula el proceso de cifrado rotatorio, incluyendo la gestión de múltiples rotores, un reflector y el sistema de muescas (notches) para el avance mecánico.

## 1. Estructura de la Clase y Configuración Inicial
La clase EnigmaMachine centraliza toda la lógica del dispositivo. En su método de inicialización se definen los componentes fundamentales:

- Alfabeto de Referencia: Una cadena estándar de 26 letras utilizada para indexar las posiciones.
- Cableado de Rotores: Se definen cuatro rotores (I, II, III y IV) con permutaciones específicas que determinan cómo se sustituye cada letra.
- Reflector: Un componente fijo que desvía la señal de vuelta a través de los rotores, garantizando que el proceso sea recíproco.
- Sistema de Notches: Una lista que almacena la letra específica en la que cada rotor activa el giro del siguiente.

## 2. Métodos de Validación y Configuración
El código incluye mecanismos para asegurar que el usuario ingrese configuraciones válidas para el sistema:

### Validación de Configuración
El método validate_config verifica tres condiciones críticas antes de aceptar un nuevo alfabeto para los rotores o el reflector:

- Que la longitud sea exactamente de 26 caracteres.
- Que todos los caracteres sean letras del alfabeto.
- Que no existan letras repetidas, asegurando una permutación completa.

### Modificación de Componentes
Los métodos modify_rotor y modify_reflector permiten al usuario alterar el cableado interno de la máquina en tiempo de ejecución, siempre y cuando pasen la validación previa.

## 3. Generación de Posiciones y Clave
El método generate_positions_from_key transforma una clave alfabética (palabra secreta) en valores numéricos que representan la posición inicial de los rotores:

- Utiliza una lógica de saltos y sumas basadas en los índices del alfabeto.
- Asigna posiciones iniciales específicas a cada uno de los cuatro rotores.
- Esto garantiza que el cifrado dependa totalmente de la clave proporcionada por el usuario.

## 4. Lógica de Giro y Avance (Notches)
Dentro de encrypt_message, se implementa el movimiento mecánico de la máquina:

- Giro Constante: El primer rotor avanza una posición con cada letra procesada.
- Movimiento en Cascada: Antes de cifrar cada carácter, el sistema verifica si los rotores actuales están en su posición de "notch" (muesca).
- Activación: Si el rotor anterior alcanza su muesca, el siguiente rotor avanza una posición. Esto emula el sistema de trinquetes de la máquina real, permitiendo un ciclo de permutaciones extremadamente largo.

## 5. Proceso de Cifrado y Descifrado
El proceso técnico de transformar un carácter se divide en tres etapas dentro de encrypt_char:

**Paso Adelante (Forward)**
La señal eléctrica viaja desde el teclado a través de los cuatro rotores. En cada rotor, la letra se desplaza según la posición actual del mismo, se sustituye según su cableado interno y se vuelve a desplazar para salir hacia el siguiente rotor.

**Reflector**
Al llegar al final, la señal pasa por el reflector, que intercambia la letra por otra y la envía de regreso. Esto permite que el descifrado se realice con la misma configuración que el cifrado.

**Paso Atrás (Inversa)**
La señal regresa a través de los rotores en orden inverso (IV al I). En esta etapa, el código busca el índice de la letra en el cableado del rotor para realizar la operación inversa a la del paso inicial.

## 6. Interfaz de Usuario y Menú
El método run gestiona la interacción con el usuario mediante un menú en consola:

- Cifrar/Descifrar: Solicita un mensaje y una clave, reiniciando las posiciones de los rotores al inicio de cada mensaje para asegurar la consistencia del algoritmo.
- Configuración: Permite personalizar cada rotor y el reflector de manera individual.
- Persistencia de Caracteres: El sistema solo cifra letras; los espacios y caracteres especiales se mantienen intactos en el mensaje resultante.
