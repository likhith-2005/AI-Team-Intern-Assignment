# NOTEBOOK

## Day 1 – Part A1: Corpus Construction

### Goal
Build a multilingual evaluation corpus for tokenizer analysis.

### Initial Attempt
Attempted to use the FLORES-200 dataset through the Hugging Face `datasets` library.

### Observation
The dataset was gated and required authentication, preventing reproducible downloads without additional setup.

### Revision
Switched to the OPUS-100 multilingual parallel corpus, which is publicly accessible and reproducible.

### Experiment
- Downloaded 1000 English–Hindi sentence pairs.
- Downloaded 1000 English–Kannada sentence pairs.
- Downloaded 1000 English–Telugu sentence pairs.

### Result
Successfully created a multilingual corpus containing:
- English: 1000 sentences
- Hindi: 1000 sentences
- Kannada: 1000 sentences
- Telugu: 1000 sentences

### Next Step
Audit `fertility.py` and evaluate the tokenizer metrics using the new corpus.