# Avances - Transformers en series de tiempo

Estado del arte en transformers
Representación de la Entrada
Se toman ventanas con o sin solapamiento y se transforman en tokens. Esto aumenta la carga semántica en comparación a un valor aislado de la serie de tiempo. Esto resolvió positivamente el debate de Are Transformers Effective for Time Series Forecasting? Y es la clave para reutilizar modelos fundacionales basados existentes (como GPT) y lograr modelos fundacionales específicos para series de tiempo como chronos. 
Además de aumentar la carga semántica de la entrada también mejora la performance del modelo ya que ahora la ventana sobre la que se hace atención es de L/T < L, donde L es la cantidad de puntos de la serie de tiempo y T es el tamaño de la ventana usada para el patching. 

Orden Encoding
El mecanismo de atención es invariante al orden de la secuencia, para solucionar esto se aplica un positional encoding. Se pueden dividir en 
Codificaciones Posicionales Absolutas (APE)
 Sinusoidal fija: En attention is all you need se utiliza una estrategia sinusoidal que no es aprendible pero permite manejar tamaños de secuencia variable. 
APE Aprendible: Se entrenan pesos como parte del entrenamiento para manejar el encoding posicional.


Codificaciones Posicionales Relativas (RPE)
La idea general es que tiene más valor codificar que el elemento i está a distancia 1 de i-1 (y que i-1 a distancia 1 de i-2) que codificar la información que el elemento i está en la posición i.    

RPE:  La idea original consiste en aprender embeddings para distancias relativas los cuales se suman al vector de Key y Value antes de realizar el producto para calcular la atención. 

Rotary Positional Embeddings (RoPE): Es más eficiente ya que aplica una matriz de rotación a los vectores de Query y Key donde el ángulo de la rotación depende de la posición absoluta del elemento.

Híbridos y específicos a series de tiempo
Basado en timestamps: Se extraen features de los timestamps como día del mes, día de la semana, etc y se incorporan al embedding.


Attention
Dos objetivos que tienen los enfoques que buscan modificar el mecanismo de atención son el de mejorar la complejidad cuadrática de este, y  el de agregar sesgo inductivo específico a  series de tiempo.

Sparse attention

ProbSparse: Se calcula la divergencia de Kullback-Leibler con respecto a una distribución uniforme y mediante eso se eligen los u elementos más relevantes para calcular la atención solo con esos. Esta estrategia está basada en que solo una pequeña proporción de elementos brindan una contribución desproporcionada para calcular el resultado.

LogTrans: utiliza una capa convolucional con una máscara LogSparse, esto es convoluciona y luego mira a elementos espaciados exponencialmente (i, i-2^1, i-2^2, etc), para calcular la atención.  

Local sensitive hashing: informer utiliza una función de LSH que agrupa a vectores similares para luego calcular atención solo dentro de dichos grupos. 


Inductive bias

Auto Correlación: se calcula la autocorrelación de la serie y luego se usa esa información para luego predecir utilizando secciones de la serie de tiempo determinada por la periodicidad obtenida de los coeficientes de autocorrelación.

Frequency-Domain Attention: Aplica la transformada de fourier a la serie entera y luego aplica atención en el dominio de frecuencias. Realiza sampling de secciones con las frecuencias mas relevantes.

Estado del arte ML aplicado a finanzas


La aplicación del Machine Learning a las finanzas es una disciplina distinta que difiere del ML estándar utilizado en otros campos.
Esta área se centra en resolver problemas fundamentales y genéricos inherentes a las series financieras, incluyendo la estructuración de datos, el etiquetado, la ponderación, las transformaciones de series de tiempo, y el backtesting

• Desafíos Únicos: El entorno financiero presenta un bajo ratio señal-ruido, y una violación crítica del supuesto de datos independientes e idénticamente distribuidos (IID) debido a la naturaleza secuencial y a los resultados superpuestos (overlapping outcomes)
Overfitting
El bajo ratio señal-ruido en los datos incrementa la probabilidad de aprender correlaciones espurias en vez de patrones inherentes.
Relacionado a eso está La Paradoja de la Investigación: La creencia de que se puede investigar ejecutando un algoritmo, haciendo backtest de las predicciones y repitiendo la secuencia hasta obtener un backtest favorable es un error. 

Correcciones Metodológicas:
Marcos’ First Law of Backtesting: "El backtesting no es una herramienta de investigación. La importancia de las características (Feature Importance) sí lo es".  El análisis de la importancia de las características debe realizarse antes de cualquier backtest.

Cross-Validation (CV) Purificada: La CV tradicional (K-Fold) falla en finanzas porque los resultados adyacentes se superponen y son serialmente dependientes. La solución es utilizar el Purged K-Fold CV, que purga las observaciones en el training set que se superponen informativamente con las del testing set.
Embargo: Se aplica un embargo a las observaciones del training set que siguen inmediatamente a un periodo de prueba (test) para prevenir la fuga de datos (leakage).
Técnicas de Conjunto: El Bagging (Bootstrap Aggregation) es generalmente preferible al Boosting en finanzas, ya que se enfoca en reducir la varianza y prevenir el sobreajuste.

Data processing
El procesamiento de datos tiene como objetivo generar un conjunto de datos continuo, homogéneo y estructurado a partir de datos financieros no estructurados.

Datos Esenciales: El proceso comienza con Datos Fundamentales, Datos de Mercado, Análisis y Datos Alternativos.

Muestreo: Es crucial muestrear las barras para producir una matriz de características que contenga ejemplos de entrenamiento relevantes. Esto se hace a menudo mediante Downsampling o, preferiblemente, Muestreo Basado en Eventos (Event-Based Sampling), como el uso del filtro CUSUM que identifica una desviación de la media en un proceso estacionario.

Price differentiation:  Existe un tradeoff entre estacionariedad y preservar memoria. La diferenciación entera (d=1) puede lograr la estacionariedad pero cancela la memoria. Como solución se utiliza el proceso de diferenciación fraccional que introduce un operador de diferencia generalizado que permite pasos no enteros. El objetivo es encontrar el coeficiente de diferenciación mínimo (d∗) que asegure la estacionariedad, permitiendo preservar la máxima memoria posible.

Bar aggregation (Agregación de Barras):

• Barras Estándar: Incluyen Time Bars (Barras de Tiempo), Tick Bars (Barras de Tick), Dollar Bars,  y Volume Bars (Barras de Volumen). Las Time Bars deben evitarse en general, ya que tienen propiedades estadísticas deficientes, como la sobre/sub-estimación de información y una fuerte correlación serial.

• Barras Impulsadas por Información: Son métodos avanzados que muestrean el mercado basándose en la actividad de trading que diverge de las expectativas. Estos se ajustan dinámicamente y abordan la fragmentación de ticks y los outliers. Ejemplos incluyen Tick Imbalance Bars (TIBs), Volume Imbalance Bars (VIBs) y Dollar Imbalance Bars (DIBs).
Labeling (Etiquetado)
El etiquetado es el proceso de asociar las características observadas (X) con los resultados futuros (y).

Método de Horizonte Fijo (Defectuoso): El método más común utiliza un horizonte de tiempo fijo (h) y un umbral constante (τ) para etiquetar, lo cual ignora la volatilidad dinámica del mercado y conduce a errores de clasificación.

El Método de la Triple Barrera: Es un método de etiquetado dependiente de la trayectoria (path-dependent) que utiliza tres límites
    1. Dos barreras horizontales (toma de ganancias y stop-loss), que son una función dinámica de la volatilidad estimada.
    2. Una barrera vertical (límite de expiración) basada en el número de barras transcurridas.

Meta-Labeling (Meta-Etiquetado): Consiste en entrenar un modelo ML secundario para aprender el tamaño de la apuesta (size), no el lado (side, largo o corto), que es establecido por un modelo primario exógeno (ej. un modelo fundamental). Este modelo secundario funciona como un clasificador binario ({0, 1}) que decide si se debe tomar la apuesta o pasar. Limita el sobreajuste porque el ML no decide la dirección de la posición.

Ponderación de Muestras (Sample Weights)
Una vez obtenida las etiquetas se pueden ponderar las muestras en base a distintos criterios. Es esencial para corregir la falta de IID causada por los resultados superpuestos.

Unicidad Promedio: Cada etiqueta es función de un rango de características de periodos en el pasado. Para un periodo t, múltiples etiquetas podrían ser función de dicho valor, es decir, múltiples etiquetas se solapan en t.  La unicidad promedio se utiliza para medir el grado de no-solapamiento de la etiqueta en su ciclo de vida.

Bootstrap Secuencial: Una técnica de remuestreo que crea muestras más cercanas a IID al controlar la redundancia.
Atribución de Retorno: Pondera las observaciones en función de su unicidad y el retorno absoluto.

Backtesting
El backtesting es la fase donde se evalúa científicamente el descubrimiento y la estrategia de inversión.
• Riesgos: La simulación histórica (walk-forward) es la forma estrecha y tradicional de backtesting, pero solo simula una única trayectoria histórica, siendo altamente vulnerable al sobreajuste.
• Probabilidad de Sobreajuste (PBO): El análisis de backtest debe evaluar la probabilidad de sobreajuste del backtest (PBO) tomando en cuenta el número de pruebas o ensayos realizados para destilar la estrategia.
Paradigmas Avanzados de Backtesting:
Simulaciones de Escenarios: Utiliza técnicas como Combinatorial Purged Cross-Validation (CPCV), que prueba el algoritmo en múltiples particiones de los datos, simulando así una gran variedad de escenarios que son consistentes con la historia.
Backtesting en Datos Sintéticos: Este método es una alternativa radical a la simulación histórica. Utiliza las características estadísticas del proceso estocástico subyacente (ej., un proceso Ornstein-Uhlenbeck discreto) para generar un gran número de conjuntos de datos sintéticos no vistos. Esto permite determinar la Regla de Trading Óptima (OTR) sin sobreajustarse a una trayectoria histórica única.

Estadísticas de Backtest
 La evaluación requiere métricas robustas que corrijan el sesgo de selección y la no-normalidad.
Probabilistic Sharpe Ratio (PSR): Calcula la probabilidad de que el verdadero ratio de Sharpe exceda un umbral determinado.
Deflated Sharpe Ratio (DSR): Ajusta el PSR para corregir el sesgo de selección y el sobreajuste del backtest.



Resultados
Se aplica backtesting con las estrategias mencionadas. Cada estrategia puede decidir en qué dirección apuesta (long o short) basado en su propia dirección. Se realizó búsqueda bayesiana de hiperparametros para maximizar el Sharpe Ratio de cada estrategia.

Datos utilizados: cotización horaria de BTCUSDT según la api de Binance. Fecha de inicio: 2020-01-01, fecha de fin: 2025-11-07.
Risk free rate para calcular el Sharpe Ratio: 0%
Comicion usada para backtest: 0.001
Sharpe ratio de Buy & Hold en el periodo: 1.16
Estrategias de trading estáticas

Moving Average Crossover: utiliza una media móvil lenta y una rápida para realizar operaciones cuando el valor de uno cruza al del otro.  Se encontró un sharpe ratio máximo de 0.82 pero de los 10 mejores solo 1 supera el 0.5, con lo cual es posible suponer una situación de overfitting. 


 Bollinger Bands: Esta es una estrategia de reversión a la media. Calcula bandas superiores e inferiores alrededor de una media móvil simple del precio. Genera una señal de compra cuando el precio cae por debajo de la banda inferior y una señal  de venta cuando el precio sube por encima de la banda superior, asumiendo que el precio se revertirá a la media. En casi todos los experimentos el sharpe ratio fue negativo.

 MACD: Esta estrategia se basa en el indicador de Convergencia/Divergencia de Medias Móviles (MACD). Utiliza un promedio ponderado lento y uno rápido. Genera una señal de compra cuando la línea MACD cruza por encima de su línea de señal correspondiente, y una señal de venta cuando la línea MACD cruza por debajo de la línea de señal. En los experimentos realizados obtuvimos, como máximo, un sharpe ratio de 0.2. 

RSIDivergence: Esta estrategia utiliza el Índice de Fuerza Relativa (RSI) para identificar posibles reversiones de tendencia. Busca divergencias entre la acción del precio y el indicador RSI. Se genera una señal de compra en una "divergencia alcista" (el precio marca un nuevo mínimo mientras que el RSI marca un mínimo más alto). Se genera una señal de venta en una "divergencia bajista" (el precio marca un nuevo máximo mientras que el RSI marca un máximo más bajo). En los experimentos realizados no se obtuvo sharpe ratio positivo.

 MultiIndicatorStrategy: Esta estrategia, propuesta por Alain Glucksmann,  combina las Bandas de Bollinger para las señales de entrada con dos medias móviles  simples (una rápida y una lenta) para la confirmación de la tendencia. Entra en una posición larga si el precio supera la Banda de Bollinger superior mientras que la SMA rápida está por encima de la SMA lenta (indicando una tendencia alcista). Entra en una posición corta si el precio cae por debajo de la Banda de Bollinger inferior mientras que la SMA rápida está  por debajo de la SMA lenta (indicando una tendencia bajista). Utiliza un stop-loss dinámico (trailing stop-loss) para gestionar las operaciones. El sharpe ratio maximo fue de 1.0; todos los experimentos en el top 10 se ubican por sobre 0.75.                                                                                           

 
SwingTrading: Esta estrategia, tomada de Trading Systems and Methods, intenta seguir los impulsos (swings) del precio basándose en la Teoría de Dow. Identifica impulsos alcistas y bajistas rastreando reversiones que superan un cierto filtro porcentual. Tiene dos modos:              
    • Agresivo: Entra en una operación inmediatamente al detectar una reversión del swing.                                    
    • Conservador: Espera una ruptura de un máximo anterior del swing (para comprar) o una ruptura de un mínimo anterior del  swing (para vender) antes de entrar en una operación.    
Obtuvo un sharpe ratio estable en torno al 0.5



Estrategias de métodos estadísticos
En todos los casos se plantea un ‘refit period’, por ej 24hs, que indica la frecuencia con la que se vuelve a entrenar el modelo. En el periodo entre entrenamientos se utilizan los pesos previamente calculados para realizar la predicción.
Además, se utiliza un umbral (threshold) para decidir si se actua en base a esa prediccion o no. Por ejemplo, si el umbral es del 1%, entonces la predicción para el periodo siguiente debe ser 1% mayor que el valor del periodo actual.

ARIMA: Se aplicó sobre los retornos del precio de cierre. No se obtuvieron resultados positivos y no se encontró una relación clara entre los hiper parámetros del modelo y el objetivo.

Kalman Arima: Se aplicó un filtro de Kalman sobre los retornos del precio de cierre. Luego se utilizó un modelo ARIMA para la predicción.  No se obtuvieron resultados positivos y no se encontró una relación clara entre los hiper parámetros del modelo y el objetivo.

ARIMAX + Garch strategy: Se utilizó un modelo GARCH para predecir la volatilidad y se utilizó dicho valor como variable exógena en un modelo ARIMAX.No se obtuvieron resultados positivos y no se encontró una relación clara entre los hiper parámetros del modelo y el objetivo.

Prophet: Se utilizó el modelo Prophet para la predicción de los valores de cierre. No se obtuvieron resultados positivos. 


Estrategias de Machine Learning
En esta sección se exploraron diversos algoritmos clásicos de machine learning como XGBOOST, y random forest, pero no se incluyen herramientas de Deep Learning. En vez de utilizar los modelos para predecir el precio exacto se toman distintas variables objetivos, como puede ser, la dirección del próximo periodo (+1 si el precio sube, -1 si el precio baja). 
En estos experimentos se realizó búsqueda de hiperparametros, aplicando backtesting, con el objetivo de maximizar el f1 score.

Variable objetivo
Para calcular la variable objetivo se transformo la variable precio, a esa transformacion, se le calcularon los minimos y maximos locales y se asigno -1, 0, +1 para los minimos, periodos de movimiento lateral, y maximos respectivamente.
Se experimento con varias transformaciones de la variable precio:
ao_on_price: se calcula el awesome oscilator sobre el precio de cierre del periodo.
ao_on_pct_change: se integra la serie de precios de cierre y luego se calcula el awesome oscillator. 
pct_change_on_ao: se calcula el awesome oscillator y luego se integra esa serie.
pct_change_std: para este método no se calculan los extremos locales, sino que se integra la serie y se marca como 
-1: y_t+1 < -σ 
+1: y_t+1 > σ
0: en otro caso 
Donde σ es una fracción de la desviación estándar calculada con una ventana deslizante de 7 días (24*7 periodos).
Algoritmos
Random forest: Se obtuvo un f1 máximo de 0.48. La mejor estrategia de labeling fue pct_change_on_ao 

Xgboost:  Se obtuvo un f1 máximo de 0.57. La mejor estrategia de labeling fue pct_change_on_ao 

Xgboost palazzo et all: esta estrategia propuesta por Gilhierme Palazzo consta en agregar, según volumen volumen,  las mediciones de intervalos de 1. La variable objetivo se marca como 0 o 1 de acuerdo de si el precio de cierre de la siguiente barra excede el de la barra actual más un umbral.   Se obtuvo un f1 máximo de 0.637

Transformers
Chronos


Conclusion
No se consiguió superar al sharpe ratio de buy and hold en el periodo estimado. Los modelos tuvieron muchas dificultades con discernir el sentido del próximo periodo. Chronos tuvo un desempeño peor que modelos más simples como xg boost, siendo incapaz siquiera de superar un baseline aleatorio (50/50).

Siguientes pasos

Reiterar en el procesamiento de datos, aplicar otras estrategias de labeling y agregación. Utilizar estrategias de cross validations en vez de backtesting para evitar overfitting.
