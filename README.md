# 🎙️ ASR Tool — Automatic Speech Recognition

A simple, working **Automatic Speech Recognition (ASR)** web application built with **Python, Gradio, and Faster-Whisper**.

The tool accepts an audio file or microphone recording and converts speech into text. It can automatically detect the spoken language or use a selected language.

## Features

- 🎤 Record audio from the microphone
- 📁 Upload an audio file
- 📝 Convert speech to text using Faster-Whisper
- 🌐 Automatic language detection
- 🇬🇧 English, 🇮🇳 Tamil, Hindi, Telugu, Malayalam and Kannada language selection
- 🧪 Unit tests included
- 💻 Simple browser-based interface
- ⚙️ Configurable Whisper model and compute settings

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Programming language |
| Faster-Whisper | Speech recognition / ASR |
| Gradio | Web interface |
| CTranslate2 | Efficient Whisper inference backend |
| Pytest | Testing |
| Git/GitHub | Version control and project hosting |

## Project Structure

```text
asr-tool/
├── app/
│   └── main.py
├── tests/
│   └── test_transcription.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10 or newer
- Internet connection for the first model download
- Microphone (optional; only needed for recording)
- Windows, Linux or macOS

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/asr-tool.git
cd asr-tool
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the ASR Tool

```bash
python app/main.py
```

Gradio will display a local URL such as:

```text
http://127.0.0.1:7862/
```

Open that URL in your browser.

### First run

The default `base` Whisper model is downloaded automatically the first time the application starts. The first startup can therefore take longer than later starts.

## How to Use

1. Start the application.
2. Open the Gradio URL in your browser.
3. Click **Record** to use your microphone, or upload an audio file.
4. Select a language or leave **Auto Detect** selected.
5. Submit the audio.
6. Read the generated transcription.

## Model Configuration

The default model is `base`.

You can change the model using an environment variable.

Windows PowerShell:

```powershell
$env:WHISPER_MODEL="small"
python app/main.py
```

macOS/Linux:

```bash
WHISPER_MODEL=small python app/main.py
```

Supported Faster-Whisper model sizes include `tiny`, `base`, `small`, `medium`, and `large-v3`. Larger models generally improve accuracy but require more memory and processing time.

For CPU:

```text
WHISPER_DEVICE=cpu
WHISPER_COMPUTE_TYPE=int8
```

For a compatible NVIDIA GPU, you can configure:

```text
WHISPER_DEVICE=cuda
WHISPER_COMPUTE_TYPE=float16
```

The exact GPU setup depends on the installed CUDA/CTranslate2 environment.

## Testing

Run the automated tests from the project root:

```bash
pytest -q
```

The tests validate:

- Missing audio handling
- Successful transcription output
- Correct language parameter handling

The tests mock the Whisper model, so they do not download a model.

## GitHub Upload

After creating a GitHub repository named `asr-tool`:

```bash
git init
git add .
git commit -m "Initial ASR tool implementation"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/asr-tool.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Suggested GitHub Repository Description

> A Python-based Automatic Speech Recognition tool using Faster-Whisper and Gradio for real-time microphone/audio-file speech-to-text transcription.

## Testing Checklist

- [x] ASR implementation
- [x] Browser UI
- [x] Microphone input
- [x] Audio file upload
- [x] Automatic language detection
- [x] Language selection
- [x] Unit tests
- [x] requirements.txt
- [x] README.md
- [x] GitHub upload instructions

## Limitations

- CPU transcription is slower than GPU transcription.
- Accuracy depends on audio quality, accent, background noise and model size.
- The first model startup requires downloading the selected Whisper model.
- This project is intended as an academic/project implementation rather than a production speech service.

## Future Enhancements

- Timestamped subtitles
- Download transcription as TXT/SRT
- Speaker diarization
- Translation
- Noise reduction
- REST API
- Docker deployment
- Cloud deployment .
