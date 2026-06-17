"""
PDF TO AUDIOBOOK CONVERTER
Author: Gaurav Mali

Requirements:
pip install gtts PyPDF2
"""

from gtts import gTTS
from PyPDF2 import PdfReader
import os


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""

    try:
        reader = PdfReader(pdf_path)

        text_list = []

        total_pages = len(reader.pages)

        print(f"\n📄 Total Pages Found: {total_pages}\n")

        for i, page in enumerate(reader.pages):
            try:
                print(f"📖 Reading Page {i + 1}/{total_pages}")

                text = page.extract_text()

                if text:
                    text_list.append(text)

            except Exception as e:
                print(f"⚠ Error reading page {i + 1}: {e}")

        return " ".join(text_list)

    except Exception as e:
        print(f"\n❌ Error opening PDF: {e}")
        return None


def convert_to_audio(text, language, output_file):
    """Convert text into speech."""

    try:
        print("\n🎙 Converting text to speech...")

        audio = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        audio.save(output_file)

        print(f"\n✅ Audiobook created successfully!")
        print(f"🎧 Saved as: {output_file}")

    except Exception as e:
        print(f"\n❌ Audio generation failed: {e}")


def main():
    print("=" * 50)
    print("📚 PDF TO AUDIOBOOK CONVERTER")
    print("=" * 50)

    pdf_path = input("\n📄 Enter PDF file path: ").strip()

    if not os.path.exists(pdf_path):
        print("\n❌ File not found!")
        return

    print("\nAvailable Languages:")
    print("en - English")
    print("hi - Hindi")
    print("fr - French")
    print("es - Spanish")
    print("de - German")

    language = input("\n🌐 Enter language code [en]: ").strip()

    if language == "":
        language = "en"

    output_name = input(
        "\n💾 Enter output filename (without .mp3): "
    ).strip()

    if output_name == "":
        output_name = "AudioBook"

    output_file = f"{output_name}.mp3"

    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("\n❌ No text found in PDF!")
        return

    word_count = len(text.split())

    print(f"\n📝 Total Words Extracted: {word_count}")

    convert_to_audio(
        text=text,
        language=language,
        output_file=output_file
    )


if __name__ == "__main__":
    main()