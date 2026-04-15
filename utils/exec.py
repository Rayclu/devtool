"""Ejecución de comandos avanzada"""
import subprocess

def run(cmd, shell=False):
    """Ejecuta comando y retorna output"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=shell)
        return result.stdout, result.returncode
    except Exception as e:
        return str(e), 1
