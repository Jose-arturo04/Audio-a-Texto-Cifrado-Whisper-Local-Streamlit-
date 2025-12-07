import os
import tempfile

import streamlit as st
from pydub import AudioSegment
from pydub.utils import which
import whisper
from cryptography.fernet import Fernet

# Hacer que pydub use ffmpeg del sistema
AudioSegment.converter = which("ffmpeg")

st.set_page_config(page_title="Whisper Local + Cifrado", page_icon="🎤")
st.title("Conversión de Audio (Whisper Local) + Cifrado")

# ---------- Cargar modelo Whisper una sola vez ----------
@st.cache_resource
def load_model():
    return whisper.load_model("base")  # puedes cambiar a "small" si quieres más rapidez

# Intentar cargar el modelo y mostrar mensaje si falla
with st.spinner("Cargando modelo de Whisper (solo la primera vez)..."):
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error cargando el modelo Whisper: {e}")
        st.stop()

# ---------- Funciones auxiliares ----------
def convert_to_wav(uploaded_file):
    # Guardar archivo subido en un temporal
    suf = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suf) as tmp:
        tmp.write(uploaded_file.getbuffer())
        in_path = tmp.name

    # Convertir a WAV con pydub + ffmpeg
    audio = AudioSegment.from_file(in_path)
    out = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(out.name, format="wav")
    return out.name

def transcribe(path):
    result = model.transcribe(path, language="es")
    return result["text"]

# ---------- Estado de sesión ----------
if "texto" not in st.session_state:
    st.session_state["texto"] = ""
if "cifrado" not in st.session_state:
    st.session_state["cifrado"] = b""
if "clave" not in st.session_state:
    st.session_state["clave"] = Fernet.generate_key()

# ---------- Clave de cifrado ----------
st.subheader("Clave de Cifrado (Fernet)")
st.code(st.session_state["clave"].decode())

# ---------- Subida de audio ----------
audio = st.file_uploader("Subir archivo de audio", type=["mp3", "wav", "m4a", "ogg"])

if audio is not None:
    st.audio(audio)
    if st.button("Convertir audio a texto"):
        with st.spinner("Transcribiendo audio, espera un momento..."):
            wav_path = convert_to_wav(audio)
            st.session_state["texto"] = transcribe(wav_path)
        st.success("Transcripción completada.")

# ---------- Texto ----------
st.subheader("Texto")
st.session_state["texto"] = st.text_area(
    "Texto (puedes editarlo):",
    st.session_state["texto"],
    height=200
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Cifrar texto"):
        if st.session_state["texto"].strip():
            f = Fernet(st.session_state["clave"])
            st.session_state["cifrado"] = f.encrypt(
                st.session_state["texto"].encode("utf-8")
            )
            st.success("Texto cifrado.")
        else:
            st.warning("No hay texto para cifrar.")

with col2:
    if st.button("Descifrar texto"):
        if st.session_state["cifrado"]:
            try:
                f = Fernet(st.session_state["clave"])
                st.session_state["texto"] = f.decrypt(
                    st.session_state["cifrado"]
                ).decode("utf-8")
                st.success("Texto descifrado.")
            except Exception as e:
                st.error(f"No se pudo descifrar: {e}")
        else:
            st.warning("No hay texto cifrado para descifrar.")

# ---------- Mostrar texto cifrado ----------
st.subheader("Texto Cifrado (bytes)")
if st.session_state["cifrado"]:
    st.code(st.session_state["cifrado"])
else:
    st.info("Aún no has cifrado nada.")
