# Audio-a-Texto-Cifrado-Whisper-Local-Streamlit-
Este proyecto convierte archivos de audio a texto usando Whisper local y permite cifrar y descifrar dicho texto usando Fernet. Funciona con Streamlit, FFmpeg, Whisper y Python.

# Requisitos
Python 3.10 o superior
FFmpeg instalado en el sistema
Dependencias instaladas con pip

# Instalación inicial (solo la primera vez)
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install streamlit pydub cryptography openai-whisper torch

# Uso diario (para ejecutar el proyecto) 
.\.venv\Scripts\activate
python -m streamlit run app.py
