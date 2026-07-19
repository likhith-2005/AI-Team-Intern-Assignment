# Corpus Notes

## Dataset
- Dataset: OPUS-100 (Helsinki-NLP)
- Source: Hugging Face Datasets
- Languages:
  - English (en)
  - Hindi (hi)
  - Kannada (kn)
  - Telugu (te)

## Corpus Size
- 1000 parallel sentence pairs were sampled for each English-language pair.

## Domain
The OPUS-100 corpus is a multilingual parallel corpus compiled from multiple publicly available translation datasets. It covers a variety of domains rather than a single specialized topic.

## Preprocessing
- Downloaded using the Hugging Face `datasets` library.
- No additional text normalization was applied.
- UTF-8 encoding was preserved.
- Sentences were stored one per line.

## Limitations
This corpus is suitable for comparing tokenizer behavior across multiple languages because the sentences are parallel translations. However, it is limited to only 1000 sentence pairs per language and may not fully represent real-world production traffic. Since the corpus is drawn from multiple domains, the measured tokenizer statistics may differ for conversational chat, technical documents, or code-heavy workloads.