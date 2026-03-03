class EnigmaMachine:

    def __init__(self):

        self.rotor_I   = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        self.rotor_II  = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        self.rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        self.rotor_IV  = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        self.reflector = "YRUHQSLOPXNGOKMIEBFZCWVJAT"

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Posiciones de los rotores
        self.rotor_position = [0, 0, 0, 0]

# REACTIFICACIONES

    def validate_key(self, key):
        if len(key) < 4:
            print("Error: La clave debe tener al menos 4 caracteres.")
            return False
        return True


    def validate_rotor_config(self, config):
        config = config.upper()

        if len(config) != 26:
            print("Error: Debe contener 26 letras.")
            return False

        if len(set(config)) != 26:
            print("Error: Contiene letras repetidas.")
            return False

        return True

# CONTEO DE CARÁCTERES

    def encrypt_char(self, char):

        if not char.isalpha():
            return char

        char = char.upper()

        # Convertir letra al índice
        pos = self.alphabet.index(char)

        # Rotor I
        pos = (pos + self.rotor_position[0]) % 26
        pos = self.alphabet.index(self.rotor_I[pos])

        # Rotor II
        pos = (pos + self.rotor_position[1]) % 26
        pos = self.alphabet.index(self.rotor_II[pos])

        # Rotor III
        pos = (pos + self.rotor_position[2]) % 26
        pos = self.alphabet.index(self.rotor_III[pos])

        # Rotor IV
        pos = (pos + self.rotor_position[3]) % 26
        pos = self.alphabet.index(self.rotor_IV[pos])

        # ---------------- REFLECTOR ----------------
        pos = self.alphabet.index(self.reflector[pos])

        # ---------------- BACKWARD ----------------
        pos = self.rotor_IV.index(self.alphabet[pos])
        pos = (pos - self.rotor_position[3]) % 26

        pos = self.rotor_III.index(self.alphabet[pos])
        pos = (pos - self.rotor_position[2]) % 26

        pos = self.rotor_II.index(self.alphabet[pos])
        pos = (pos - self.rotor_position[1]) % 26

        pos = self.rotor_I.index(self.alphabet[pos])
        pos = (pos - self.rotor_position[0]) % 26

        return self.alphabet[pos]

# CIFRADO

    def encrypt_message(self, message, key):

        if not self.validate_key(key):
            return None

        key = key.upper()

        # Inicializar posiciones según clave
        self.rotor_position = [
            self.alphabet.index(key[0]),
            self.alphabet.index(key[1]),
            self.alphabet.index(key[2]),
            self.alphabet.index(key[3])
        ]

        encrypted = ""

        for char in message:

            # Primero ciframos
            encrypted += self.encrypt_char(char)

            # Luego rotamos (stepping correcto)
            self.rotor_position[0] = (self.rotor_position[0] + 1) % 26

            if self.rotor_position[0] == 0:
                self.rotor_position[1] = (self.rotor_position[1] + 1) % 26

            if self.rotor_position[1] == 0:
                self.rotor_position[2] = (self.rotor_position[2] + 1) % 26

            if self.rotor_position[2] == 0:
                self.rotor_position[3] = (self.rotor_position[3] + 1) % 26

        return encrypted

    # DESCIFRAR

    def decrypt_message(self, message, key):
        return self.encrypt_message(message, key)

    # CONFIGURACIONES

    def modify_rotor(self, rotor_number, new_config):

        if not self.validate_rotor_config(new_config):
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


    def modify_reflector(self, new_config):

        if not self.validate_rotor_config(new_config):
            return

        self.reflector = new_config.upper()
        print("Reflector modificado correctamente.")

# MENÚ

    def display_menu(self):
        print("\n" + "="*50)
        print("MÁQUINA ENIGMA")
        print("="*50)
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Configuraciones")
        print("4. Salir")
        print("="*50)


    def run(self):

        while True:

            self.display_menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                message = input("Ingrese mensaje a cifrar: ")
                key = input("Ingrese clave (mín. 4 letras): ")
                result = self.encrypt_message(message, key)

                if result:
                    print("Mensaje cifrado:", result)

            elif option == "2":
                message = input("Ingrese mensaje a descifrar: ")
                key = input("Ingrese clave (mín. 4 letras): ")
                result = self.decrypt_message(message, key)

                if result:
                    print("Mensaje descifrado:", result)

            elif option == "3":
                print("\n1. Modificar Rotor I")
                print("2. Modificar Rotor II")
                print("3. Modificar Rotor III")
                print("4. Modificar Rotor IV")
                print("5. Modificar Reflector")

                sub = input("Seleccione opción: ")

                if sub in ["1","2","3","4"]:
                    new_conf = input("Ingrese nueva configuración: ")
                    self.modify_rotor(int(sub), new_conf)

                elif sub == "5":
                    new_conf = input("Ingrese nueva configuración del reflector: ")
                    self.modify_reflector(new_conf)

            elif option == "4":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

if __name__ == "__main__":
    enigma = EnigmaMachine()
    enigma.run()

