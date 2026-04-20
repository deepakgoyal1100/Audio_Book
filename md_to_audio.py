import asyncio
import edge_tts
import os

# Configuration
INPUT_FILE = "book.md"
OUTPUT_FILE = "output.mp3"
VOICE = "en-US-GuyNeural"  # Professional male voice

async def generate_audiobook():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found!")
        return

    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Simple cleanup: Remove markdown headers and extra whitespace
    clean_text = text.replace("#", "").strip()

    print(f"Synthesizing audio with voice: {VOICE}...")
    communicate = edge_tts.Communicate(clean_text, VOICE)
    
    await communicate.save(OUTPUT_FILE)
    print(f"Audiobook generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audiobook())
