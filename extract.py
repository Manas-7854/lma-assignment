import json
import pathlib from Path

import pymupdf

def extract_pdf(pdf_path):
    pages = []

    with pymupdf.open(pdf_path) as doc:
