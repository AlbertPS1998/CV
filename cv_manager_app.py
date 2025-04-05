# -*- coding: utf-8 -*-
"""
Script definitivo: cargas un JSON con tus datos y te genera un CV PDF con diseño espectacular sin mover un dedo.
"""

import os
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# === CONFIGURACIÓN DE RUTAS ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
PROFILE_PATH = os.path.join(BASE_DIR, 'albert_puig_base.json')  # nombre genérico

os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === CARGAR PERFIL BASE ===
def cargar_json():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print("❌ No se encontró el archivo de perfil base.")
        return None

# === GENERAR PDF CON DISEÑO ÉPICO ===
def generar_cv_pdf(datos):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('curriculum_template_es.html')
    html = template.render(datos)

    filename = f"CV_{datos.get('nombre', 'sin_nombre').replace(' ', '_')}.pdf"
    output_path = os.path.join(OUTPUT_DIR, filename)
    HTML(string=html, base_url=BASE_DIR).write_pdf(output_path)

    print(f"✅ PDF generado correctamente: {output_path}")

if __name__ == '__main__':
    datos = cargar_json()
    if datos:
        generar_cv_pdf(datos)
    else:
        print("No se pudo generar el CV porque no hay datos.")
