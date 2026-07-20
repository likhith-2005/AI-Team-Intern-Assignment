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

---

## Day 2 – Part A2 & A3: Fertility Analysis

### Goal
Evaluate tokenizer fertility across the four languages.

### Experiments
- Audited the provided `fertility.py`.
- Compared average-per-sentence vs corpus-level aggregation.
- Evaluated GPT-2 and XLM-R tokenizers.
- Computed:
  - Tokens per word
  - Tokens per character
  - Tokens per byte
  - Tokens per sentence

### Result
Observed that GPT-2 produces much higher fertility for Indic languages than English, while XLM-R significantly reduces this gap.

---

## Day 3 – Part A4

### Goal
Summarize findings and recommend suitable tokenization metrics.

### Result
Recommended monitoring average input tokens per request by language and discussed implications for multilingual LLM serving.

---

## Day 4 – Part B

### Goal
Analyze KV-cache memory usage, batching behaviour, throughput, and scheduler preemption.

### Result
Estimated practical concurrency limits, explained throughput degradation at larger batch sizes, and proposed scheduler preemption as the primary monitoring metric.

---

## Day 5 – Part C

### Goal
Recommend an efficient deployment strategy for multilingual query rewriting.

### Result
Recommended using a small inference-time rewriting model based on the provided constraints and discussed expected cost and deployment considerations.

---

## Environment

- Python 3.10
- Hugging Face Datasets
- Transformers
- SentencePiece
- tiktoken