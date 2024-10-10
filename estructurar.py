import os

# Función para crear carpetas y archivos
def crear_estructura():
    # Definir la estructura de carpetas y archivos
    estructura = {
        'referentes_bibliograficos': [
            'bibliografia.md',
            'libros.md',
            'articulos.md',
            'tesis.md',
            'videos.md'
        ],
        'eventos_academicos': [
            'humanos_xxi_2024.md',
            'otros_eventos.md',
            'participaciones_futuras.md'
        ],
        'conceptos_matematicos': [
            'algebra.md',
            'geometria.md',
            'calculo.md',
            'logica.md',
            'probabilidad_estadistica.md'
        ],
        'logros_didactica': [
            'estrategias_ensayo_error.md',
            'recursos_tecnologicos.md',
            'enfoques_colaborativos.md',
            'metodos_participacion_activa.md'
        ]
    }

    # Crear carpetas y archivos
    for carpeta, archivos in estructura.items():
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crear carpeta
            print(f'Carpeta creada: {carpeta}')
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, 'w') as f:
                f.write(f'# {archivo.replace("_", " ").title()}\n\n')  # Título para cada archivo
                print(f'Archivo creado: {ruta_archivo}')

    # Crear el archivo README.md en el directorio principal
    with open('README.md', 'w') as readme:
        contenido_readme = '''# Línea Investigativa: Pedagogía y Didáctica de la Matemática

Este repositorio contiene la documentación de mi línea investigativa en el área de la pedagogía y didáctica de la matemática. Se incluyen referencias bibliográficas, participaciones en eventos académicos, conceptos matemáticos clave y logros alcanzados en la enseñanza.

## Estructura del repositorio

- `/referentes_bibliograficos/`: Contiene las lecturas y fuentes consultadas.
- `/eventos_academicos/`: Documenta mi participación en eventos académicos.
- `/conceptos_matematicos/`: Desarrolla conceptos matemáticos relevantes.
- `/logros_didactica/`: Relata los logros en la enseñanza de la matemática.

## Contribuciones

Se aceptan sugerencias y colaboraciones para mejorar este repositorio.
'''
        readme.write(contenido_readme)
        print('Archivo README.md creado.')

# Ejecutar la función para crear la estructura
if __name__ == '__main__':
    crear_estructura()
