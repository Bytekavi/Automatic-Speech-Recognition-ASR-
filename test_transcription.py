import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

# Prevent model download/loading during unit tests.
fake_model = MagicMock()

with patch("faster_whisper.WhisperModel", return_value=fake_model):
    import main


def test_missing_audio():
    assert "Please upload" in main.transcribe_audio(None, "Auto Detect")


def test_successful_transcription():
    segment1 = MagicMock(text=" Hello")
    segment2 = MagicMock(text=" world")
    fake_info = MagicMock(language="en")
    fake_model.transcribe.return_value = ([segment1, segment2], fake_info)

    result = main.transcribe_audio("sample.wav", "Auto Detect")

    assert "Detected language: en" in result
    assert "Hello world" in result


def test_selected_language_is_passed():
    fake_model.transcribe.return_value = ([MagicMock(text=" Vanakkam")], MagicMock(language="ta"))

    main.transcribe_audio("sample.wav", "ta")

    kwargs = fake_model.transcribe.call_args.kwargs
    assert kwargs["language"] == "ta"
