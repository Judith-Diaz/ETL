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
print(df_orders_rellenar.isnull().sum())
print("------------------cuantos nulos hay en esta tabla categories, porque vi! que habia nulos en parent_category_id---------------")
print(df_categories.isnull().sum())
#en este caso en la csv de categories, se observaron cierta incosostenci9a en la realcion de padre-hijo en Alimentos → Juguetes y Automotriz → Juguetes . Por eso decidi eliminarlas
#Detectar duplicados

df_categories[df_categories['parent_category_id'].notna()]###
print("------------------detectar duplicados---------------",df_orders.duplicated().sum())

df_orders.duplicated(subset=['order_id'])
df_order_items.duplicated(subset=['order_item_id'])
df_customers.duplicated(subset=['customer_id'])
df_products.duplicated(subset=['product_id'])
df_reviews.duplicated(subset=['review_id'])
df_brands.duplicated(subset=['brand_id'])
df_inventory.duplicated(subset=['inventory_id'])
df_promotions.duplicated(subset=['promotion_id'])
df_suppliers.duplicated(subset=['supplier_id'])
df_warehouses.duplicated(subset=['warehouse_id'])
df_categories.duplicated(subset=['category_id'])