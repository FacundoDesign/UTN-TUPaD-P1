# TP 6 - Estructuras de Datos Complejas

## Observaciones sobre mi resolución:

### Decisiones tomadas
- Archivos separados: Cada ejercicio está en un archivo individual para facilitar la revisión y comprensión.
- Variables descriptivas: Utilicé nombres claros como `precios_frutas`, `agenda_telefonica`, `contador_palabras` para mejorar la legibilidad.
- Funciones modulares: En ejercicios complejos (8 y 9) separé la lógica en funciones específicas para cada operación.
- Menús interactivos: Agregué sistemas de menú en los ejercicios 8 y 9 para una experiencia más completa.

### Validaciones agregadas
- Entrada de datos: Implementé controles con `try-except` para validar entradas numéricas y evitar errores.
- Existencia de claves: Verifico si las claves existen antes de operarlas en diccionarios.
- Datos vacíos: Uso `.strip()` para eliminar espacios en blanco de las entradas del usuario.
- Valores positivos: Validé que los stocks y cantidades sean números positivos donde corresponde.

### Mejoras implementadas
- Mensajes informativos: Cada ejercicio tiene títulos claros y mensajes explicativos.
- Estadísticas adicionales: Agregué información extra como totales, promedios y análisis comparativos.
- Ordenamiento: Utilicé `sorted()` para mostrar resultados ordenados alfabéticamente.
- Alertas inteligentes: Sistema de alertas para stock bajo en el ejercicio 8.
- Confirmaciones: Pedí confirmación para operaciones críticas como eliminar o reemplazar datos.

### Estructuras de datos utilizadas
- Diccionarios: Para mapear relaciones clave-valor (precios, contactos, agenda).
- Listas: Para almacenar colecciones ordenadas (frutas, palabras).
- Tuplas: Para datos inmutables (notas de alumnos, claves compuestas en agenda).
- Sets**: Para operaciones de conjuntos y eliminar duplicados.
- Tuplas como claves: En el ejercicio 9 para crear claves compuestas (día, hora).

### Detalles técnicos
- Ejercicio 5: Convertí texto a minúsculas con `.lower()` para evitar duplicados por mayúsculas.
- Ejercicio 6: Usé `sum()` y `len()` para calcular promedios de tuplas de notas.
- Ejercicio 7: Implementé operaciones de sets: intersección (`&`), diferencia (`-`), unión (`|`).
- Ejercicio 8: Agregué sistema de alertas basado en umbrales de stock.
- Ejercicio 9: Demostré cómo las tuplas inmutables pueden ser claves de diccionarios.
- Ejercicio 10: Utilicé `.items()` para invertir eficientemente un diccionario.

### Métodos y funciones clave utilizadas
- Diccionarios: `.keys()`, `.values()`, `.items()`, verificación con `in`
- Listas: `list()`, `sorted()`, list comprehensions
- Sets: operadores `&`, `|`, `^`, `-` para intersección, unión, diferencia
- Strings: `.split()`, `.strip()`, `.lower()`, `.capitalize()`
- Generales: `len()`, `sum()`, `max()`, `min()`

### Testing y depuración
- Datos de prueba: Incluí datos iniciales en cada ejercicio para facilitar las pruebas.
- Verificaciones: Agregué comprobaciones de integridad (ej: suma de conjuntos en ejercicio 7).
- Manejo de errores: Implementé bloques try-except para entradas inválidas.
- Mensajes de estado: Confirmaciones claras para cada operación exitosa.

### Funcionalidades extra implementadas
- Ejercicio 4: Lista de contactos disponibles cuando no se encuentra uno específico.
- Ejercicio 5: Identificación de palabra más frecuente y estadísticas adicionales.
- Ejercicio 6: Cálculo de promedio general del curso y clasificación aprobado/desaprobado.
- Ejercicio 7: Desglose detallado de quién aprobó solo cada parcial.
- Ejercicio 8: Sistema completo de gestión con múltiples operaciones.
- Ejercicio 9: Agrupación de actividades por día y eliminación de eventos.
- Ejercicio 10: Consultas bidireccionales y comparación lado a lado.

### Conceptos avanzados aplicados
- Inmutabilidad: Uso correcto de tuplas como claves de diccionarios.
- Comprehensions: List comprehensions para filtrado eficiente.
- Operaciones de conjuntos: Aplicación práctica de teoría de conjuntos.
- Modularidad: Separación de responsabilidades en funciones específicas.
- **Experiencia de usuario**: Interfaces intuitivas con menús y validaciones.
