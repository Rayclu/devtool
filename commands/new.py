import utils.fs as fs
from core.detector import has
from core.executor import run_cmd

def run(args):
    print(args)
    if len(args) < 2:
        print("Using: devtool new <stack> <name>")
        print("Supported stacks: django")
        raise "Stack does not specified."

    stack = args[0]
    name = args[1]

    if stack == "django":
        create_django(name)
    else:
        print("❌ Stack not supported")


def create_django(name, path=''):
    print("[INFO] Creating django project...")

    if not has("python3"):
        print("❌ Python not installed")
        return
    import platform
    match platform.system():
        case "Linux":
            if not path != '': 
                try:
                    fs.mkdir(f"~/Desktop/{name}")
                except:
                    fs.mkdir(f"~/Escritorio/{name}")
        case _:
            pass
    fs.chdir(name)

    print("[RUN] Creando venv...")
    run_cmd("python3 -m venv venv")

    print("[RUN] Instalando Django...")
    run_cmd("venv/bin/pip install --upgrade pip")
    run_cmd("venv/bin/pip install django")

    print("[RUN] Inicializando proyecto Django...")
    run_cmd("venv/bin/django-admin startproject app .")

    print("✔ Proyecto creado en:", fs.getcwd())
