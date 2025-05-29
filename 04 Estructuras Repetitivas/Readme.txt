# Algunas observaciones sobre mi resolución:

## Decisiones tomadas
- Archivos separados: Decidí hacer un archivo por ejercicio para que sea más fácil de revisar y corregir.
- Variables descriptivas: Usé nombres claros como `numero_secreto`, `suma_total` para que el código sea más entendible.

## Validaciones agregadas
- Entrada de datos: Agregué controles para evitar errores cuando el usuario ingresa algo incorrecto.
- Casos especiales: Consideré situaciones como números negativos y el número cero.
- Límites: En el ejercicio 8, validé que no se excedan los 100 números.

## Mejoras implementadas
- Mensajes informativos: Agregué títulos y mensajes claros para que se entienda qué hace cada programa.
- Verificaciones: En algunos ejercicios incluí verificaciones para comprobar que los cálculos están correctos.
- Flexibilidad: Los ejercicios 8 y 9 se pueden probar con pocos números cambiando una sola variable.

## Estructuras de control usadas
- FOR: Para cuando sabía exactamente cuántas veces repetir (ej: del 0 al 100).
- WHILE: Para cuando la repetición dependía de una condición (ej: hasta que adivine el número).
- WHILE True: Para validar entrada de datos hasta que sea correcta.

## Detalles técnicos
- Ejercicio 2: Usé división entera para contar dígitos en lugar de convertir a texto.
- Ejercicio 5: Agregué el módulo `random` para generar números aleatorios.
- Ejercicio 8: Incluí porcentajes y estadísticas adicionales para hacer el análisis más completo. Y agregue una version en donde el usuario tiene el control de la cantidad de nuneros a verificar.
- Ejercicio 10: Manejé correctamente los números negativos manteniendo el signo.

## Testing y depuración
- Configuré los ejercicios 8 y 9 para probar con pocos números primero.
- Agregué contadores y verificaciones para asegurarme de que todo funcione bien.
- Incluí mensajes de error claros cuando algo sale mal.
