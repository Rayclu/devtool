from core.detector import has

def run():
    print("\n[CHECK] Estado del entorno:\n")

    checks = {
        "Python": "python",
        "Node": "node",
        "npm": "npm",
        "Bun": "bun",
    }

    for name, cmd in checks.items():
        status = "✔" if has(cmd) else "❌"
        print(f"{status} {name}")
    
    print()
