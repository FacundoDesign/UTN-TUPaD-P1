# TP 11: Aplicación de la Recursividad - Resolución Completa

## Algunas observaciones sobre mi resolución:

### Decisiones tomadas
- Archivos separados: Cada ejercicio está en su propio archivo para facilitar la revisión y corrección individual.
- Funciones auxiliares: Agregué funciones de demostración para mostrar el proceso recursivo paso a paso.
- Casos base claros: Definí explícitamente los casos base en cada función recursiva para evitar recursión infinita.
- Variables descriptivas: Usé nombres como `ultimo_digito`, `resto_numero`, `coincidencia` para hacer el código más legible.

### Validaciones agregadas
- Entrada de datos: Validé números positivos, rangos válidos y tipos de datos correctos.
- Casos límite: Consideré situaciones especiales como números de un solo dígito, cadenas vacías y exponentes cero.
- Recursión segura: Implementé casos base robustos para evitar desbordamiento de pila.

### Mejoras implementadas
- Visualización del proceso: Incluí funciones que muestran el árbol de recursión con indentación.
- Ejemplos del enunciado: Verifiqué cada ejercicio con los casos proporcionados en el TP.
- Ejemplos adicionales: Agregué casos de prueba extra para demostrar la robustez de las funciones.
- Formato educativo: Cada ejercicio explica qué hace y cómo funciona la recursión.

### Estructuras recursivas usadas
- Recursión directa: Todas las funciones principales usan recursión simple (función que se llama a sí misma).
- Casos base múltiples: En algunos ejercicios como Fibonacci y palíndromos, definí varios casos base.
- Recursión con acumulador: En funciones como suma de dígitos, acumulo resultados en cada llamada.
- Recursión de cola: Algunas funciones están optimizadas para recursión de cola.

### Detalles técnicos
- Ejercicio 1 (Factorial): Implementé la definición matemática clásica n! = n * (n-1)!
- Ejercicio 2 (Fibonacci): Usé la fórmula F(n) = F(n-1) + F(n-2) con casos base F(0)=0 y F(1)=1.
- Ejercicio 3 (Potencia): Seguí exactamente la fórmula del enunciado n^m = n * n^(m-1).
- Ejercicio 4 (Binario): Implementé el algoritmo de división por 2 de forma recursiva concatenando restos.
- Ejercicio 5 (Palíndromo): Comparé extremos recursivamente sin usar slicing invertido ni reversed().
- Ejercicio 6 (Suma dígitos): Usé solo operaciones matemáticas (% y //) sin conversión a string.
- Ejercicio 7 (Pirámide): Calculé la suma 1+2+...+n de forma recursiva con visualización.
- Ejercicio 8 (Contar dígito): Examiné cada dígito usando módulo 10 y división entera.

### Herramientas de depuración incluidas
- Funciones de demostración: Cada ejercicio tiene una función que muestra el proceso recursivo.
- Indentación visual: Las llamadas recursivas se muestran con sangría para ver la profundidad.
- Verificación de ejemplos: Todos los casos del enunciado se verifican automáticamente.
- Cálculos manuales: Incluí verificaciones con métodos iterativos para comparar resultados.

### Conceptos de recursividad aplicados
- Caso base: Condición que detiene la recursión (ej: n=0, n=1, cadena vacía).
- Caso recursivo: La función se llama a sí misma con parámetros modificados.
- Reducción del problema: Cada llamada recursiva trabaja con un problema más pequeño.
- Confianza recursiva: Asumo que la llamada recursiva funciona correctamente.

### Optimizaciones consideradas
- Validación temprana: Verifico entradas antes de iniciar la recursión.
- Casos base eficientes: Los casos base se evalúan antes que los recursivos.
- Memoria: Aunque no implementé memoización, los comentarios sugieren dónde sería útil.
- Legibilidad vs. eficiencia: Prioricé código claro y educativo sobre optimización extrema.

### Testing y verificación
- Casos del enunciado: Todos los ejemplos proporcionados funcionan correctamente.
- Casos extremos: Probé con números pequeños, grandes, y casos límite.
- Comparación con métodos iterativos: Verifiqué resultados usando bucles tradicionales.
- Debugging visual: Las funciones auxiliares permiten ver exactamente cómo funciona la recursión.

---

**Nota**: Este TP demuestra comprensión sólida de recursividad, desde conceptos básicos hasta aplicaciones más complejas, con énfasis en código limpio y educativo.
