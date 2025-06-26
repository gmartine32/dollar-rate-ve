# 📈 API de Tasa de Cambio USD - Bolívar (VE)

Esta API permite consultar la tasa del dólar en Venezuela y su variación diaria. Desarrollada con **Flask**, PostgreSQL y arquitectura **hexagonal**, implementa buenas prácticas, logging y control de acceso mediante API Key.

---

## 🚀 Funcionalidades

- Obtener la tasa actual del dólar.
- Consultar la tasa por fecha histórica.
- Insertar una nueva tasa (protegido con API Key).
- Seguridad por cabecera `x-api-key`.
- Arquitectura limpia + logs + CORS habilitado.

---

## 📦 Requisitos

- Python 3.11+
- Docker y Docker Compose (para despliegue)
- PostgreSQL 15+

---

## 🧪 Ejecutar localmente (modo desarrollo)

```bash
# 1. Clona el repositorio
git clone https://github.com/tu_usuario/flask-api-dolar.git
cd flask-api-dolar

# 2. Crea y activa entorno virtual
python -m venv .venv
source .venv/bin/activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Copia archivo de variables y edítalo
cp .env.example .env

# 5. Corre la app
python main.py
