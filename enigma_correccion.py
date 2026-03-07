class EnigmaMachine:
    def __init__(self):

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_I   = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.rotor_II  = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        self.rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        self.rotor_IV  = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        self.reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        
        # NOTCHES DEFINIDOS
        self.notches = ["Q", "E", "V", "J"]
        self.rotor_position = [0, 0, 0, 0]

    # VALIDACIÓN
    def validate_config(self, config):

        config = config.upper()

        if len(config) != 26:
            print("Error: Debe contener 26 letras.")
            return False

        if not config.isalpha():
            print("Error: Solo debe contener letras.")
            return False

        if len(set(config)) != 26:
            print("Error: No puede haber letras repetidas.")
            return False

        return True

    # MODIFICACIÓN DE ROTORES
    def modify_rotor(self, rotor_number, new_config):

        if not self.validate_config(new_config):
            return

        if rotor_number == 1:
            self.rotor_I = new_config.upper()
        elif rotor_number == 2:
            self.rotor_II = new_config.upper()
        elif rotor_number == 3:
            self.rotor_III = new_config.upper()
        elif rotor_number == 4:
            self.rotor_IV = new_config.upper()
        else:
            print("Rotor inválido.")
            return

        print("Rotor modificado correctamente.")

    # MODIFICACIÓN DE REFLECTOR
    def modify_reflector(self, new_config):

        if not self.validate_config(new_config):
            return

        self.reflector = new_config.upper()
        print("Reflector modificado correctamente.")

    # GENERADOR DE POSICIONES
    def generate_positions_from_key(self, key):

        key = key.strip().upper()

        if not key.isalpha():
            print("La clave solo debe contener letras.")
            return None

        values = [self.alphabet.index(k) for k in key]

        r1 = sum(values[::2]) % 26
        r2 = sum(values[1::2]) % 26
        r3 = sum(values) % 26
        r4 = len(values) % 26

        return [r1, r2, r3, r4]

    # CIFRADO DE CARACTERES
    def encrypt_char(self, char):

        char = char.upper()
        pos = self.alphabet.index(char)

        # PASO ADELANTE (FORWARD)
        rotors = [self.rotor_I, self.rotor_II, self.rotor_III, self.rotor_IV]
        for i, rotor in enumerate(rotors):
            pos = (pos + self.rotor_position[i]) % 26
            pos = self.alphabet.index(rotor[pos])
            pos = (pos - self.rotor_position[i]) % 26

        # REFLECTOR
        pos = self.alphabet.index(self.reflector[pos % 26])

        # PASO ATRÁS (INVERSA)
        for i, rotor in reversed(list(enumerate(rotors))):
            pos = (pos + self.rotor_position[i]) % 26
            pos = rotor.index(self.alphabet[pos])
            pos = (pos - self.rotor_position[i]) % 26

        return self.alphabet[pos % 26]

    # CIFRADO DEL MENSAJE
    def encrypt_message(self, message, key):

        # REINICIO DE POSICIÓN POR CADA MENSAJE
        positions = self.generate_positions_from_key(key)

        if positions is None:
            return None

        self.rotor_position = positions.copy()
        encrypted = ""

        for char in message:

            if char.isalpha():

                # LÓGICA DE GIRO POR NOTCHES
                n0 = self.alphabet[self.rotor_position[0]] == self.notches[0]
                n1 = self.alphabet[self.rotor_position[1]] == self.notches[1]
                n2 = self.alphabet[self.rotor_position[2]] == self.notches[2]

                # EL PRIMER ROTOR SIEMPRE GIRA
                self.rotor_position[0] = (self.rotor_position[0] + 1) % 26

                # GIRO EN CASCADA
                if n0:
                    self.rotor_position[1] = (self.rotor_position[1] + 1) % 26
                    if n1:
                        self.rotor_position[2] = (self.rotor_position[2] + 1) % 26
                        if n2:
                            self.rotor_position[3] = (self.rotor_position[3] + 1) % 26

                encrypted += self.encrypt_char(char)

            else:
                encrypted += char

        return encrypted

    # DESCIFRADO
    def decrypt_message(self, message, key):
        return self.encrypt_message(message, key)

    def display_menu(self):

        print("\n" + "="*50)
        print("MÁQUINA ENIGMA")
        print("="*50)
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Configurar rotores")
        print("4. Salir")
        print("="*50)

    def run(self):

        while True:

            self.display_menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                message = input("Ingrese mensaje a cifrar: ")
                key = input("Ingrese clave: ")
                result = self.encrypt_message(message, key)
                if result is not None:
                    print("Mensaje cifrado:", result)

            elif option == "2":
                message = input("Ingrese mensaje a descifrar: ")
                key = input("Ingrese clave: ")
                result = self.decrypt_message(message, key)
                if result is not None:
                    print("Mensaje descifrado:", result)

            elif option == "3":

                # MENÚ DE CONFIGURACIÓN
                print("\n1. Modificar Rotor I")
                print("2. Modificar Rotor II")
                print("3. Modificar Rotor III")
                print("4. Modificar Rotor IV")
                print("5. Modificar Reflector")

                sub = input("Seleccione opción: ")

                if sub in ["1", "2", "3", "4"]:
                    new_conf = input("Ingrese nueva configuración (26 letras únicas): ")
                    self.modify_rotor(int(sub), new_conf)

                elif sub == "5":
                    new_conf = input("Ingrese nueva configuración del reflector (26 letras únicas): ")
                    self.modify_reflector(new_conf)

                else:
                    print("Opción inválida.")

            elif option == "4":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

if __name__ == "__main__":
    enigma = EnigmaMachine()
    enigma.run()