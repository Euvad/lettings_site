# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# Ajouter le chemin du projet Django
sys.path.insert(0, os.path.abspath(".."))

# Configuration Django pour Sphinx
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")


django.setup()

# -- Project information -----------------------------------------------------
project = "lettings_site"
copyright = "2025, VadimTheZombie"
author = "VadimTheZombie"
release = "03/04/2025"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",  # Générer la documentation automatiquement
    "sphinx.ext.napoleon",  # Supporte les docstrings au format Google/NumPy
    "sphinx.ext.viewcode",  # Ajoute des liens vers le code source
    "sphinx.ext.intersphinx",  # Permet de créer des liens entre plusieurs docs
    "sphinx.ext.todo",  # Permet d'afficher les TODO dans la doc
]

# Active les TODO dans la documentation
todo_include_todos = True

# Inclure les docstrings des classes et des méthodes
autodoc_default_options = {
    "members": True,  # Inclure les attributs et méthodes
    "undoc-members": True,  # Inclure même les éléments sans docstring
    "private-members": True,  # Inclure les méthodes privées (_example)
    "special-members": "__init__",  # Inclure les méthodes spéciales comme __init__
    "inherited-members": True,
    "show-inheritance": True,
}

# Chemin des templates
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"  # Meilleur rendu pour la documentation
html_static_path = ["_static"]
