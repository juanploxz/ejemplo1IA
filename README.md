# Neon Dash

Un juego arcade sencillo inspirado en *Geometry Dash*, creado con Python,
Streamlit y un componente HTML5 Canvas. La versión visible en la cabecera debe
ser **v2.1**; esto permite confirmar que Streamlit desplegó el recurso actualizado.
Streamlit y un componente HTML5 Canvas.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Usa la barra espaciadora, la flecha arriba o un toque sobre el juego para
controlar el personaje. El nivel se genera de forma procedural y combina cinco
modos (`cube`, `ship`, `ball`, `wave` y `UFO`), portales de velocidad y gravedad,
orbes de impulso y estructuras cada vez más precisas. El récord se conserva en
el almacenamiento local del navegador.

## Pruebas

Las validaciones estructurales no necesitan instalar Streamlit ni abrir un
navegador:

```bash
python -m unittest discover -s tests -v
```
Usa la barra espaciadora, la flecha arriba o un toque/clic sobre el juego para
saltar los obstáculos. El récord se conserva en el almacenamiento local del
navegador.
