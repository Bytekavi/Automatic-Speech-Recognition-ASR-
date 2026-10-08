import gradio as gr
from faster_whisper import WhisperModel
import os
import tempfile

MODEL_SIZE = os.getenv("WHISPER_MODEL", "base")
DEVICE = os.getenv("WHISPER_DEVICE", "cpu")
COMPUTE_TYPE = os.getenv("WHISPER_COMPUTE_TYPE", "int8")

print(f"Loading Whisper model: {MODEL_SIZE} ({DEVICE}, {COMPUTE_TYPE})")
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

def transcribe_audio(audio_path, language):
    """Transcribe an uploaded/recorded audio file."""
    if not audio_path:
        return "Please upload or record an audio file."

    lang = None if language == "Auto Detect" else language
    try:
        segments, info = model.transcribe(
            audio_path,
            language=lang,
            beam_size=5,
            vad_filter=True,
        )

        text_parts = []
        for segment in segments:
            text_parts.append(segment.text.strip())

        text = " ".join(text_parts).strip()
        detected = info.language if info.language else "unknown"

        if not text:
            return f"No speech was detected. Detected language: {detected}"

        return f"Detected language: {detected}\n\n{text}"
    except Exception as exc:
        return f"Transcription error: {exc}"

demo = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(
            sources=["upload", "microphone"],
            type="filepath",
            label="Speak or upload audio",
        ),
        gr.Dropdown(
            choices=["Auto Detect", "en", "ta", "hi", "te", "ml", "kn"],
            value="Auto Detect",
            label="Language",
        ),
    ],
    outputs=gr.Textbox(
        label="Transcription",
        lines=10,
        placeholder="Your speech-to-text result will appear here...",
    ),
    title="🎙️ ASR Tool — Automatic Speech Recognition",
    description=(
        "Upload an audio file or record from your microphone. "
        "The application uses Faster-Whisper for speech-to-text."
    ),
    examples=[],
)

if __name__ == "__main__":
    demo.launch()
