# Proyecto ETL: E-commerce

Este proyecto realiza un pipeline de **Extracción, Transformación y Carga (ETL)** sobre 11 archivos CSV de un sistema de e-commerce utilizando **Python** y **Pandas**. El objetivo principal es limpiar y transformar datos transaccionales para dejarlos listos para responder preguntas clave de negocio y análisis de Inteligencia de Negocios.

---

##  Estructura del Proyecto

A continuación, se detalla la organización de los archivos y carpetas del proyecto representados en forma de explorador de archivos:

```text
📁 ETL/
├── 📁 data/                        # Carpeta con los 11 archivos CSV originales (fuente de datos)
│   ├── 📄 ecommerce_brands.csv      # Información de las marcas de los productos
│   ├── 📄 ecommerce_categories.csv  # Jerarquía de categorías y subcategorías
│   ├── 📄 ecommerce_customers.csv   # Información general de los clientes registrados
│   ├── 📄 ecommerce_inventory.csv   # Estado del stock y fecha de última reposición
│   ├── 📄 ecommerce_order_items.csv # Detalle de los productos de cada pedido
│   ├── 📄 ecommerce_orders.csv      # Datos principales del pedido (monto, fechas, notas, etc.)
│   ├── 📄 ecommerce_products.csv    # Catálogo de productos disponibles
│   ├── 📄 ecommerce_promotions.csv  # Registro de campañas y descuentos
│   ├── 📄 ecommerce_reviews.csv     # Calificaciones y comentarios de usuarios
│   ├── 📄 ecommerce_suppliers.csv   # Proveedores de los productos
│   └── 📄 ecommerce_warehouses.csv  # Detalle de los almacenes
├── 📁 output/                      # Carpeta donde se guardan los reportes y datasets transformados
├── 📄 etl.py                       # Script principal con el proceso completo de limpieza y transformación
├── 📄 README.md                    # Instrucciones de uso y estructura del proyecto (este archivo)
└── 📄 requirements.txt             # Archivo con las dependencias necesarias (Pandas)
```

---

##  Descripción de Componentes

### 1. `data/` (Origen de datos)
Contiene los archivos fuente en formato CSV. 

### 2. `etl.py` (Script Pipeline)
El código de Python realiza las siguientes tareas de forma automatizada:
* **Extracción**: Carga dinámica con `glob` y Pandas de todos los archivos de datos.
* **Transformación**:
  * Relleno inteligente de valores nulos (por ejemplo, notas vacías como `"sin pedido"`, promociones nulas como `0`).
  * Análisis de registros duplicados a nivel general y por columnas identificadoras (`id`s).
  * Conversión de columnas temporales en formato de texto a formato nativo de fecha (`datetime`).
* **Análisis**: Responde 3 preguntas de negocio clave:
  1. Top 5 clientes con mayor gasto acumulado.
  2. Identificación del producto más vendido por cantidad.
  3. Evolución cronológica de las ventas mes a mes.

### 3. `output/` (Destino de datos)
Directorio reservado para los datos ya limpios y listos para visualización o reportes.



Una vez ejecutado el script `etl.py`, encontrarás los siguientes reportes en formato CSV listos para análisis:

- **top_5_clientes.csv**: Listado de los clientes con mayor volumen de gasto.
- **ranking_productos.csv**: Reporte de los productos más vendidos,
- **evolucion_ventas_mensual.csv**: Análisis temporal de los ingresos totales mes a mes.
- **pedidos_limpios.csv**: La tabla maestra de órdenes tras el proceso de limpieza de nulos y corrección de tipos.

 **Nota:** Los archivos en esta carpeta se sobrescriben en cada ejecución para garantizar que siempre cuentes con la versión más reciente y válida de la información [216, Historial de chat].

##  Cómo Ejecutar el Proyecto

### Requisitos Previos
* Tener instalado **Python 3.x** y **Git** en tu sistema.

### Paso a Paso

1. **Clonar el repositorio**:
   Abre una terminal git Bash en tu computadora y clona el proyecto con el siguiente comando:
   ```bash
   git clone https://github.com/Judith-Diaz/ETL.git
   ```

2. **Ingresar a la carpeta del proyecto**:
   ```bash
   cd ETL
   ```

3. **Crear un entorno virtual** `.venv` (recomendado para aislar las dependencias):
   ```bash
   python -m venv .venv
   ```

4. **Activar el entorno virtual**:
   * **En Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * **En Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   * **En Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

5. **Instalar dependencias (Pandas)**:
   Este comando lee el archivo `requirements.txt` e instala de forma automática la librería **Pandas** (y cualquier otra dependencia del proyecto) dentro de tu entorno virtual:
   ```bash
   pip install -r requirements.txt
   ```

6. **Ejecutar el script principal**:
   ```bash
   python etl.py
   ```


### Estadísticas de Ejecución
  
   Tiempo promedio: 0.71 segundos (para los 11 archivos actuales).
   Capacidad: Optimizado para procesos de carga diferencial que ahorran tiempo de ejecución al no procesar toda la historia cada vez

