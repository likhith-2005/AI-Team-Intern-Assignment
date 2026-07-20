# AI Team Intern Assignment

This repository contains my solutions for the AI Team Intern Assignment.

## Repository Structure

```
partA/
partB/
partC/
starter_kit/
AI_USAGE.md
NOTEBOOK.md
requirements.txt
```

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd AI-Team-Intern-Assignment
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Part A

Download the corpus:

```bash
python partA/scripts/download_corpus.py
```

Run fertility metrics with GPT-2:

```bash
python partA/scripts/fertility_metrics.py --corpus en=partA/data/corpus/eng.txt --corpus hi=partA/data/corpus/hin.txt --corpus kn=partA/data/corpus/kan.txt --corpus te=partA/data/corpus/tel.txt --tokenizer gpt2
```

Run fertility metrics with XLM-R:

```bash
python partA/scripts/fertility_metrics.py --corpus en=partA/data/corpus/eng.txt --corpus hi=partA/data/corpus/hin.txt --corpus kn=partA/data/corpus/kan.txt --corpus te=partA/data/corpus/tel.txt --tokenizer hf:xlm-roberta-base
```

## Notes

- Python 3.10+
- Install all required dependencies using `requirements.txt`.