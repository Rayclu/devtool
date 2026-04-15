"""Manejo de sistema de archivos"""
import os
import shutil

def mkdir(path):
    """Crea directorio"""
    os.makedirs(path, exist_ok=True)

def copy_tree(src, dst):
    """Copia árbol de directorios"""
    shutil.copytree(src, dst)
def cd(path):
    """"""
    os.chdir(path)
def rm_tree(path):
    """Elimina árbol de directorios"""
    shutil.rmtree(path)

def getcwd():
    return os.getcwd()