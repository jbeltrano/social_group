#!/bin/bash

echo "🔧 Iniciando setup del proyecto Django + MySQL..."

# 2. Levantar base de datos con Docker Compose
echo "🐬 Levantando MySQL con Docker Compose..."
docker compose up -d


# Esperar a que MySQL esté listo
echo "⏳ Esperando a que MySQL esté listo..."
sleep 60


# 3. Ejecutar el script SQL de inicialización (si existe)
if [ -f "Proyecto/Backend/cmd/db/init.sql" ]; then
  
  echo "📄 Ejecutando script SQL de inicialización..."
  docker exec -i mysql-demo-compose mysql -u root -prootpassword testdb < ./Proyecto/Backend/cmd/db/init.sql
  echo "✅ Script SQL ejecutado"
else
  echo "⚠️  No se encontró init.sql en Proyecto/Backend/cmd/db/"
fi


# 4. Configurando entorno virtual y instalacion de dependencias de Python
cd Proyecto || exit

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  echo "🌐 Creando entorno virtual..."
  python3 -m venv venv
  echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r Backend/requirements.txt


# 5. Aplicar migraciones 
echo "🗃️  Aplicando migraciones de Django..."
python manage.py makemigrations
python manage.py migrate

# 6. Ejecutar tests
echo "🧪 Ejecutando tests de Django..."
pytest

echo ""
echo "✅ Setup finalizado."
echo ""
echo "📌 Próximos pasos:"
echo "   1. Configurar la base de datos en CookShare/settings.py"
echo "   2. Agregar 'core' a INSTALLED_APPS en CookShare/settings.py"
echo "   3. Cargar las variables de entorno necesarias"
echo "   4. python manage.py runserver # Iniciar servidor Django"
echo ""
echo "🌐 Django estará disponible en: http://127.0.0.1:8000"
echo "🔧 Panel admin en: http://127.0.0.1:8000/admin"