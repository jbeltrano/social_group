@echo off
echo "🔧 Iniciando setup del proyecto Django + MySQL..."

rem 2. Levantar base de datos con Docker Compose
echo "🐬 Levantando MySQL con Docker Compose..."
docker compose up -d


rem Esperar a que MySQL esté listo
echo "⏳ Esperando a que MySQL esté listo..."
timeout /t 60 > nul


rem 3. Ejecutar el script SQL de inicialización (si existe)
if exist "Proyecto/Backend/cmd/db/init.sql" (
    echo "📄 Ejecutando script SQL de inicialización..."
    docker exec -i mysql-demo-compose mysql -u testuser -ppassword testdb < ./Proyecto/Backend/cmd/db/init.sql
    
    echo "✅ Script SQL ejecutado"
) else (
    echo "⚠️  No se encontró init.sql en Proyecto/Backend/cmd/db/"
)


rem 4. Configurando entorno virtual y instalacion de dependencias de Python
cd "Proyecto"

rem Crear entorno virtual si no existe
if not exist "venv" (
    echo "🌐 Creando entorno virtual..."
    python -m venv venv
    echo "✅ Entorno virtual creado"
)

rem Activar entorno virtual
call venv\Scripts\activate.bat

rem Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r Backend/requirements.txt


rem 5. Crear proyecto Django si no existe
if not exist "manage.py" (
    echo "🎯 Creando proyecto Django..."
    django-admin startproject CookShare .
    echo "✅ Proyecto Django creado"
)

rem 6. Crear app core si no existe
if not exist "core" (
    echo "🧩 Creando app core..."
    python manage.py startapp core
    echo "✅ App core creada"
)


rem 7. Crear estructura MVC dentro del modulo core
mkdir "core/models" "core/controllers" "core/views" "core/templates"


rem 8. Crear archivos __init__.py en cada carpeta para que Python las reconozca como paquetes
type nul > "core/models/__init__.py"
type nul > "core/controllers/__init__.py"
type nul > "core/views/__init__.py"
type nul > "core/templates/__init__.py"

rem 9. Ejecucion del programa
start http://127.0.0.1:8000/
python manage.py runserver


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