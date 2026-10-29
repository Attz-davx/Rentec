import MySQLdb

host = "147.182.171.222"
port = 23026
user = "avnadmin"
password = "TU_PASSWORD"
database = "defaultdb"

try:
    db = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        db=database,
        ssl={"fake": True}
    )
    cursor = db.cursor()
    
    # Consulta de prueba para ver las tablas creadas
    cursor.execute("SHOW TABLES;")
    tablas = cursor.fetchall()
    
    print("¡Conexión exitosa! Las tablas en tu base de datos son:")
    for tabla in tablas:
        print(f"- {tabla[0]}")

except Exception as e:
    print(f"Error al conectar: {e}")

finally:
    if 'db' in locals() and db:
        db.close()