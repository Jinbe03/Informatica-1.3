from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client.ventas

# Consulta a la base de datos
clientes = db.clientes.find({"edad": {"$gte": 30}})
for cliente in clientes:
    print(cliente)
# 