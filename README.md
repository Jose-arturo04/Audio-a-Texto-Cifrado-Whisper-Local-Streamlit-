# 🎤 Proyecto Audio a Texto + Cifrado (Whisper Local + Streamlit)

Este proyecto convierte archivos de audio a texto usando **Whisper local** y permite **cifrar y descifrar texto** mediante **Fernet**.  
Funciona con **Streamlit**, **FFmpeg**, **Whisper** y **Python** de forma local sin depender de APIs externas.

---

## 🚀 Funcionalidades

| Función | Descripción |
|--------|-------------|
| 🔊 Subir audio | MP3, WAV, OGG, M4A |
| 🎙 Convertir a WAV | Pydub + FFmpeg |
| 🧠 Transcripción IA | Whisper local (modelo base) |
| 🔐 Cifrado de texto | Algoritmo Fernet seguro |
| 🔓 Descifrado | Recupera el texto original |

---

## 📁 Requisitos

- Python 3.10+
- FFmpeg instalado y agregado al PATH
- Dependencias instaladas

---

## 🔧 Instalación inicial (solo primera vez)

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install streamlit pydub cryptography openai-whisper torch

---

## 🔧 Instalación inicial (solo primera vez)
.\.venv\Scripts\activate
python -m streamlit run app.py

