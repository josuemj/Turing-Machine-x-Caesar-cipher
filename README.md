# Proyecto de Simulación de Máquina de Turing - Cifrado César

Este proyecto implementa una simulación de una máquina de Turing en Python para encriptar y desencriptar mensajes mediante el cifrado César. La arquitectura sigue el modelo MVC (Modelo-Vista-Controlador) y devuelve los resultados en formato JSON. Este README describe cada módulo del proyecto y proporciona un JSON de ejemplo para configurar la máquina de Turing.

## Estructura del Proyecto

### 1. Módulo `model.py` - Lógica de la Máquina de Turing

Este módulo contiene la implementación de las clases de la máquina de Turing para el cifrado y descifrado de mensajes usando el cifrado César. Se definen dos clases principales:

- **`TuringMachineEncrypt`**: Simula la máquina de Turing para el cifrado César.
- **`TuringMachineDecrypt`**: Simula la máquina de Turing para el descifrado César.

Cada clase contiene métodos para realizar el desplazamiento de letras basado en la clave de cifrado, implementando el cifrado César.

#### Funciones principales:
- **`encrypt_message(key, machineTuring, message)`**: Aplica el desplazamiento César a un mensaje utilizando la clave indicada.
- **`decrypt_message(key, machineTuring, encrypted_message)`**: Aplica el desplazamiento inverso para restaurar el mensaje original.

### 2. Módulo `view.py` - Interfaz de Entrada y Salida

Este módulo gestiona la entrada y salida de datos para la máquina de Turing. Proporciona funciones para cargar el archivo de entrada y mostrar el resultado en formato JSON.

#### Funciones principales:
- **`load_input()`**: Lee y retorna el archivo JSON que contiene la estructura de la máquina de Turing y el mensaje para encriptar o desencriptar.

### 3. Módulo `controller.py` - Controlador

Este módulo conecta el modelo y la vista. Coordina las operaciones de encriptación y desencriptación, procesando la entrada y mostrando la salida.

#### Funciones principales:
- **`process_encryption(key, machineTuring, encrypted_message)`**: Extrae la información de la entrada y utiliza el modelo para cifrar el mensaje.
- **`process_decryption(key, machineTuring, encrypted_message)`**: Extrae la información de la entrada y utiliza el modelo para descifrar el mensaje.
- **`handle_request(key, machineTuring, encrypted_message action)`**: Controla la ejecución de la encriptación o desencriptación, devolviendo el resultado en JSON a través de la vista.

### 4. Módulo de Pruebas `tests.py`

Contiene pruebas unitarias para validar las operaciones de encriptación y desencriptación de mensajes, utilizando diferentes llaves y mensajes. Esto garantiza que los módulos funcionen de acuerdo con lo esperado y que el JSON generado sea válido.

## Formato del Archivo JSON

El archivo JSON define la estructura de la máquina de Turing, incluyendo estados, alfabeto, estado inicial, y la tabla de transiciones. A continuación, se presenta un ejemplo de configuración en JSON:

```json
{
  "Q": ["q0", "q1", "q_accept"],
  "Σ": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "],
  "Γ": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N
