#!/bin/bash

echo "🔧 Iniciando setup del proyecto Django + MySQL..."

# 2. Levantar base de datos con Docker Compose
echo "🐬 Levantando MySQL con Docker Compose..."
docker compose --env-file ./Proyecto/.env up -d


# Esperar a que MySQL esté listo
echo "⏳ Esperando a que MySQL esté listo..."
sleep 10

# 3. Ejecutar el script SQL de inicialización (si existe)
if [ -f "Proyecto/Backend/cmd/bd/init.sql" ]; then
  echo "📄 Ejecutando script SQL de inicialización..."
  docker exec -i mysql-demo-compose mysql -u testuser -ppassword testdb < ./Proyecto/Backend/cmd/db/init.sql
  # docker exec -it mysql-demo-compose mysql -h 127.0.0.1 -u testuser -ppassword testdb < ./Proyecto/Backend/cmd/db/init.sql
  echo "✅ Script SQL ejecutado"
else
  echo "⚠️  No se encontró init.sql en Proyecto/Backend/cmd/bd/"
fi

# 4. Configurar entorno virtual de Python
echo "🐍 Configurando entorno virtual de Python..."
cd Proyecto/Backend || exit

if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
source venv/bin/activate

# 5. Instalar dependencias
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt

# 6. Crear proyecto Django si no existe
if [ ! -f "manage.py" ]; then
  echo "🎯 Creando proyecto Django..."
  django-admin startproject backend .
  echo "✅ Proyecto Django creado"
fi

# 7. Crear app 'core' si no existe
if [ ! -d "core" ]; then
  echo "📱 Creando app 'core'..."
  python manage.py startapp core
  echo "✅ App 'core' creada"
  echo "⚠️  Recuerda agregar 'core' a INSTALLED_APPS en settings.py"
fi

# 8. Aplicar migraciones
echo "🔄 Aplicando migraciones de Django..."
python manage.py makemigrations
python manage.py migrate

# 9. Crear superusuario (opcional)
echo ""
read -p "¿Deseas crear un superusuario para Django admin? (s/n): " crear_super

if [ "$crear_super" = "s" ] || [ "$crear_super" = "S" ]; then
  python manage.py createsuperuser
fi

cd ../../

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
echo "🔧 Panel admin en: http://127.0.0.1:8000/admin"<