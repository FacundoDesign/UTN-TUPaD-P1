# TP Funciones en Python

## Algunas observaciones sobre mi resolución:

Decidi elegir dos formatos de entrega para este TP: Actividades individuales y compiladas en un programa ejecutable.
En la Actividad 4, elegi usar `math.pi` en lugar de 3.14159 para tener mayor precisión en los cálculos del área y perímetro del círculo. En la Actividad 7, manejé el caso especial de división por cero devolviendo un mensaje de error en lugar de que el programa falle. La Actividad 6 (tabla de multiplicar) me gustó porque es muy visual y fácil de verificar que funciona bien. En la Actividad 8, investigué la fórmula del IMC para asegurarme de implementarla correctamente. Agregué un programa de pruebas automáticas para poder verificar todas las funciones de una vez sin tener que ingresar datos manualmente cada vez.

## Decisiones tomadas

- Modularidad: Cada función tiene una responsabilidad específica y bien definida según el principio de responsabilidad única.
- Documentación: Agregué docstrings a todas las funciones con descripción, argumentos y valores de retorno para que sea más profesional.
- Programa principal: Implementé una función `main()` interactiva que ejecuta todas las actividades en secuencia.

## Validaciones agregadas

- División por cero: En la función `operaciones_basicas()` validé que no se divida por cero y retorno un mensaje descriptivo.
- Entrada de datos: Usé `int()` y `float()` según corresponda para cada tipo de dato esperado.
- Precisión: Implementé formato de 2 decimales con `:.2f` en todos los resultados que lo requieren.

## Mejoras implementadas

- Pruebas automáticas: Creé la función `pruebas_automaticas()` que ejecuta todas las funciones con valores predefinidos para testing rápido.
- Interfaz clara: Agregué separadores visuales y títulos para cada actividad que mejoran la experiencia del usuario.
- Flexibilidad: El programa permite elegir entre modo interactivo o pruebas automáticas al inicio.
- Imports organizados: Importé `math` al inicio para las funciones trigonométricas y constantes matemáticas.

## Estructuras y conceptos aplicados

- Funciones con parámetros: Todas las funciones reciben los datos necesarios como argumentos.
- Funciones con retorno: La mayoría devuelve valores que luego se usan en el programa principal.
- Tuplas: En `operaciones_basicas()` retorno una tupla con los cuatro resultados.
- Manejo de strings: Uso de f-strings para formatear salidas de manera elegante.

## Detalles técnicos

- Actividad 4: Usé `math.pi` y `**` para potencias, más preciso y pythónico que `pow()`.
- Actividad 5: Aplicé la conversión directa dividiendo por 3600 (60*60 segundos en una hora).
- Actividad 7: Implementé el retorno de tupla para devolver múltiples valores de una sola función.
- Actividad 8: La fórmula del IMC usa **2 para elevar al cuadrado la altura.
- Actividad 9: Implementé la fórmula exacta `(celsius * 9/5) + 32` para la conversión de temperatura.

## Testing y depuración

- Valores de prueba: Las pruebas automáticas usan valores conocidos para verificar que los cálculos sean correctos.
- Casos especiales: Probé la división por cero y otros casos límite.
- Verificación manual: Los resultados se pueden verificar fácilmente con calculadora para confirmar precisión.
- Modo dual: El programa permite tanto ejecución interactiva como testing automático para facilitar las pruebas durante desarrollo.
