#!/usr/bin/env python3
"""
fertility_metrics.py -- tokenizer fertility benchmark with multiple metrics

Computes:
- Tokens per word
- Tokens per character
- Tokens per UTF-8 byte
- Tokens per sentence

Usage:
    python fertility_metrics.py \
        --corpus eng=partA/data/corpus/eng.txt \
        --corpus hin=partA/data/corpus/hin.txt \
        --tokenizer gpt2
"""

import argparse
import random
import unicodedata

random.seed(1337)


def load_tokenizer(spec: str):
    if spec.startswith("hf:"):
        from transformers import AutoTokenizer

        tok = AutoTokenizer.from_pretrained(spec[3:])
        return lambda s: tok.encode(s, add_special_tokens=False)
    else:
        import tiktoken

        enc = tiktoken.get_encoding(spec)
        return enc.encode


def read_lines(path: str):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            line = unicodedata.normalize("NFC", line)
            lines.append(line)
    return lines


def analyze(lines, encode):
    total_tokens = 0
    total_words = 0
    total_chars = 0
    total_bytes = 0
    total_sentences = len(lines)

    for line in lines:
        line = line.lower()

        tokens = encode(line)

        total_tokens += len(tokens)
        total_words += len(line.split())
        total_chars += len(line)
        total_bytes += len(line.encode("utf-8"))

    return {
        "tok_per_word": total_tokens / total_words,
        "tok_per_char": total_tokens / total_chars,
        "tok_per_byte": total_tokens / total_bytes,
        "tok_per_sentence": total_tokens / total_sentences,
    }


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--corpus",
        action="append",
        required=True,
        metavar="LANG=PATH",
        help="language code and path",
    )

    ap.add_argument("--tokenizer", default="gpt2")

    args = ap.parse_args()

    encode = load_tokenizer(args.tokenizer)

    print(f"Tokenizer: {args.tokenizer}")
    print(
        f"{'Lang':<8}"
        f"{'Tok/Word':>12}"
        f"{'Tok/Char':>12}"
        f"{'Tok/Byte':>12}"
        f"{'Tok/Sent':>14}"
    )
    print("-" * 60)

    results = {}

    for spec in args.corpus:
        lang, path = spec.split("=", 1)

        lines = read_lines(path)
        stats = analyze(lines, encode)

        results[lang] = stats

        print(
            f"{lang:<8}"
            f"{stats['tok_per_word']:>12.2f}"
            f"{stats['tok_per_char']:>12.3f}"
            f"{stats['tok_per_byte']:>12.3f}"
            f"{stats['tok_per_sentence']:>14.2f}"
        )

    if len(results) >= 2:
        langs = list(results)
        base = langs[0]

        print()

        for lang in langs[1:]:
            ratio = (
                results[lang]["tok_per_word"]
                / results[base]["tok_per_word"]
            )

            print(
                f"{lang} is {ratio:.2f}x the token/word fertility of {base} "
                f"({'worse' if ratio > 1 else 'better'} tokenization)"
            )


if __name__ == "__main__":
    main()