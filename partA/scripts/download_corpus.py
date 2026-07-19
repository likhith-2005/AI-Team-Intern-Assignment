from pathlib import Path
from datasets import load_dataset

# Output directory
output_dir = Path(__file__).resolve().parent.parent / "data" / "corpus"
output_dir.mkdir(parents=True, exist_ok=True)

languages = {
    "hi": "hin",
    "kn": "kan",
    "te": "tel",
}

english_lines = []

for lang_code, short_name in languages.items():
    print(f"Downloading en-{lang_code}...")

    ds = load_dataset(
        "Helsinki-NLP/opus-100",
        f"en-{lang_code}",
        split="train[:1000]"
    )

    with open(output_dir / f"{short_name}.txt", "w", encoding="utf-8") as f_lang:
        for i, row in enumerate(ds):
            if lang_code == "hi":
                english_lines.append(row["translation"]["en"])
            f_lang.write(row["translation"][lang_code] + "\n")

with open(output_dir / "eng.txt", "w", encoding="utf-8") as f_en:
    for line in english_lines:
        f_en.write(line + "\n")

print("Corpus downloaded successfully!")