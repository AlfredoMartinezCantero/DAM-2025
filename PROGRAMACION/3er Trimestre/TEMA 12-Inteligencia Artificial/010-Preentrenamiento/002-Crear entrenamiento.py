#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

INPUT_TXT = "input.txt"
OUTPUT_JSONL = "output.jsonl"


def main():
    question = None
    answer_lines = []

    with open(INPUT_TXT, "r", encoding="utf-8") as f, \
         open(OUTPUT_JSONL, "w", encoding="utf-8") as out:

        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("Q:"):
                # Save previous Q/A if exists
                if question and answer_lines:
                    write_pair(out, question, answer_lines)

                question = line[2:].strip()
                answer_lines = []

            elif line.startswith("A:"):
                answer_lines.append(line[2:].strip())

            else:
                # Multiline answer support
                answer_lines.append(line)

        # Final pair
        if question and answer_lines:
            write_pair(out, question, answer_lines)


def write_pair(out, question, answer_lines):
    record = {
        "question": question,
        "answer": " ".join(answer_lines).strip()
    }
    out.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
