#!/bin/bash

# Cargar variables de entorno desde .env si existe
if [ -f ".env" ]; then
  export $(cat .env | grep -v '#' | xargs)
fi

# Verificar variables de entorno necesarias
if [ -z "${DB_USER}" ] || [ -z "${DB_PASSWORD}" ] || [ -z "${DB_NAME}" ] || [ -z "${DB_PORT}" ] || [ -z "${DB_PASSWORD_ROOT}" ]; then
  echo "❌ Error: Faltan variables de entorno requeridas"
  echo "Por favor, asegúrate de que las siguientes variables estén definidas:"
  echo "DB_USER, DB_PASSWORD, DB_NAME, DB_PORT, DB_PASSWORD_ROOT"
  exit 1
fi

echo "🔧 Iniciando setup del proyecto..."

# 1. Levantar base de datos con Docker Compose
echo "🐘 Levantando MySql con Docker Compose..."
if command -v docker-compose >/dev/null 2>&1; then
  docker-compose up -d
  # docker compose --env-file /ruta/personalizada/.env up -d
else
  docker compose up -d
fi

# Esperar unos segundos a que MySql esté listo
echo "⏳ Esperando a que la base de datos esté lista..."
sleep 5

# 2. Ejecutar el script SQL de inicialización
if [ -f "Proyecto/Backend/cmd/bd/init.sql" ]; then
  echo "📄 Ejecutando script SQL de inicialización..."
  # Usando las variables de entorno definidas
  docker exec -i mysql_container mysql -u "${DB_USER}" -p"${DB_PASSWORD}" "${DB_NAME}" < Proyecto/Backend/cmd/bd/init.sql
else
  echo "⚠️ No se encontró init.sql en Proyecto/Backend/cmd/bd/"
fi

# 3. Backend (Python)
echo "📦 Configurando Backend en Python"
cd Proyecto/Backend || exit

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  echo "🐍 Creando entorno virtual de Python..."
  python -m venv venv
fi

# Activar entorno virtual
echo "🔄 Activando entorno virtual..."
source venv/Scripts/activate

# Instalar dependencias si existe requirements.txt
if [ -f "requirements.txt" ]; then
  echo "📦 Instalando dependencias de Python..."
  pip install -r requirements.txt
else
  echo "⚠️ No se encontró requirements.txt"
fi

cd ../../

# 4. Frontend (opcional)
#read -p "¿Quieres usar Vue o React? (vue/react): " choice
#
#if [ "$choice" = "vue" ]; then
#  echo "📦 Creando frontend con Vue..."
#  cd Proyecto || exit
#  npm create vue@latest Frontend
#  cd ..
#elif [ "$choice" = "react" ]; then
#  echo "📦 Creando frontend con React..."
#  cd Proyecto || exit
#  npx create-react-app Frontend
#  cd ..
#else
#  echo "⚠️ Opción no válida. No se instaló frontend."
#fi

echo "✅ Setup finalizado."
