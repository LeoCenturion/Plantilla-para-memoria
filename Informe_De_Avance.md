# Informe de Avance

**Título del Trabajo:** Predicción de series de tiempos aplicado al trading de criptomonedas usando la arquitectura de Transformers
 
**Autor:** Ing. Martín Leonardo Centurión
 
**Director del trabajo:** Camilo Argoty
 
---

## 1. Breve resumen del trabajo realizado hasta la fecha

El presente Trabajo Final tiene como objetivo principal estudiar, en el contexto de análisis y predicción de series de tiempo, el desempeño de la arquitectura de *Transformers* aplicada a un sistema de trading de criptomonedas. Se busca no solo obtener un rendimiento superior al de estrategias tradicionales, sino también gestionar y regular el nivel de riesgo incurrido.

El proyecto se encuentra en una fase avanzada, habiendo completado la etapa de investigación teórica y la fase de experimentación y *backtesting* de las distintas estrategias propuestas. Se ha realizado un profundo estudio del estado del arte tanto en el dominio de los Transformers aplicados a series de tiempo como en las metodologías de Machine Learning específicas para el dominio financiero.

**Situación Actual y Avances Clave:**

A la fecha, se ha concluido con la implementación y evaluación de un amplio espectro de modelos, que sirven como punto de referencia para la estrategia basada en Transformers. Los principales logros son:

1.  **Estudio Exhaustivo del Dominio:** Se completó una extensa revisión bibliográfica que abarca desde los fundamentos del trading algorítmico y el análisis técnico, hasta las arquitecturas más recientes de Transformers (Informer, Autoformer, PatchTST) y las mejores prácticas en finanzas cuantitativas (Diferenciación Fraccional, Triple Barrera, Purged K-Fold CV).

2.  **Procesamiento de Datos:** Se obtuvieron y procesaron los datos históricos de cotizaciones horarias para el par BTCUSDT desde 2020 hasta 2025 desde la API de Binance.

3.  **Implementación de Estrategias *Baseline*:**
    *   **Estrategias Estáticas:** Se implementaron y optimizaron (mediante búsqueda Bayesiana) múltiples estrategias clásicas como *Moving Average Crossover*, Bandas de Bollinger, MACD y *MultiIndicatorStrategy*.
    *   **Modelos Estadísticos:** Se evaluaron modelos como ARIMA y Prophet, aplicados sobre los retornos del activo.
    *   **Machine Learning Clásico:** Se entrenaron y evaluaron modelos como Random Forest y XGBoost, utilizando diversas técnicas de *feature engineering* y etiquetado para predecir la dirección del precio.

4.  **Implementación del Modelo Transformer:** Se implementó y evaluó un modelo basado en la arquitectura Transformer (Chronos) para la misma tarea de predicción.

5.  **Resultados Preliminares:** La fase de *backtesting* ha sido completada, y los resultados han sido consolidados. Sorprendentemente, y en línea con parte de la literatura académica reciente, el modelo Transformer (Chronos) no logró superar a estrategias más simples como el *Buy & Hold* o a modelos de ML clásico como XGBoost en las métricas definidas (Sharpe Ratio y F1 Score). Este hallazgo, aunque negativo en términos de rendimiento de la estrategia, es un resultado central y de gran valor para el trabajo.

**Dificultades Encontradas y Próximos Pasos:**

La principal dificultad encontrada fue el bajo rendimiento del modelo Transformer, que demostró ser incapaz de superar un *baseline* aleatorio. Esto sugiere una alta propensión al sobreajuste o una inadecuada configuración para este problema específico.

Los próximos pasos se centran en el análisis profundo de estos resultados y la redacción de la memoria final:
*   Analizar en detalle las posibles causas del bajo rendimiento del modelo Transformer.
*   Documentar exhaustivamente la metodología y los resultados de todos los experimentos.
*   Redactar las conclusiones del trabajo y proponer líneas de investigación futuras, como la exploración de arquitecturas más robustas (ej. PatchTST) y metodologías de validación más estrictas.

Se estima que, dado que la fase experimental ha concluido, el tiempo restante es suficiente para completar la redacción de la memoria y la documentación del proyecto antes del inicio del Taller de Trabajo Final.

## 2. Avance en las tareas

A continuación, se detalla el estado de las tareas según lo definido en el plan de proyecto original.

| Tarea | Estado |
| :--- | :---: |
| **1.0 Estudio del dominio del problema (176 h)** | <div style="background-color:green; text-align:center;">$ --</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**1.1 Búsqueda de bibliografía (8 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**1.2 Estudio sobre trading (40 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**1.3 Estudio sobre indicadores y análisis técnico (40 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**1.4 Estudio sobre trading algorítmico (30 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;1.5 Estudio sobre análisis de series de tiempo I (24 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;1.6 Estudio sobre análisis de series de tiempo II (24 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;1.7 Estudio sobre compra/venta de criptomonedas (10 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| **2.0 Procuración y análisis de datos (38 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**2.1 Obtención de datos (3 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**2.2 Análisis y tratamiento (10 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**2.3 Exploración y visualización inicial (15 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**2.4 Entrenamiento y selección de un modelo simple (10 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| **3.0 Exploración de métodos tradicionales y estado del arte (150 h)** | <div style="background-color:green; text-align:center;">$$ +</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.1 Métodos tradicionales I (25 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.2 Métodos tradicionales II (25 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3 Estado del arte I (25 h) | <div style="background-color:green; text-align:center;">$$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.4 Estado del arte II (25 h) | <div style="background-color:green; text-align:center;">$$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.5 Entrenamiento y selección de modelos (30 h) | <div style="background-color:green; text-align:center;">$ +</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;3.6 Visualización y exploración (20 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| **4.0 Exploración del uso de transformers en series de tiempo (100 h)** | <div style="background-color:yellow; text-align:center;">$$ +</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**4.1 Investigación redes neuronales, transformers (20 h)** | <div style="background-color:green; text-align:center;">$$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**4.2 Entrenamiento y selección de modelos (50 h)** | <div style="background-color:yellow; text-align:center;">$ +</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**4.3 Visualización y exploración (20 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;**4.4 Comparativa con estado del arte (10 h)** | <div style="background-color:green; text-align:center;">$ =</div> |
| **5.0 Implementación del sistema de trading (100 h)** | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1 Integración con la API del exchange para compra/venta (20 h) | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.2 Parametrización de las variables riesgo, monto, etc. (15 h) | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.3 Integración con la API del exchange para cotizaciones (15 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4 Implementación de la lógica de decisión (15 h) | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.5 Integración con el modelo (10 h) | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.6 Productización de la CLI (15 h) | <div style="background-color:green; text-align:center;">$ =</div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.7 Desarrollo de la lógica de monitorización (20 h) | <div style="background-color:yellow; text-align:center;"></div> |
| &nbsp;&nbsp;&nbsp;&nbsp;5.8 Documentación (5 h) | <div style="background-color:yellow; text-align:center;"></div> |
| **6.0 Escritura de las memorias (50 h)** | |


## 3. Cumplimiento de los requerimientos

| Requerimiento | Estado |
| :--- | :---: |
| **Req Funcionales** | |
| 1.1 El sistema debe poder operar de forma autónoma. | <div style="background-color:yellow;"></div> |
| 1.2 El usuario debe poder ingresar credenciales. | <div style="background-color:green;"></div> |
| 1.3 El sistema debe poder detenerse de forma segura. | <div style="background-color:green;"></div> |
| 1.4 El sistema debe tener parámetros configurables de riesgo. | <div style="background-color:yellow;"></div> |
| 1.5 Se le puede definir un monto máximo. | <div style="background-color:yellow;"></div> |
| **Req de Documentación** | |
| 2.1 Documentado como iniciar y detener el sistema. | <div style="background-color:yellow;"></div> |
| 2.2 Documentado los parámetros de configuración. | <div style="background-color:yellow;"></div> |
| **Req de Testing** | |
| 3.1 Tests de integración contra la API del exchange. | <div style="background-color:yellow;"></div> |
| 3.2 Tests de componente que validen las reglas de negocio. | <div style="background-color:green;"></div> |
| 3.3 El modelo será evaluado según su capacidad predicativa. | <div style="background-color:green;"></div> |
| 3.4 Se diseñará una forma de monitorizar el rendimiento. | <div style="background-color:yellow;"></div> |
| **Req de Interfaz** | |
| 4.1 El sistema proveerá una interfaz de línea de comandos (CLI). | <div style="background-color:green;"></div> |
| 4.2 La CLI será clara en sus errores. | <div style="background-color:green;"></div> |


## 4. Gestión de riesgos

| Riesgo | Estado |
| :--- | :---: |
| Riesgo #1: La arquitectura de Transformers no es adecuada. | <div style="background-color:red;"></div> |
| Riesgo #2: Se requiere de hardware especializado. | <div style="background-color:yellow;"></div> |
| Riesgo #3: La integración con la API del exchange es arancelada. | <div style="background-color:green;"></div> |
| Riesgo #4: La comisión para las transacciones incrementa. | <div style="background-color:green;"></div> |
| Riesgo #5: Deja de funcionar la computadora de desarrollo. | <div style="background-color:green;"></div> |

**Análisis de los Riesgos Modificados:**

**Riesgo #1: La arquitectura de Transformers no es adecuada para la predicción de series de tiempo en el contexto de las criptomonedas.** (S:10, O:3, RPN:30 -> **S\*:6, O\*:3, RPN\*:18**)
- **Justificación:** Este riesgo se ha manifestado parcialmente. Los resultados del modelo Chronos fueron pobres. Sin embargo, el plan de mitigación (explorar otros modelos estadísticos y de *deep learning*) fue ejecutado en etapas previas, proporcionando alternativas viables (como XGBoost) y resultados concretos para el trabajo final. Aunque el modelo central no fue efectivo, el objetivo de "estudiar el desempeño" se cumplió y se generaron conclusiones valiosas. El riesgo se considera ahora **Crítico** pero controlado, ya que el proyecto puede concluir exitosamente con estos hallazgos.

**Riesgo #2: Se requiere de hardware especializado o de gran poder de cómputo para entrenar los modelos de redes neuronales.** (S:5, O:5, RPN:25 -> **S\*:3, O\*:5, RPN\*:15**)
- **Justificación:** Se ha comprobado que, si bien el entrenamiento de los modelos de ML es intensivo, no ha requerido hardware que exceda las capacidades de una estación de trabajo moderna o servicios en la nube accesibles. La mitigación (contratar un servicio cloud si es necesario) ha mantenido el riesgo bajo control. Se considera **Moderado** pero gestionado.
