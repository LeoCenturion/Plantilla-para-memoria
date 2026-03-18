# Procesamiento de datos
El paso de **Estructuración y Procesamiento de Datos** es quizás una de las contribuciones más importantes de Marcos López de Prado, ya que ataca el problema fundamental de "basura entra, basura sale" (Garbage In, Garbage Out) en el Machine Learning financiero. Él argumenta que los métodos tradicionales de procesamiento de datos destruyen la señal predictiva antes de que el modelo pueda siquiera analizarla.

A continuación, se detalla este punto en sus cuatro pilares fundamentales:

### 1. El Reloj de Volumen y las Barras de Información (Muestreo de Datos)
La forma estándar en la que la industria agrupa los datos es en "barras de tiempo" (por ejemplo, el precio de cierre cada minuto, cada hora o cada día). López de Prado rechaza categóricamente esta práctica.
*   **El problema del Tiempo Cronológico:** Los mercados no procesan la información a intervalos de tiempo constantes. Hay horas de altísima actividad (como la apertura del mercado) y horas casi vacías (como el mediodía). Usar barras de tiempo sobremuestrea la información durante los períodos de baja actividad y submuestrea durante los períodos de alta actividad, lo que genera malas propiedades estadísticas como la correlación en serie, la heterocedasticidad y la no normalidad de los retornos.
*   **Barras de Dólares (Dollar Bars):** Sugiere cambiar a un reloj basado en la actividad del mercado. Las *Dollar Bars* toman una muestra cada vez que se intercambia un valor predefinido en el mercado (ej. cada vez que se negocian 1 millón de dólares). Esto es superior a las barras de volumen o de *ticks* porque el número de acciones negociadas fluctúa drásticamente si el precio del activo se duplica o se reduce a la mitad, mientras que el valor en dólares es mucho más estable a lo largo de los años.
*   **Barras impulsadas por Información (Imbalance & Runs Bars):** El nivel más avanzado es muestrear los datos basándose en el desequilibrio de las órdenes. Las *Tick Imbalance Bars* o *Volume Imbalance Bars* detectan si hay una secuencia inusual de compras agresivas o ventas agresivas. El objetivo es generar una nueva barra (tomar una muestra) exactamente en el momento en que se detecta que están entrando al mercado operadores informados o institucionales, capturando el desequilibrio antes de que el precio alcance un nuevo nivel de equilibrio.

### 2. El Dilema entre Estacionariedad y Memoria (Diferenciación Fraccional)
Para que un algoritmo de Machine Learning pueda predecir el futuro basándose en el pasado, necesita que los datos sean **estacionarios** (es decir, que sus propiedades estadísticas, como la media y la varianza, no cambien constantemente con el tiempo).
*   **El error clásico:** Para lograr la estacionariedad, los analistas suelen aplicar una diferenciación entera a los precios (calcular los retornos diarios o cambios porcentuales). El problema es que esta técnica borra absolutamente toda la "memoria" a largo plazo de la serie de precios. Se pierde información vital sobre el nivel absoluto del precio y las tendencias históricas. Los retornos son estacionarios pero no tienen memoria; los precios tienen memoria pero no son estacionarios.
*   **La Solución (Fractional Differentiation):** López de Prado introduce la **Diferenciación Fraccional**, que permite aplicar un grado de diferenciación con un número real (por ejemplo, $d=0.45$) en lugar de un número entero (como $d=1$). El objetivo es encontrar el coeficiente mínimo de diferenciación ($d^*$) que sea justo el necesario para que la serie pase una prueba estadística de estacionariedad (como el test ADF), pero que conserve la mayor cantidad posible de correlación con la serie de precios original. De esta forma, el modelo de ML recibe datos estables pero enriquecidos con memoria histórica.

### 3. Detección de Rupturas Estructurales (Structural Breaks)
Los mercados no son estáticos; transicionan entre diferentes regímenes (por ejemplo, pasan de un mercado en rango a una tendencia explosiva, o de un patrón de reversión a la media a uno de *momentum*). 
*   **La Oportunidad:** Estos cambios de régimen son sumamente rentables porque atrapan a la mayoría de los participantes del mercado por sorpresa, haciéndoles cometer errores costosos, como duplicar apuestas perdedoras antes de verse forzados a liquidar sus posiciones (stop-loss). 
*   **Las Herramientas:** En lugar de asumir linealidad, se utilizan pruebas de explosividad y filtros avanzados para crear características (features) para el modelo. Destaca el uso del **SADF (Supremum Augmented Dickey-Fuller)** y filtros **CUSUM** (Cumulative Sum) para detectar matemáticamente en qué momento los precios abandonan un comportamiento de paseo aleatorio (random walk) y entran en una fase de burbuja exponencial o de colapso.

### 4. Entropía y Características Microestructurales
En lugar de depender del análisis técnico clásico, los datos en bruto se transforman en métricas de la teoría de la información y la microestructura del mercado:
*   **Entropía:** Utilizando la entropía de Shannon o algoritmos de compresión como Lempel-Ziv, se puede medir la complejidad y previsibilidad de una serie de precios. Un mercado con alta entropía es muy eficiente (sus precios son ruido impredecible), mientras que un mercado con baja entropía está "comprimido", contiene patrones redundantes, es ineficiente y, por ende, es el caldo de cultivo ideal para que se formen burbujas y oportunidades predictivas.
*   **Microestructura:** A partir de los datos de alta frecuencia (mensajes FIX que muestran cancelaciones de órdenes, tamaños de colas, etc.), se calculan métricas como el **VPIN** (Probabilidad de Trading Informado Sincronizado por Volumen), la **Lambda de Kyle** o la **Lambda de Amihud**. Estas métricas permiten al algoritmo cuantificar la iliquidez, el impacto en el precio de las transacciones y rastrear el comportamiento oculto de las grandes instituciones antes de que el precio se mueva.

# Labeling
Basado en el marco de trabajo de Marcos López de Prado, el **etiquetado de los datos (Labeling)** es uno de los pasos donde la mayoría de los investigadores cometen errores fundamentales al aplicar Machine Learning a las finanzas. 

La literatura tradicional suele utilizar el **método de horizonte de tiempo fijo** (fixed-time horizon), el cual evalúa si el precio será mayor o menor dentro de un tiempo exacto en el futuro (por ejemplo, en 5 días o en 24 horas) superando un umbral de retorno constante,,. López de Prado argumenta que este enfoque es irreal y defectuoso por dos razones: aplica el mismo umbral independientemente de la volatilidad del mercado, y **falla en capturar la dependencia de la trayectoria (path dependency)**,. Es decir, si el precio sufre un colapso del 10% durante ese período —lo que en la vida real activaría un *stop-loss* y liquidaría la posición— pero se recupera justo al final del horizonte fijo, el método tradicional lo etiquetaría erróneamente como una ganancia, creando un modelo ciego al riesgo.

Para solucionar esto, López de Prado introduce técnicas altamente especializadas:

### 1. Umbrales Dinámicos
En lugar de utilizar un umbral de ganancia o pérdida fijo (por ejemplo, un 2%), los límites de la operación deben ajustarse dinámicamente como una función del riesgo actual. Para ello, propone utilizar una medida como la desviación estándar móvil ponderada exponencialmente, asegurando que los umbrales de toma de ganancias y de frenado de pérdidas se adapten a la volatilidad del momento,,.

### 2. El Método de la Triple Barrera (Triple-Barrier Method)
Para resolver el problema de la trayectoria del precio, se establecen tres "barreras" dinámicas desde el momento en que se inicia una teórica operación,:
*   **Barrera Superior (Toma de ganancias):** Un umbral dinámico por encima del precio de entrada,.
*   **Barrera Inferior (Stop-Loss):** Un umbral dinámico por debajo del precio de entrada que previene pérdidas catastróficas,.
*   **Barrera Vertical (Límite de tiempo):** Un período de retención máximo (ej. un número límite de barras) para evitar tener capital bloqueado en una posición estancada,.

**Lógica de etiquetado:** La observación adquiere su etiqueta dependiendo exclusivamente de **cuál de las tres barreras se toca primero**,. Si el precio toca la barrera superior, se etiqueta con un `1` (Compra/Ganancia). Si toca la barrera inferior, se etiqueta con un `-1` (Venta/Pérdida). Si se acaba el tiempo y toca la barrera vertical, se etiqueta con un `0` (Neutral) o con el signo del retorno actual,. Esto entrena al modelo de ML a reconocer operaciones que son rentables *dentro* de las estrictas reglas reales de gestión de riesgos.

### 3. Meta-Etiquetado (Meta-Labeling)
Normalmente, los modelos intentan predecir la *dirección* (comprar o vender) y el *tamaño* de la posición al mismo tiempo,. López de Prado propone bifurcar este proceso mediante el meta-etiquetado:
*   **Modelo Primario:** Un sistema simple (que puede ser un cruce de medias móviles, bandas de Bollinger, o incluso la intuición humana fundamentada) decide la **dirección** de la apuesta,,. Este modelo prima un alto *recall*, es decir, capturar todas las posibles oportunidades.
*   **Modelo Secundario (El Meta-Modelo):** Es un poderoso algoritmo de Machine Learning que no predice el mercado, sino que responde a una pregunta binaria: *¿Tendrá éxito la señal del modelo primario?*,. Sus etiquetas son simplemente `1` (el modelo primario acertó) o `0` (el modelo primario falló),.

**Los beneficios del Meta-Etiquetado son masivos:**
*   **Aumenta la precisión (F1-Score):** El modelo secundario se encarga de filtrar los falsos positivos (operaciones de baja confianza), mejorando radicalmente la métrica F1,. 
*   **Limita el sobreajuste (Overfitting):** Dado que el modelo de ML solo se usa para calcular el **tamaño de la apuesta** (donde `0` significa ignorar la oportunidad) y no la dirección, el riesgo de sobreajuste catastrófico disminuye.
*   **Habilita el enfoque "Cuantamental":** Permite colocar una sofisticada capa de Machine Learning sobre modelos fundamentales clásicos o analistas humanos, ayudando a determinar matemáticamente qué tanta confianza deberíamos tener en su intuición bajo las condiciones actuales del mercado,.

Finalmente, dentro de estas técnicas, López de Prado recomienda limpiar los datos **eliminando etiquetas innecesarias o raras** (cuando una clase tiene muy pocas muestras), ya que las clases excesivamente desequilibradas deterioran el rendimiento de los clasificadores de Machine Learning.

# Cross validation

El problema fundamental del *K-Fold Cross-Validation* tradicional al aplicarse a problemas financieros es que asume que las observaciones son independientes e idénticamente distribuidas (IID). En las series de tiempo financieras, esta suposición es falsa debido a la superposición de los resultados y a la correlación en serie de los datos.

Cuando se utiliza validación cruzada tradicional, la superposición temporal provoca "fugas de información" (leakage), es decir, el conjunto de entrenamiento termina conteniendo información que también aparece en el conjunto de prueba. Entrenar un modelo con información que, de forma encubierta, contiene parte de los datos que debe predecir, mejora falsamente el rendimiento de la estrategia y conduce inevitablemente a descubrimientos falsos y sobreajustes catastróficos. 

Para prevenir estas fugas durante la validación y desarrollo de modelos, Marcos López de Prado introduce una clase computacional llamada `PurgedKFold`, la cual aplica dos técnicas estrictas para la separación de datos:

**1. Purgado (Purging)**
Consiste en eliminar del conjunto de entrenamiento todas aquellas observaciones cuyas etiquetas se superpongan en el tiempo con las etiquetas incluidas en el conjunto de prueba. 
*   **La mecánica:** En finanzas, una etiqueta a menudo no depende de un solo instante, sino de una trayectoria a lo largo de un período temporal (por ejemplo, el rendimiento durante los siguientes 5 días o hasta que toque una barrera). Si una observación de prueba depende de la información ocurrida en el intervalo temporal $[t_{j,0}, t_{j,1}]$, el algoritmo purga (borra) cualquier observación de entrenamiento cuya propia ventana temporal de evaluación solape con ese intervalo.
*   **El objetivo:** Esto garantiza estrictamente que el modelo no se entrene utilizando el mismo retorno de precios o los mismos eventos exactos por los que luego será evaluado.

**2. Embargo (Embargoing)**
Incluso si el purgado elimina la superposición directa de etiquetas, existe un segundo peligro: las características financieras suelen presentar persistencia a largo plazo y correlación en serie (como los procesos ARMA).
*   **La mecánica:** Para evitar que la inercia o "memoria" del mercado contamine la evaluación, se impone un "embargo". Esto significa que se elimina adicionalmente un pequeño búfer o bloque de observaciones de entrenamiento que ocurren **inmediatamente después** del conjunto de prueba. 
*   **El tamaño del embargo:** López de Prado menciona que eliminar un valor pequeño (como por ejemplo el 1% del total de las barras temporales) suele ser suficiente para eliminar el efecto de los eventos de mercado que persisten a través de la frontera de la división de datos. 
*   **Observaciones anteriores:** Es importante destacar que **no** es necesario aplicar un embargo a las observaciones de entrenamiento que se encuentran temporalmente *antes* del conjunto de prueba. La razón es que esas etiquetas pasadas solo contienen información que ya era de dominio público en el momento en que comienza la ventana de prueba, por lo tanto, no introducen ningún sesgo de mirar hacia el futuro (look-ahead bias).



# Backtesting

El enfoque de Marcos López de Prado sobre el backtesting y la evaluación de riesgos es una de sus críticas más severas a la industria financiera tradicional. Él sostiene que la mayoría de los descubrimientos empíricos en finanzas son falsos debido al sobreajuste (overfitting) y al sesgo de selección. 

A continuación, se detalla en profundidad su marco de trabajo para un backtesting y evaluación de riesgos verdaderamente rigurosos:

### 1. Las Tres Leyes del Backtesting
López de Prado establece tres reglas inquebrantables que todo investigador cuantitativo debe seguir para evitar el autoengaño:
*   **Primera Ley:** "El backtesting no es una herramienta de investigación. La importancia de las características (feature importance) sí lo es". Tratar de entender por qué una estrategia funciona basándose en el resultado de un backtest lleva a inventar historias (*storytelling*) ex-post. La investigación real se hace analizando qué variables tienen poder predictivo antes de simular la estrategia.
*   **Segunda Ley:** "Hacer backtesting mientras se investiga es como beber y conducir. No investigue bajo la influencia de un backtest". El backtest solo debe ejecutarse una vez que el modelo está completamente definido. Si el backtest fracasa, se debe desechar el modelo y empezar desde cero; ajustar los parámetros para mejorar el resultado del backtest es la receta garantizada para el sobreajuste.
*   **Tercera Ley:** "Todo resultado de backtest debe reportarse junto con todos los ensayos (trials) involucrados en su producción". Si pruebas 1,000 estrategias aleatorias, por pura suerte estadística alguna se verá increíble. Sin saber cuántos intentos fallidos hubo, es imposible evaluar si el éxito es real o un falso descubrimiento.

### 2. Los 7 Pecados del Inversor Cuantitativo
Incluso si tu código de backtest es perfecto, los resultados probablemente sean engañosos si caes en los errores clásicos. López de Prado destaca siete "pecados" principales que contaminan las simulaciones:
1.  **Sesgo de supervivencia (Survivorship bias):** Usar el universo actual de activos, ignorando las empresas que quebraron o fueron deslistadas en el pasado.
2.  **Sesgo de mirar al futuro (Look-ahead bias):** Usar información que aún no era pública en el momento en que se habría tomado la decisión simulada (ej. usar datos de ganancias el último día del trimestre, aunque el reporte se publique un mes después).
3.  **Storytelling:** Inventar una justificación a posteriori para un patrón aleatorio.
4.  **Data mining / Data snooping:** Entrenar el modelo con los mismos datos que se usan para la prueba.
5.  **Costos de transacción irreales:** Asumir que se puede operar sin impactar el precio del mercado (slippage) o ignorar comisiones.
6.  **Valores atípicos (Outliers):** Depender de unos pocos eventos extremos del pasado que es improbable que se repitan.
7.  **Ventas en corto (Shorting):** Asumir que siempre es posible pedir prestado un activo para venderlo en corto a un costo predecible.

### 3. Más allá de la Simulación Histórica (Walk-Forward)
El método tradicional en la industria es el *Walk-Forward* (simular el pasado cronológicamente). López de Prado advierte que esto prueba **un solo escenario** (el camino histórico que por casualidad ocurrió), el cual es facilísimo de sobreajustar. Para solucionar esto, propone dos grandes alternativas:

*   **Combinatorial Purged Cross-Validation (CPCV):** Como se explicó anteriormente, este método divide los datos purgados y embargados en grupos, generando todas las combinaciones posibles de conjuntos de entrenamiento y prueba. En lugar de un solo Ratio de Sharpe, el CPCV te devuelve una **distribución empírica de Ratios de Sharpe** provenientes de miles de "historias alternativas" construidas a partir de los mismos datos. 
*   **Backtesting con Datos Sintéticos:** Al calibrar las reglas de *trading* (como los límites de toma de ganancias y *stop-loss*), no se debe usar la historia real porque el modelo se ajustará al ruido del pasado. En su lugar, López de Prado recomienda caracterizar el proceso estocástico subyacente del precio (por ejemplo, modelarlo como un proceso de Ornstein-Uhlenbeck) y generar cientos de miles de caminos de datos sintéticos. Sobre estos mundos simulados se calculan las Reglas de Trading Óptimas (OTR).

### 4. Nuevas Métricas de Evaluación de Riesgo y Eficiencia
El Ratio de Sharpe tradicional asume que los retornos se distribuyen normalmente (campana de Gauss), lo cual es falso en finanzas (los retornos tienen asimetría y colas pesadas). Para evaluar el riesgo real, López de Prado introduce métricas ajustadas:

*   **Probabilidad de Sobreajuste de Backtest (PBO):** Mide la probabilidad de que la estrategia que seleccionaste como "la mejor" dentro de tu muestra de entrenamiento termine rindiendo por debajo de la mediana en datos fuera de la muestra, simplemente debido al sesgo de selección.
*   **Probabilistic Sharpe Ratio (PSR):** Corrige el Ratio de Sharpe tradicional penalizándolo si los retornos tienen sesgo negativo (skewness), colas pesadas (kurtosis) o si el historial de datos es demasiado corto. Te da la probabilidad real de que tu Sharpe sea mayor a un benchmark.
*   **Deflated Sharpe Ratio (DSR):** Va un paso más allá del PSR y ajusta el umbral de aceptación basándose en el **número de ensayos independientes (trials)** y la varianza de esos ensayos. Si probaste 10,000 variaciones de una estrategia, el DSR exigirá un Ratio de Sharpe muchísimo más alto para considerar que la estrategia es estadísticamente significativa.

En conclusión, la evaluación de riesgos para López de Prado no se trata solo de poner un *stop-loss*. Se trata de aplicar rigor matemático para demostrar que los retornos de una estrategia provienen de un fenómeno económico real (con poder predictivo estadísticamente validado) y no de haber torturado los datos históricos hasta que confesaron un resultado rentable.
