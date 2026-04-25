
🧠 🧩 Flujo completo del CLI.

[Usuario]
   ↓
[CLI: devtool]
   ↓
[Parseo de comandos]
   ↓
[Validaciones (entorno)]
   ↓
[Selección de stack/runtime]
   ↓
[Generación de proyecto]
   ↓
[Configuración (opcional: Docker/red)]
   ↓
[Output listo para ejecutar]


🔥 🔍 Flujo detallado.
┌──────────────────────────────┐
│ Usuario ejecuta comando      │
│ devtool new <stack> <name>   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Parseo de argumentos         │
│ - stack (django, nest, etc)  │
│ - flags (--runtime, --docker)│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Validación de stack          │
│ ¿existe ese template?        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Detección de entorno         │
│ - node? bun? python? dotnet? │
└──────────────┬───────────────┘
               ↓
        ┌───────────────┐
        │ ¿runtime dado?│
        └──────┬────────┘
               ↓
     ┌───────────────┐
     │ NO            │
     │ Auto-detect   │
     └──────┬────────┘
            ↓
   ┌─────────────────────┐
   │ ¿múltiples opciones?│
   └──────┬──────────────┘
          ↓
   ┌───────────────┐
   │ Sí → preguntar│
   │ No → usar uno │
   └───────────────┘

               ↓
┌──────────────────────────────┐
│ Validación de dependencias   │
│ (ej: python, django, bun)    │
└──────────────┬───────────────┘
               ↓
      ┌──────────────────┐
      │ ¿faltan cosas?   │
      └──────┬───────────┘
             ↓
   ┌───────────────┐
   │ Sí → error +  │
   │ instrucciones │
   └───────────────┘
             ↓ NO
┌──────────────────────────────┐
│ Generación de proyecto       │
│ - copiar template base       │
│ - renombrar archivos         │
│ - inicializar config         │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Setup runtime                │
│ - npm install / bun install  │
│ - pip install                │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ ¿flag --docker?              │
└──────┬───────────────────────┘
       ↓
 ┌───────────────┐
 │ Sí            │
 │ Generar:      │
 │ - Dockerfile  │
 │ - compose.yml │
 └───────────────┘

               ↓
┌──────────────────────────────┐
│ Output final                 │
│ ✔ Proyecto creado            │
│ ✔ Cómo ejecutarlo            │
└──────────────────────────────┘

🧠 🧩 Estructura interna.
devtool/
│
├── cli.py              ← entrada principal
├── commands/
│   ├── new.py          ← crear proyectos
│   ├── run.py          ← ejecutar
│   └── doctor.py       ← validar entorno
│
├── core/
│   ├── detector.py     ← detecta node/bun/python
│   ├── validator.py    ← chequea dependencias
│   ├── runtime.py      ← decide qué usar
│
├── templates/
│   ├── django/
│   ├── nest/
│   ├── dotnet/
│
├── docker/
│   ├── django.tpl
│   ├── node.tpl
│
└── utils/
    ├── exec.py         ← ejecutar comandos
    └── fs.py           ← manejo de archivos

🔥 Ejecución:
devtool new django blog --docker


[INFO] Detectando entorno...
✔ Python detectado
✔ pip detectado

[INFO] Instalando dependencias...
✔ Django instalado

[INFO] Generando proyecto Django...
✔ Estructura creada

[INFO] Configurando Docker...
✔ Dockerfile generado
✔ docker-compose generado

[OK] Proyecto listo 🚀

Para correr:
cd blog
docker-compose up
