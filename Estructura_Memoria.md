# Propuesta de Estructura para la Memoria

**Título del trabajo:** Predicción de series de tiempos aplicado al trading de criptomonedas usando la arquitectura de Transformers

---

## Capítulo 1: Introducción General

### 1.1 Motivación y Contexto
- **Contenido:** Introducir el problema del trading algorítmico y la evolución desde modelos clásicos (ARIMA, RNN/LSTM) a la arquitectura Transformer. Destacar el potencial de los Transformers para capturar dependencias complejas y no lineales en series de tiempo financieras.
- **Fuentes:** Documento "Financial Time Series Transformers Research", Documento "Time Series Transformer Deep Dive"

### 1.2 El Desafío de los Datos Financieros
- **Contenido:** Describir las dificultades inherentes a los mercados financieros: bajo ratio señal-ruido, no-estacionariedad, y la Hipótesis de los Mercados Eficientes. Plantear por qué estos factores representan un reto para cualquier modelo predictivo.
- **Fuentes:** Documento "Financial Time Series Transformers Research", `Estado del arte en transformers.md`

### 1.3 Objetivos y Alcance del Trabajo
- **Contenido:** Definir el objetivo central: estudiar y evaluar rigurosamente el desempeño de la arquitectura Transformer para la predicción de la serie de tiempo de BTCUSDT en un contexto de trading, comparándolo con un espectro de estrategias base.
- **Fuentes:** `GEMINI.md` (Descripción del proyecto)

---

## Capítulo 2: Introducción Específica (Estado del Arte)

### 2.1 Evolución de Arquitecturas Transformer para Series de Tiempo
- **Contenido:** Un survey de cómo se han adaptado los Transformers al dominio de series de tiempo.
    - **2.1.1 Adaptaciones Arquitectónicas Clave:** Cubrir las tres áreas clave de adaptación: 1) Representación de la Entrada (Patching), 2) Codificación Posicional (APE, RPE, RoPE), y 3) Mecanismos de Atención Eficiente (ej. ProbSparse de Informer).
    - **2.1.2 Modelos Notables:** Describir brevemente las contribuciones de arquitecturas influyentes: la familia de eficiencia (Informer, Autoformer) y la revolución de la simplicidad (PatchTST).
    - **2.1.3 El Debate del Rendimiento: Transformers vs. Modelos Lineales:** Discutir el crucial paper 'LTSF-Linear', su crítica a la complejidad de los Transformers, y la posterior respuesta de la comunidad (ej. PatchTST) que re-contextualizó el debate.
- **Fuentes:** Documento "Time Series Transformer Deep Dive", `Estado del arte en transformers.md`

### 2.2 Estado del Arte en Machine Learning para Finanzas
- **Contenido:** Revisión de las metodologías específicas e indispensables para el modelado en finanzas cuantitativas, más allá de la arquitectura del modelo.
    - **2.2.1 Estructuración y Procesamiento de Datos:** Explicar técnicas avanzadas como la Diferenciación Fraccional para el balance entre estacionariedad y memoria, y la agregación de barras basada en eventos (TIBs, VIBs).
    - **2.2.2 Estrategias de Etiquetado y Ponderación:** Detallar métodos robustos para la generación de la variable objetivo: el Método de la Triple Barrera (Triple Barrier Method) y el Meta-Etiquetado (Meta-Labeling) para la gestión del tamaño de la posición.
    - **2.2.3 Metodologías de Validación y Backtesting:** Explicar la invalidez de la validación cruzada estándar (K-Fold CV) y la necesidad de usar técnicas como Purged K-Fold CV y Combinatorial CV para prevenir la fuga de datos y el sobreajuste. Mencionar la modelización realista de costos de transacción.
- **Fuentes:** Documento "Financial Time Series Transformers Research", `Estado del arte en transformers.md`

---

## Capítulo 3: Diseño e Implementación

### 3.1 Conjunto de Datos y Preprocesamiento
- **Contenido:** Descripción del activo (BTCUSDT), el período de estudio (2020-2025), la fuente (Binance), y las técnicas específicas de preprocesamiento y extracción de características aplicadas.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Resultados)

### 3.2 Metodología Experimental
- **Contenido:** Cómo se diseñaron y ejecutaron los experimentos.
    - **3.2.1 Estrategias de Referencia (Baselines):** Detallar todas las estrategias base implementadas para comparación: Buy & Hold, estáticas (Cruce de Medias, Bollinger, MACD), estadísticas (ARIMA), y de ML clásico (Random Forest, XGBoost).
    - **3.2.2 Arquitectura Transformer Propuesta:** Describir la arquitectura Transformer específica implementada (Chronos). Detallar su configuración, el método de tokenización y la codificación posicional utilizada.
    - **3.2.3 Estrategia de Etiquetado para Modelos ML:** Explicar la estrategia de etiquetado específica usada para los modelos de ML, incluyendo las transformaciones de la variable precio (ej. pct_change_on_ao).
- **Fuentes:** `Estado del arte en transformers.md` (Secciones Resultados, Transformers, Estrategias de Machine Learning)

### 3.3 Framework de Backtesting y Evaluación
- **Contenido:** El entorno de simulación y las métricas para juzgar el rendimiento.
    - **3.3.1 Motor de Backtesting y Parámetros:** Mencionar las herramientas usadas y los parámetros clave de la simulación (comisión: 0.001, tasa libre de riesgo: 0%).
    - **3.3.2 Métricas de Evaluación:** Definir las métricas de éxito: Sharpe Ratio para las estrategias de trading y F1 Score para los modelos de clasificación.
    - **3.3.3 Optimización de Hiperparámetros:** Mencionar el uso de búsqueda Bayesiana para encontrar los hiperparámetros que maximizan las métricas objetivo.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Resultados)

---

## Capítulo 4: Ensayos y Resultados

### 4.1 Resultados de Estrategias de Trading Estáticas y Estadísticas
- **Contenido:** Presentar los Sharpe Ratios obtenidos para las estrategias baseline (Moving Average, Bollinger, ARIMA, etc.). Idealmente en una tabla comparativa.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Resultados)

### 4.2 Resultados de Modelos de Machine Learning Clásico
- **Contenido:** Presentar los F1 scores para Random Forest y XGBoost con las diferentes estrategias de etiquetado, mostrando el rendimiento de estos modelos intermedios.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Estrategias de Machine Learning)

### 4.3 Resultados del Modelo Transformer (Chronos)
- **Contenido:** Describir el desempeño cuantitativo y cualitativo del modelo Chronos. Resaltar el hallazgo clave de que su rendimiento fue inferior a modelos más simples.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Conclusion)

### 4.4 Análisis Comparativo y Discusión de Resultados
- **Contenido:** Comparar el rendimiento entre todas las clases de modelos. Discutir las posibles razones de la sub-performance del Transformer (ej. sobreajuste, necesidad de más datos, tokenización, etc.). Este es el núcleo del análisis de resultados.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Conclusion)

---

## Capítulo 5: Conclusiones

### 5.1 Conclusiones Generales
- **Contenido:** Resumir los hallazgos principales del trabajo. La conclusión central es que, bajo las condiciones estudiadas, el modelo Transformer no logró superar a estrategias más simples ni a la de Buy & Hold.
- **Fuentes:** `Estado del arte en transformers.md` (Sección Conclusion)

### 5.2 Limitaciones del Estudio
- **Contenido:** Discutir las limitaciones del trabajo actual para contextualizar los resultados (ej. un solo activo, un solo período de tiempo, una sola arquitectura Transformer).
- **Fuentes:** Sugerido basado en buenas prácticas de investigación.

### 5.3 Trabajo Futuro
- **Contenido:** Delinear los próximos pasos y futuras líneas de investigación basadas en los hallazgos: reiterar en el procesamiento de datos, probar otras estrategias de etiquetado (Triple Barrera), usar validación cruzada robusta (Purged CV), y explorar otras arquitecturas (PatchTST).
- **Fuentes:** `Estado del arte en transformers.md` (Sección Siguientes pasos)
