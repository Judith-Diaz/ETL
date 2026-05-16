import pandas as pd
import glob
import os
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
df_copias_ = {
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

#en orders
df_copias_Orders['order_date']=pd.to_datetime(df_copias_Orders['order_date'])
df_copias_Orders[order_number]= pd.to_string(df_copias_Orders[order_number])
#en 
df_copias_Orders['ship_date']=pd.to_datetime(df_copias_Orders['ship_date'])
print("----------copia de orders limpiaCreada------------")