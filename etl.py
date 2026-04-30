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
df_orders = pd.read_csv('data/ecommerce_orders.csv')
df_order_items = pd.read_csv('data/ecommerce_order_items.csv')
df_customers = pd.read_csv('data/ecommerce_customers.csv')
df_products = pd.read_csv('data/ecommerce_products.csv')

# Explorar
print(f"\n Resumen:")
print(f"Orders: {len(df_orders)} filas, {len(df_orders.columns)} columnas")
print(f"Order Items: {len(df_order_items)} filas")
print(f"Customers: {len(df_customers)} filas")
print(f"Products: {len(df_products)} filas")

print("\n Primeras filas de orders:")
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
print("------------------cuantos nulos hay en esta tabla---------------")
print(df_orders.isnull().sum())
print("-------la desicion fue relleno con 0 campos numericos y con 'sin pedido' el srt--------------")
#hago una copia del data set para no modificar el original
df_orders_rellenar = df_orders.copy()
#relleno los nulos
df_orders_rellenar['notes'] = df_orders_rellenar['notes'].fillna("sin pedido")
df_orders_rellenar['promotion_id'] = df_orders_rellenar['promotion_id'].fillna(0)
#verifico que no haya nulos
print(df_orders_rellenar.info())
#verifico que se haya rellenado los nulos
print(df_orders_rellenar.isnull().sum())