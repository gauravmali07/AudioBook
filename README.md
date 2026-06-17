# 📚 PDF to Audiobook Converter

Convert PDF documents into high-quality MP3 audiobooks using Python, Google Text-to-Speech (gTTS), and PyPDF2.

## 🌟 Overview

PDF to Audiobook Converter is a Python-based automation tool that extracts text from PDF files and converts it into spoken audio. The application supports multi-page PDFs, multiple languages, and custom output filenames, making it useful for students, professionals, and accessibility-focused users.

## 🚀 Features

* 📄 Extract text from PDF documents
* 🎙️ Convert text into natural-sounding speech
* 🌍 Support multiple languages
* 🎧 Generate MP3 audiobook files
* 📚 Process multi-page PDF documents
* 📝 Display extracted word count
* ⚡ User-friendly command-line interface
* 🛡️ Error handling and progress tracking

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| gTTS       | Text-to-Speech Conversion |
| PyPDF2     | PDF Text Extraction       |

## 📂 Project Structure

```text
pdf-to-audiobook-converter/
│
├── Audio-book.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── sample/
│   └── sample.pdf
│
├── output/
│   └── audiobook.mp3
│
└── screenshots/
    └── demo.png
```

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/gauravmali07/pdf-to-audiobook-converter.git
cd pdf-to-audiobook-converter
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python Audio-book.py
```

Follow the prompts:

1. Enter PDF file path
2. Select language code
3. Enter output filename

Example:

```text
📄 Enter PDF file path: sample.pdf
🌐 Enter language code [en]: en
💾 Enter output filename: MyAudioBook
```

Output:

```text
MyAudioBook.mp3
```

## 🌍 Supported Languages

| Language | Code |
| -------- | ---- |
| English  | en   |
| Hindi    | hi   |
| French   | fr   |
| Spanish  | es   |
| German   | de   |

## 📈 Future Enhancements

* GUI using Tkinter
* Streamlit Web Application
* Drag-and-Drop PDF Upload
* Voice Selection Options
* Chapter-wise Audio Generation
* Progress Bar Interface
* Audiobook Metadata Support

## 🎯 Learning Outcomes

This project demonstrates:

* File Handling
* Python Automation
* PDF Processing
* Text-to-Speech Integration
* Error Handling
* User Input Validation

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

## 👨‍💻 Author

**Gaurav Mali**

* GitHub: https://github.com/gauravmali07
* LinkedIn: https://linkedin.com/in/gaurav-mali

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
