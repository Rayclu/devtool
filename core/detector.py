import shutil

def has(cmd):
    """Detecta si un comando está disponible en el sistema"""
    return shutil.which(cmd) is not None
