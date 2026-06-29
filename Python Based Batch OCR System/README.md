# Batch OCR System (Simulation)

A lightweight Python-based automated system designed to batch process image files, simulate image preprocessing (such as grayscale transformation, noise reduction, and thresholding), mimic optical character recognition (OCR), and export the extracted results into organized text files.

## Features

- **Automated Directory Setup:** Automatically checks and creates missing input/output directories safely on any Operating System (Windows, macOS, Linux).
- **Safe Path & Extension Handling:** Robust file processing that supports multi-dot filenames (e.g., `image.test.png`) and case-insensitive extensions (`.PNG`, `.jpg`, `.JPEG`).
- **Interactive Prompts:** Clear log messages to guide users if the image folder is missing or currently empty.

## How It Works

1. The script initializes and ensures an input folder (`images`) and an output folder (`outputtext`) exist.
2. It scans the input folder for valid image formats (`.jpg`, `.jpeg`, `.png`).
3. Each image goes through a simulated preprocessing pipeline.
4. Simulated text is extracted and saved into a corresponding `.txt` file inside the output folder.

## Getting Started

### Prerequisites

You only need Python 3.x installed on your system. This project uses standard built-in Python libraries (`os`), so no external dependencies are required.

### Installation & Running

1. Clone or download this repository to your local machine.
2. Run the script using your terminal or an IDE (like Jupyter Notebook):
   ```bash
   python script_name.py
