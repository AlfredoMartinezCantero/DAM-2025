#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json
import textwrap

MODEL = "qwen2.5:3b-instruct"
INPUT_TXT = "convertido.txt"
OUTPUT_JSONL = "entrenamiento.jsonl"
CHUNK_SIZE = 1200  # characters


def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()


def main():
    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = textwrap.wrap(text, CHUNK_SIZE)

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        for chunk in chunks:
            prompt = f"""
You are an expert teacher.
Read the following text and generate ONE high-quality question
and its correct answer.

Return STRICT JSON ONLY in this format:
{{"question":"...","answer":"..."}}

Text:
\"\"\"
{chunk}
\"\"\"
"""

            response = call_ollama(prompt)

            try:
                data = json.loads(response)
                out.write(json.dumps(data, ensure_ascii=False) + "\n")
            except json.JSONDecodeError:
                print("⚠️ Skipped invalid model output")


if __name__ == "__main__":
    main()
