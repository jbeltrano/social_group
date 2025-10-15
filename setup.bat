@echo off
echo "🔧 Iniciando setup del proyecto Django + MySQL..."

rem 2. Levantar base de datos con Docker Compose
echo "🐬 Levantando MySQL con Docker Compose..."
docker compose up -d


rem Esperar a que MySQL esté listo
echo "⏳ Esperando a que MySQL esté listo..."
timeout /t 10 > nul


rem 3. Ejecutar el script SQL de inicialización (si existe)
if exist "Proyecto/Backend/cmd/db/init.sql" (
    echo "📄 Ejecutando script SQL de inicialización..."
    docker exec -i mysql-demo-compose mysql -u testuser -ppassword testdb < ./Proyecto/Backend/cmd/db/init.sql
    
    echo "✅ Script SQL ejecutado"
) else (
    echo "⚠️  No se encontró init.sql en Proyecto/Backend/cmd/db/"
)


rem 4. Instalar dependencias de Python
cd "Proyecto"
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt


rem 5. Crear proyecto Django si no existe
if not exist "manage.py" (
    echo "🎯 Creando proyecto Django..."
    django-admin startproject CookShare .
    echo "✅ Proyecto Django creado"
)


rem 6. Crear modulo core para MVC si no existe
if not exist "core" (
    echo "🎯 Creando modulo core para MVC..."
    python manage.py startapp core
    echo "✅ Modulo core creado"
)

rem 7. Crear estructura MVC dentro del modulo core
mkdir "core/models" "core/controllers" "core/views" "core/templates"


rem 8. Crear archivos __init__.py en cada carpeta para que Python las reconozca como paquetes
type nul > "core/models/__init__.py"
type nul > "core/controllers/__init__.py"
type nul > "core/views/__init__.py"
type nul > "core/templates/__init__.py"


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