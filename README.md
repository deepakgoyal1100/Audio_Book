# Local Audiobook Maker

A lightweight, high-performance tool to convert your Markdown books into high-quality MP3 audiobooks using Microsoft Edge's neural TTS.

## 🚀 Stack
- **Python**: Core logic and script execution.
- **Edge-TTS**: High-quality, fast, and free neural text-to-speech.
- **Markdown**: Easy-to-write source format for books.

## 🛠️ Installation
1. Ensure you have Python installed.
2. Install the required dependency:
   ```bash
   pip install edge-tts
   ```

## 📖 How to Use
1. Add your book content to `book.md`.
2. Run the synthesis script:
   ```bash
   python md_to_audio.py
   ```
3. Your audiobook will be generated as `output.mp3`.

## 🧪 Testing
- Verify that `output.mp3` is created in the root directory.
- Play the file using any media player to check audio quality.

## 🎯 Use Cases
- Converting long articles or personal notes into audio for commuting.
- Creating drafts of self-published books to listen for flow and rhythm.
- Accessibility for people with visual impairments or reading difficulties.

## 🔮 Future Additions
- Multi-voice support for different characters.
- Automatic chapter splitting based on Markdown headers.
- Support for custom local TTS models (Fish Audio S2, etc.).
