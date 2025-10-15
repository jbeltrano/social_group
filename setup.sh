#!/bin/bash

echo "🔧 Iniciando setup del proyecto Django + MySQL..."

# 2. Levantar base de datos con Docker Compose
echo "🐬 Levantando MySQL con Docker Compose..."
docker compose up -d


# Esperar a que MySQL esté listo
echo "⏳ Esperando a que MySQL esté listo..."
sleep 10


# 3. Ejecutar el script SQL de inicialización (si existe)
if [ -f "Proyecto/Backend/cmd/db/init.sql" ]; then
  echo "📄 Ejecutando script SQL de inicialización..."
  docker exec -i mysql-demo-compose mysql -u testuser -ppassword testdb < ./Proyecto/Backend/cmd/db/init.sql

  echo "✅ Script SQL ejecutado"
else
  echo "⚠️  No se encontró init.sql en Proyecto/Backend/cmd/db/"
fi


# 4. Instalar dependencias de Python
cd Proyecto || exit
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt


# 5. Crear proyecto Django si no existe
if [ ! -f "manage.py" ]; then
  echo "🎯 Creando proyecto Django..."
  django-admin startproject CookShare .
  echo "✅ Proyecto Django creado"
fi


# 6. Crear modulo core para MVC si no existe
if [ ! -d "core" ]; then
  echo "🎯 Creando modulo core para MVC..."
  python manage.py startapp core
  echo "✅ Modulo core creado"
fi

# 7. Crear estructura MVC dentro del modulo core
mkdir core/models core/controllers core/views core/templates


# 8. Crear archivo __init__.py en cada carpeta para que Python las reconozca como paquetes
touch core/models/__init__.py
touch core/controllers/__init__.py
touch core/views/__init__.py
touch core/templates/__init__.py


echo ""
echo "✅ Setup finalizado."
echo ""
echo "📌 Próximos pasos:"
echo "   1. cd Proyecto/Backend"
echo "   2. source venv/bin/activate"
echo "   3. python test_connection.py  # Probar conexión a MySQL"
echo "   4. python manage.py runserver # Iniciar servidor Django"
echo ""
echo "🌐 Django estará disponible en: http://127.0.0.1:8000"
echo "🔧 Panel admin en: http://127.0.0.1:8000/admin"