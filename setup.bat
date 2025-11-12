@echo off
echo ==============================================
echo "🔧 Iniciando setup del proyecto Django + SQLite3..."
echo ==============================================

rem -------------------------------------------------
rem 1. Crear entorno virtual y preparar dependencias
rem -------------------------------------------------

cd "Proyecto"

if not exist "venv" (
    echo "🌐 Creando entorno virtual..."
    python -m venv venv
    echo "✅ Entorno virtual creado"
)

call venv\Scripts\activate.bat

echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r Backend/requirements.txt


rem -------------------------------------------------
rem 2. Crear base de datos SQLite e inicializar datos
rem -------------------------------------------------

set DB_PATH=Backend\db.sqlite3
set INIT_SQL=Backend\cmd\db\init.sql

echo "🗃️  Configurando base de datos SQLite..."
if exist "%DB_PATH%" (
    echo "⚠️  Eliminando base de datos anterior..."
    del "%DB_PATH%"
)

echo "📄 Creando nueva base de datos SQLite..."
python - <<END
import sqlite3, os
db_path = r"%DB_PATH%"
sql_path = r"%INIT_SQL%"
if os.path.exists(sql_path):
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()
    conn = sqlite3.connect(db_path)
    conn.executescript(sql)
    conn.close()
    print("✅ Script SQL ejecutado correctamente.")
else:
    print("⚠️  No se encontró el archivo:", sql_path)
END


rem -------------------------------------------------
rem 3. Aplicar migraciones y preparar Django
rem -------------------------------------------------

echo "🔧 Aplicando migraciones de Django..."
python manage.py makemigrations
python manage.py migrate

rem -------------------------------------------------
rem 4. Ejecutar tests
rem -------------------------------------------------

echo "🧪 Ejecutando tests de Django..."
pytest

echo ""
echo "✅ Setup completado correctamente."
echo ""
echo "📌 Próximos pasos:"
echo "   1. Asegúrate de que DATABASES usa sqlite3 en settings.py"
echo "   2. Puedes iniciar el servidor con:"
echo "      python manage.py runserver"
echo ""
echo "🌐 Django estará disponible en: http://127.0.0.1:8000"
echo "🔧 Panel admin en: http://127.0.0.1:8000/admin"
echo ==============================================
