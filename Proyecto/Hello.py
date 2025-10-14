#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import MySQLdb
from dotenv import load_dotenv
from datetime import datetime

def main():
    # Cargar variables del archivo .env
    env_path = Path(__file__).resolve().parent.parent.parent / '.env'
    
    if env_path.exists():
        load_dotenv(env_path)
        print("✅ Variables de entorno cargadas desde .env")
    else:
        print("⚠️  No se pudo cargar .env, usando variables de entorno existentes")
    
    # Obtener variables de entorno
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', 3306))
    
    try:
        # Conectar a MySQL
        print(f"🔌 Conectando a MySQL en {db_host}:{db_port}...")
        connection = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        
        # Crear cursor y ejecutar query
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        
        print(f"✅ Conectado a MySQL, hora actual: {result[0]}")
        
        # Cerrar conexión
        cursor.close()
        connection.close()
        
    except MySQLdb.Error as e:
        print(f"❌ Error al conectar con la BD: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()