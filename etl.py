from pandas._libs import properties
import pandas as pd
import glob
import os
import time 


# Inicio del cronómetro al empezar el script
inicio_proceso = time.time()


# Verificar que existen los archivos CSV descargados
archivos = glob.glob('data/ecommerce_*.csv')
if not archivos:
    print(" No se encontraron los archivos. Asegurate de descargarlos en la carpeta data/")
    print("   Deberías tener: ecommerce_orders.csv, ecommerce_customers.csv, etc.")
else:
    print(f" Archivos encontrados: {len(archivos)}")
    for f in sorted(archivos):
        print(f"  - {os.path.basename(f)}")

# Cargar los CSVs principales
df_brands = pd.read_csv('data/ecommerce_brands.csv')
df_inventory = pd.read_csv('data/ecommerce_inventory.csv')
df_promotions = pd.read_csv('data/ecommerce_promotions.csv')
df_reviews = pd.read_csv('data/ecommerce_reviews.csv')
df_suppliers = pd.read_csv('data/ecommerce_suppliers.csv')
df_warehouses = pd.read_csv('data/ecommerce_warehouses.csv')
df_categories = pd.read_csv('data/ecommerce_categories.csv')
df_orders = pd.read_csv('data/ecommerce_orders.csv')
df_order_items = pd.read_csv('data/ecommerce_order_items.csv')
df_customers = pd.read_csv('data/ecommerce_customers.csv')
df_products = pd.read_csv('data/ecommerce_products.csv')

# Explorar
print(f"\n Resumen:")
print(f"Orders: {len(df_orders)} filas, {len(df_orders.columns)} columnas")
print(f"Order Items: {len(df_order_items)} filas, {len(df_order_items.columns)} columnas")
print(f"Customers: {len(df_customers)} filas, {len(df_customers.columns)} columnas")
print(f"Products: {len(df_products)} filas, {len(df_products.columns)} columnas")
print(f"Brands: {len(df_brands)} filas, {len(df_brands.columns)} columnas")
print(f"Inventory: {len(df_inventory)} filas, {len(df_inventory.columns)} columnas")
print(f"Promotions: {len(df_promotions)} filas, {len(df_promotions.columns)} columnas")
print(f"Reviews: {len(df_reviews)} filas, {len(df_reviews.columns)} columnas")
print(f"Suppliers: {len(df_suppliers)} filas, {len(df_suppliers.columns)} columnas")
print(f"Warehouses: {len(df_warehouses)} filas, {len(df_warehouses.columns)} columnas")
print(f"Categories: {len(df_categories)} filas, {len(df_categories.columns)} columnas")
print(f"\n Primeras filas de orders:")
print(df_orders.head())
print("\n Info de orders:")
print(df_orders.info())

print("---------------------------------")
print("\n Primeras filas de order_items:")
print(df_order_items.head())
print("\n Info de orders:")
print(df_order_items.info())
print("---------------------------------")
print("\n Primeras filas de customers:")
print(df_customers.head())
print("\n Info de customers:")
print(df_customers.info())
print("---------------------------------")
print("\n Primeras filas de products:")
print(df_products.head())
print("\n Info de products:")
print(df_products.info())
print("---------------------------------")
print("\n Primeras filas de reviews:")
print(df_reviews.head())
print("\n Info de reviews:")
print(df_reviews.info())
print("---------------------------------")
print("\n Primeras filas de brands:")
print(df_brands.head())
print("\n Info de brands:")
print(df_brands.info())
print("---------------------------------")
print("\n Primeras filas de inventory:")
print(df_inventory.head())
print("\n Info de inventory:")
print(df_inventory.info())
print("---------------------------------")
print("\n Primeras filas de promotions:")
print(df_promotions.head())
print("\n Info de promotions:")
print(df_promotions.info())      

print("---------------------------------")
print("\n Primeras filas de suppliers:")
print(df_suppliers.head())
print("\n Info de suppliers:")
print(df_suppliers.info())      

print("---------------------------------")
print("\n Primeras filas de warehouses:")
print(df_warehouses.head())
print("\n Info de warehouses:")
print(df_warehouses.info())      

print("---------------------------------")
print("\n Primeras filas de categories:")
print(df_categories.head())
print("\n Info de categories:")
print(df_categories.info())     
print("---------------------------------") 
#esto l uso porque no entiendo bien para qeu sirve el campo donde estan los nulls, entonces veo el dataset completo, ay que el anterior ocmando solo me meustar una vista previa.
pd.set_option('display.max_rows', None)
print(df_categories)



print("------------------cuantos nulos hay en esta tabla Orders, porque vi! que habia nulos en notas y promocion---------------")
print(df_orders.isnull().sum())
print("-------la desicion fue relleno con 0 campos numericos y con 'sin pedido' el srt--------------")
#En este caso decidí no borrar los nulos ya que representan en la columna promotion_id : 33 que son 67% y en notes el 18 que serian 82%, 
# como son mas del 5% es decir no son pocos, hay que rellenar con 0 (porque s float) la ucencia de promoción  y con “sin nota” (string)
#  para la ausencia de notas ,respectivamente
#hago una copia del data set para no modificar el original
df_orders_rellenar = df_orders.copy()
#relleno los nulos
df_orders_rellenar['notes'] = df_orders_rellenar['notes'].fillna("sin pedido")
df_orders_rellenar['promotion_id'] = df_orders_rellenar['promotion_id'].fillna(0)
#verifico que no haya nulos
print(df_orders_rellenar.info())
#verifico que se haya rellenado los nulos
print("---------verifico que los nulos se hayan rellenado   EN ORDERS   ------------")
print(df_orders_rellenar.isnull().sum())
print("------------------cuantos nulos hay en esta tabla categories, porque vi! que habia nulos en parent_category_id---------------")
print(df_categories.isnull().sum())
#en este caso en la csv de categories, se observaron cierta incosostenci9a en la realcion de padre-hijo en Alimentos → Juguetes y Automotriz → Juguetes (es decir era un alimeto y decia que pertenecia a juguetes ). Por eso decidi eliminarlas a esas filas
print("---------veo las filas de categories que tienen nulos en parent_category_id porque presentan inconsistencias, peor decido no borrarlas ya que pueden ser errores de la fuente de datos---------------")

#df_categories_borrar_nulos = df_categories[df_categories['parent_category_id'].notna()]
#print(df_categories_borrar_nulos)

#voy a buscar duplicados en todos los csv ,pero solo en columnas especificas
print("------------------cantidad de filas duplicadas en los csv en genral , NO EN UNA COLUMNA ESPECIFICA   --------------- ")
duplicados = df_orders.duplicated().sum()
duplicados1 = df_customers.duplicated().sum()
duplicados2 = df_products.duplicated().sum()
duplicados3 = df_reviews.duplicated().sum()
duplicados4 = df_order_items.duplicated().sum()
duplicados5 = df_brands.duplicated().sum()
duplicados6 = df_inventory.duplicated().sum()
duplicados7 = df_promotions.duplicated().sum()
duplicados8 = df_suppliers.duplicated().sum()
duplicados9 = df_warehouses.duplicated().sum()
duplicados10 = df_categories.duplicated().sum()
print(f"Duplicados encontrados: {duplicados}")
print(f"Duplicados encontrados: {duplicados1}")
print(f"Duplicados encontrados: {duplicados2}")
print(f"Duplicados encontrados: {duplicados3}")
print(f"Duplicados encontrados: {duplicados4}")
print(f"Duplicados encontrados: {duplicados5}")
print(f"Duplicados encontrados: {duplicados6}")
print(f"Duplicados encontrados: {duplicados7}")
print(f"Duplicados encontrados: {duplicados8}")
print(f"Duplicados encontrados: {duplicados9}")
print(f"Duplicados encontrados: {duplicados10}")
print("----")
print("------------------cantidad de filas duplicadas en los csv solo en la oclumnas de id--------------- ")
df_orders_clean=df_orders.duplicated(subset=['order_id']).sum()
print(f"orders: {df_orders_clean}")

df_customers_clean=df_customers.duplicated(subset=['customer_id']).sum()
print(f"customers: {df_customers_clean}")
df_products_clean=df_products.duplicated(subset=['product_id']).sum()
print(f"products: {df_products_clean}")
df_reviews_clean=df_reviews.duplicated(subset=['review_id']).sum()
print(f"reviews: {df_reviews_clean}")
df_order_items_clean=df_order_items.duplicated(subset=['order_item_id']).sum()
print(f"order_items: {df_order_items_clean}")
df_brands_clean=df_brands.duplicated(subset=['brand_id']).sum()
print(f"brands: {df_brands_clean}")
df_inventory_clean=df_inventory.duplicated(subset=['inventory_id']).sum()
print(f"inventory: {df_inventory_clean}")
df_promotions_clean=df_promotions.duplicated(subset=['promotion_id']).sum()
print(f"promotions: {df_promotions_clean}")
df_suppliers_clean=df_suppliers.duplicated(subset=['supplier_id']).sum()
print(f"suppliers: {df_suppliers_clean}")
df_warehouses_clean=df_warehouses.duplicated(subset=['warehouse_id']).sum()
print(f"warehouses: {df_warehouses_clean}")
df_categories_clean=df_categories.duplicated(subset=['category_id']).sum()
print(f"categories: {df_categories_clean}")

print("---------------------corregir lso tipo de datos-----------------------")
#voy a ver los tipo de datos de cada csv
print(df_orders.dtypes)
print(df_customers.dtypes)
print(df_products.dtypes)
print(df_reviews.dtypes)
print(df_order_items.dtypes)
print(df_brands.dtypes)
print(df_inventory.dtypes)
print(df_promotions.dtypes)
print(df_suppliers.dtypes)
print(df_warehouses.dtypes)
print(df_categories.dtypes)
print("--------------------como ver lso tipo de datos de una forma mas eficiente y no tener qu estar escribiendo 11 lineas----")
#un bucle (loop). Esto hará que Python recorra cada "caja" y te muestre su información automáticamente.
#Agrega este código al final de tu script para tener un reporte general:
# Creamos un diccionario con todas tus tablas para identificarlas por nombre
tablas = {
    "Orders": df_orders,
    "reviews": df_reviews,
    "promocion":df_promotions,
    "suppliers":df_suppliers,
    "warehouses":df_warehouses,
    "brands":df_brands,
    "inventory":df_inventory,
    "customers":df_customers,
    "products":df_products,
    "order_items":df_order_items,
    "categories": df_categories
}

print("\n--- REVISIÓN GENERAL DE TIPOS DE DATOS ---")
for nombre, df in tablas.items():
    print(f"\nTipos de datos en {nombre}:")
    print(df.dtypes)  # Aquí usamos el atributo dtypes para una vista limpia 

#voy a segior  creando copias de los archivos asi el original em queda intacto por las dudas, como hice para los balores nulos 
#para hacer las copias de una uso un diccionario = {
df_copias_= {
    "Orders": df_orders,
    "reviews": df_reviews,
    "promocion":df_promotions,
    "suppliers":df_suppliers,
    "warehouses":df_warehouses,
    "brands":df_brands,
    "inventory":df_inventory,
    "customers":df_customers,
    "products":df_products,
    "order_items":df_order_items,
    "categories": df_categories
   }
for nombre,df in df_copias_.items():
    df_copias_[nombre]=df.copy()
    print(f"copia creadad para {nombre}")

#Empiezo a tarbajar en las tranformaciones , pero sobre las copias que hice
print("----------------------Empiezo a tarbajar en las tranformaciones , pero sobre las copias que hice----------------------")

#en orders tenia fecha y estaba como string y lo pase a datetime
df_copias_['Orders']['order_date']=pd.to_datetime(df_copias_['Orders']['order_date'])

#en promociones tenia fecha y estaba como string y lo pase a datetime
df_copias_['promocion']['start_date']=pd.to_datetime(df_copias_['promocion']['start_date'])
df_copias_['promocion']['end_date']=pd.to_datetime(df_copias_['promocion']['end_date'])

#en inventory tenia fecha y estaba como string y lo pase a datetime
df_copias_['inventory']['last_restock_date']=pd.to_datetime(df_copias_['inventory']['last_restock_date'])

#en customers tenia fechas y estaba como string y lo pase a datetime
df_copias_['customers']['birth_date']=pd.to_datetime(df_copias_['customers']['birth_date'])
df_copias_['customers']['registration_date']=pd.to_datetime(df_copias_['customers']['registration_date'])
df_copias_['customers']['last_login']=pd.to_datetime(df_copias_['customers']['last_login'])


#en products  temia fecha y estaba como string y lo pase a datetime
df_copias_['products']['created_at']=pd.to_datetime(df_copias_['products']['created_at'])
df_copias_['products']['updated_at']=pd.to_datetime(df_copias_['products']['updated_at'])

#reviews tenia fecha y estaba como string y lo pase a datetime
df_copias_['reviews']['created_at']=pd.to_datetime(df_copias_['reviews']['created_at'])

#categories tenia actegoria que es numero  y lo tengo como float y lo pase a int!! 
'''
La razón por la que la columna parent_category_id sigue apareciendo como float64 después de usar pd.to_numeric es la presencia de valores nulos (NaN)
. En Pandas, los números enteros estándar no pueden contener valores nulos; cuando una columna numérica tiene celdas vacías, Pandas la convierte automáticamente a tipo flotante para poder representar esos nulos como NaN
.
Para solucionar esto y que la columna sea de tipo entero en tu proceso ETL, tienes dos caminos principales dependiendo de cómo quieras manejar esos nulos:
 Opción A: Rellenar nulos con 0 y convertir a entero (Recomendada), en fin por esta la conversion aunque la hice sigue siendo float ya que  a los nulos no los borre ni los converti en 0, pero porque la tabla el sentido que tiene no es muy relevante.
'''
df_copias_['categories']['parent_category_id']=pd.to_numeric(df_copias_['categories']['parent_category_id'], errors='coerce')



#verificamos los cambios de los tipos de datos que realizamos de todos los csv
print("\ncorroboramos los tipos se datos si se cambiaron :",df_copias_['Orders'].dtypes)

#tambien lo po dedemos hacer mas eficicente  que revisar la tabla o ir 1 por 1.Con pandas podemos consultar los tipos de datos de un subconjunto específico 
# de columnas pasando una lista de nombres entre corchetes dobles, es decir de las columnas ue querramos ocnsultar y ademas lo bueno es que nos parecera el nombre de la ocmlumna cosa que si hacemos ocmo arriva  vemos el resultado


print("\n--vericicacion de Orders----------------\n")
transformaciones_completas_=['order_date']
print(df_copias_['Orders'][transformaciones_completas_].dtypes)

print("\n--vericicacion de promocion----------------\n")
transformaciones_completas_=['start_date','end_date']
print(df_copias_['promocion'][transformaciones_completas_].dtypes)

print("\n--vericicacion de inventory----------------\n")
transformaciones_completas_=['last_restock_date']
print(df_copias_['inventory'][transformaciones_completas_].dtypes)

print("\n--vericicacion de customers----------------\n")
transformaciones_completas_=['birth_date','registration_date','last_login']
print(df_copias_['customers'][transformaciones_completas_].dtypes)

print("\n--vericicacion de products----------------\n")
transformaciones_completas_=['created_at','updated_at']
print(df_copias_['products'][transformaciones_completas_].dtypes)

print("\n--vericicacion de reviews----------------\n")
transformaciones_completas_=['created_at']
print(df_copias_['reviews'][transformaciones_completas_].dtypes)

print("\n--vericicacion de categories----------------\n")
transformaciones_completas_=['parent_category_id']
print(df_copias_['categories'][transformaciones_completas_].dtypes)

print("---------Responde preguntas de negocio---------------")
#TRANSFORM - Respondé preguntas de negocio
# Desafío: Respondé estas 3 preguntas de negocio: 
# 1. ¿Cuáles son los 5 clientes que más gastaron?
#  2. ¿Cuál es el producto más vendido (por cantidad)?
#  3. ¿Cómo evolucionaron las ventas mes a mes?

print ('1') #adrupamos por customer_id y ademas sumamos total_amount
clientes_mas_gastaron=df_copias_['Orders'].groupby('customer_id').agg({'total_amount': 'sum'})
print("-------------------------------------------")
print("clientes que mas gastaron")
print(clientes_mas_gastaron)
print("-------------------------------------------")
print("-------------------------------------------")
print("clientes que mas gastaron ordenados de mayor a menor por la columna total_amount, los 5 primeros")
#les voy a renombrar las columnas para que sea mas entendible
clientes_mas_gastaron=clientes_mas_gastaron.rename(columns={
    'customer_id':'cliente',
    'total_amount':'total_gastado'
    })
print(clientes_mas_gastaron.sort_values(by='total_gastado',ascending=False).head(5))#para que se lieste ordena de froma descendente usamos 'sort_values' y la columna que queremos que tome pàra ordenar '(by='total_amount',ascending=False) y por ultimo cuantas filas queremos que muestres(5)

print("------------------2--producto más vendido por cantidad----------------------")
print("cantidad y precio unitario por producto")
productos_vendidos_por_cantidad=df_copias_['order_items'].groupby('product_id').agg({
    'quantity': 'sum',
    })

print(productos_vendidos_por_cantidad)
print("-------------------------------------------")
print("-------------------------------------------")
print("cantidad vendida por producto ordenados de mayor a menor por la columna quantiti, los 5 primeros")
#voy a renombrar las columnas para que sea mas entendible
productos_vendidos_por_cantidad=productos_vendidos_por_cantidad.rename(columns={
    'product_id':'producto',
    'quantity':'cantidad',
 
    })
print(productos_vendidos_por_cantidad.sort_values(by='cantidad',ascending=False).head(5))#para que se lieste ordena de froma descendente usamos 'sort_values' y la columna que queremos que tome pàra ordenar '(by='quantity',ascending=False) y por ultimo cuantas filas queremos que muestres(5)
#ahora quiero que me digas los 5 productos mas vendidos
print("-------------------------------------------")
print("-------------------------------------------")
print(f"\n📦 Producto más vendido: ID {productos_vendidos_por_cantidad.idxmax()} ({productos_vendidos_por_cantidad.max()} unidades)")
#ahora tambien agregamos con un inner join los nombres de los productos?? 

print("----------------------3------evolucion de ventas----------------------")
#promedio de ventas por mes, osea que noimporta el año, solo los meses enteros 
#vamos a agrupar  por y sumamaos los totales de ventas( total_amount) por mes (order_date).Primero hagouna clumna nueva para que solo tome meses y años , luego lo agrupo  con la suma de los totales, renombro las columnas.
df_nuevaColumaMes=df_copias_['Orders']['order_date'].dt.to_period('M')
df_totales_por_mes=df_copias_['Orders'].groupby(df_nuevaColumaMes).agg({'total_amount': 'sum'}).reset_index()
df_totales_por_mes=df_totales_por_mes.rename(columns={
    'order_date':'mes',
    'total_amount':'total_ventas_mensual'
    })
    
print(df_totales_por_mes)


print("--- Guardando reportes de negocio en /output ---")
# 1. Top 5 Clientes
clientes_mas_gastaron.head(5).to_csv('output/top_5_clientes.csv', index=False)

# 2. Producto más vendido (con nombres)
productos_vendidos_por_cantidad.to_csv('output/ranking_productos.csv', index=False)

# 3. Evolución mensual de ventas
df_totales_por_mes.to_csv('output/evolucion_ventas_mensual.csv', index=False)


#  Guardar las tablas maestras limpias (Fase de Staging finalizada) 
# Ejemplo con la tabla de pedidos ya corregida
df_copias_['Orders'].to_csv('output/pedidos_limpios.csv', index=False)
df_copias_['promocion'].to_csv('output/promociones_limpias.csv', index=False)
df_copias_['inventory'].to_csv('output/inventory_limpias.csv', index=False)
df_copias_['customers'].to_csv('output/customers_limpias.csv', index=False)
df_copias_['products'].to_csv('output/products_limpias.csv', index=False)
df_copias_['order_items'].to_csv('output/order_items_limpias.csv', index=False)
df_copias_['warehouses'].to_csv('output/warehouses_limpias.csv', index=False)
df_copias_['reviews'].to_csv('output/reviews_limpias.csv', index=False)
df_copias_['categories'].to_csv('output/categories_limpias.csv', index=False)
df_copias_['suppliers'].to_csv('output/suppliers_limpias.csv', index=False)

print("✅ Archivos CSV guardados en output/ con exito.")


print("\n--- 💾 Iniciando etapa de (LOAD) guardar paquets")

# GUARDAR TABLAS MAESTRAS LIMPIAS (En Parquet para alto rendimiento)
df_orders_rellenar.to_parquet('output/ecommerce_orders_limpio.parquet', index=False, engine='pyarrow')
df_customers.to_parquet('output/ecommerce_customers_limpio.parquet', index=False)
df_products.to_parquet('output/ecommerce_products_limpio.parquet', index=False)
df_order_items.to_parquet('output/ecommerce_order_items_limpio.parquet', index=False)
df_reviews.to_parquet('output/ecommerce_reviews_limpio.parquet', index=False)
df_inventory.to_parquet('output/ecommerce_inventory_limpio.parquet', index=False)

df_categories.to_parquet('output/ecommerce_categories_limpio.parquet', index=False)
df_promotions.to_parquet('output/ecommerce_promotions_limpio.parquet', index=False)
df_suppliers.to_parquet('output/ecommerce_suppliers_limpio.parquet', index=False)
df_warehouses.to_parquet('output/ecommerce_warehouses_limpio.parquet', index=False)
print("✅ Archivos Parquet guardados en output/ con exito.")


#Comparar tamaños de los archivos CSV y Parquet
tamanio_csv_orders=os.path.getsize('output/pedidos_limpios.csv')/1024
tamanio_csv_customers=os.path.getsize('output/customers_limpias.csv')/1024
tamanio_csv_products=os.path.getsize('output/products_limpias.csv')/1024
tamanio_csv_promotions=os.path.getsize('output/promociones_limpias.csv')/1024
tamanio_csv_order_items=os.path.getsize('output/order_items_limpias.csv')/1024
tamanio_csv_reviews=os.path.getsize('output/reviews_limpias.csv')/1024
tamanio_csv_inventory=os.path.getsize('output/inventory_limpias.csv')/1024
tamanio_csv_categories=os.path.getsize('output/categories_limpias.csv')/1024
tamanio_csv_suppliers=os.path.getsize('output/suppliers_limpias.csv')/1024
tamanio_csv_warehouses=os.path.getsize('output/warehouses_limpias.csv')/1024

tamanio_parquet_orders=os.path.getsize('output/ecommerce_orders_limpio.parquet')/1024
tamanio_parquet_customers=os.path.getsize('output/ecommerce_customers_limpio.parquet')/1024
tamanio_parquet_products=os.path.getsize('output/ecommerce_products_limpio.parquet')/1024
tamanio_parquet_promotions=os.path.getsize('output/ecommerce_promotions_limpio.parquet')/1024
tamanio_parquet_order_items=os.path.getsize('output/ecommerce_order_items_limpio.parquet')/1024
tamanio_parquet_reviews=os.path.getsize('output/ecommerce_reviews_limpio.parquet')/1024
tamanio_parquet_inventory=os.path.getsize('output/ecommerce_inventory_limpio.parquet')/1024
tamanio_parquet_categories=os.path.getsize('output/ecommerce_categories_limpio.parquet')/1024
tamanio_parquet_suppliers=os.path.getsize('output/ecommerce_suppliers_limpio.parquet')/1024
tamanio_parquet_warehouses=os.path.getsize('output/ecommerce_warehouses_limpio.parquet')/1024




print(f"📊 Auditoría de almacenamiento (Orders):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_orders:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_orders:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Customers):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_customers:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_customers:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Products):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_products:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_products:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Promotions):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_promotions:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_promotions:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Order Items):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_order_items:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_order_items:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Reviews):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_reviews:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_reviews:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Inventory):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_inventory:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_inventory:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Categories):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_categories:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_categories:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Suppliers):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_suppliers:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_suppliers:.1f} KB")
print(f"📊 Auditoría de almacenamiento (Warehouses):")
print(f"   - Tamaño estimado en CSV: {tamanio_csv_warehouses:.1f} KB")
print(f"   - Tamaño real en Parquet: {tamanio_parquet_warehouses:.1f} KB")

#  Fin del cronómetro al terminar la carga
fin_proceso = time.time()

#  Cálculo de la duración total
duración_total = fin_proceso - inicio_proceso

print(f"--- ETL Finalizado con éxito ---")
print(f"Tiempo total de ejecución: {duración_total:.2f} segundos")