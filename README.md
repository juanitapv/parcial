# Proyecto: Sopa de Letras-Por: Juanita Prado

Dada una supa de letras se creo un algoritmo que permita solucionar la sopa de letras. Es decir, que encuentre las palabras de una lista dada y que luego cree un reporte de aquellas palabras de la lista que estan en la sopa de letras(True) y aquellas que no lo estan(False) **Visual Studio Code**.

## Archivos del Proyecto

- **`arch.txt`**: Contiene la sopa de letras y las palabras a buscar.
- **`arch.json`**: Archivo de salida en formato JSON que indica si las palabras fueron encontradas o no.
- **`arch.py`**: Script principal que procesa la sopa de letras y genera el archivo JSON.

## Estructura del Proyecto

1. **`arch.txt`**:  
   Formato del archivo:A M A R S
S T E R I
O M A Z C
A L C R H
P O L O S
---
AMAR
OSA
SOLO
POLOS
MEZCLAR
PALO


- La cuadrícula de letras está separada por espacios.
- Las palabras a buscar están separadas por líneas después de `---`.

2. **`arch.py`**:  
Contiene funciones para:
- Leer y procesar el archivo `arch.txt`.
- Buscar palabras en la sopa de letras en direcciones horizontales y verticales.
- Generar un archivo JSON con los resultados.

3. **`arch.json`**:  
Archivo de salida que muestra los resultados en formato JSON:
```json
{
    "AMAR": true,
    "OSA": true,
    "SOLO": true,
    "POLOS": true,
    "MEZCLAR": false,
    "PALO": false
}
```

## Requisitos

1. **Version de python**:
   ```
   python --version
   ```
2. **Biblioteca de python**
  - `json`

##Ejecución del programa

1. **Clonar repositorio desde view-terminal en nueva carpeta**:
    ```
   git clone https://github.com/juanitapv/parcial.git
    ```
2. **Asegura que se este en un ruta correcta**
    ```
    cd parcial 45\parcial45
    ```
3. **Archivo a ejecutar**
    ```
    python arch.py
    ```
