import os

def run_cmd(cmd):
    """Ejecuta un comando del sistema"""
    print(f"[RUN] {cmd}")
    return os.system(cmd)
