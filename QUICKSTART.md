# 🚀 DevTool — CLI para Generar Proyectos Backend

Una herramienta de línea de comandos para crear y configurar proyectos backend rápidamente.

## 📋 Estructura del Proyecto

```
devtool/
├── cli.py                    # Entrada principal
├── commands/                 # Comandos disponibles
│   ├── new.py              # Crear nuevos proyectos
│   ├── doctor.py           # Verificar entorno
│   └── run.py              # Ejecutar proyectos
├── core/                    # Lógica central
│   ├── detector.py         # Detecta herramientas disponibles
│   ├── validator.py        # Valida dependencias
│   ├── runtime.py          # Selecciona runtime
│   └── executor.py         # Ejecuta comandos del sistema
├── templates/              # Plantillas de proyectos
│   └── django/             # Template de Django
├── docker/                 # Templates Docker
│   ├── django.tpl          # Dockerfile para Django
│   └── node.tpl            # Dockerfile para Node/Bun
├── utils/                  # Utilidades
│   ├── exec.py             # Ejecución de comandos
│   └── fs.py               # Operaciones de filesystem
├── Dockerfile              # Para ejecutar DevTool en Docker
├── requirements.txt        # Dependencias Python
└── .dockerignore           # Archivos a ignorar en Docker
```

## 🚀 Instalar y Usar

### Opción 1: Ejecución Local
```bash
cd devtool
python cli.py doctor        # Verificar entorno
python cli.py new django myapp
```

### Opción 2: Con Docker (Recomendado)

Sin instalar Python en tu máquina:
```bash
git clone <repo>
cd devtool

# Construir imagen
docker build -t devtool .

# Ejecutar
docker run -it -v $(pwd):/app devtool new django myapp
```

✨ Los proyectos generados aparecerán en tu carpeta actual.

## 📝 Comandos Disponibles

### `devtool doctor`
Verifica que herramientas tienes disponibles:
```bash
python cli.py doctor

[CHECK] Estado del entorno:

✔ Python
✔ Node
✔ npm
❌ Bun
```

### `devtool new <stack> <nombre>`
Crea un nuevo proyecto:
```bash
python cli.py new django myblog
python cli.py new nest myapi
```

### `devtool run`
Ejecuta un proyecto (en desarrollo)

## 🐳 Docker Explicado Simple

### ¿Qué problema resuelve Docker?

**Sin Docker:**
- "Me falta Python"
- "Tengo Python 3.10 pero necesito 3.12"
- "En mi compu funciona pero en la tuya no"

**Con Docker:**
- Todo viene empaquetado
- Funciona en cualquier máquina
- No instalas nada en tu sistema

### ¿Cómo funciona?

1. **Dockerfile = Receta**
   - Define todo lo que la app necesita
   - Python version, dependencias, etc.

2. **Imagen = Plantilla**
   ```bash
   docker build -t devtool .     # Crear imagen
   ```

3. **Contenedor = Instancia**
   ```bash
   docker run -it devtool        # Ejecutar imagen
   ```

### Flujo Step-by-Step

```bash
git clone https://github.com/tu-usuario/devtool
cd devtool

# Paso 1: Crear imagen Docker
docker build -t devtool .
# Esto ejecuta todas las instrucciones del Dockerfile
# una sola vez (caché después)

# Paso 2: Ejecutar
docker run -it -v $(pwd):/app devtool new django myapp
```

**`-v $(pwd):/app`** = "Mi carpeta actual ↔️ `/app` dentro del contenedor"

Los proyectos que crees aparecen en tu máquina automáticamente.

## 🎯 Casos de Uso

### Crear un proyecto Django rápido
```bash
docker run -it -v $(pwd):/app devtool new django shopify_clone
```

### Verificar tu entorno
```bash
python cli.py doctor
```

### Desarrollo local
```bash
python cli.py new nest api_rest --runtime bun
```

## 🔧 Próximas Mejoras

- [ ] Soporte para Node/Bun
- [ ] Flag `--docker` para generar Dockerfile automático
- [ ] Comando `config` para preferencias globales
- [ ] Más templates (FastAPI, NestJS, .NET)
- [ ] Bases de datos integradas

## 📚 Architecture Decisions

✅ **No instalamos lenguajes automáticamente**
- Evita problemas de permisos
- El usuario controla su sistema

✅ **Validamos dependencias**
- Mejor UX
- Errores claros

✅ **Soporte multi-runtime**
- Node, Bun, Python, .NET
- Flexible

✅ **Docker opcional**
- No obligatorio
- Para reproducibilidad

## 🎓 Aprender Más

### Cómo funciona el Dockerfile
```dockerfile
FROM python:3.12              # Imagen base con Python
WORKDIR /app                  # Carpeta de trabajo
COPY . .                      # Copiar código
RUN pip install --upgrade pip # Instalar herramientas
CMD ["python", "cli.py"]      # Comando por defecto
```

### Variables de Entorno
Si necesitas pasar valores:
```bash
docker run -e DJANGO_ENV=production -it devtool ...
```

---

**Hecho por desarrolladores para desarrolladores** 🚀
