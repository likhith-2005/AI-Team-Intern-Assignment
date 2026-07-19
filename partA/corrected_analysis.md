# Corrected Analysis

## Executive Summary

The results reported in `REPORT_v0.md` are reproducible; however, several conclusions drawn from those results are either unsupported or stronger than the available evidence justifies.

The tokenizer benchmark confirms that the GPT-2 tokenizer produces substantially more tokens for the provided Hindi corpus than for the provided English corpus. However, this observation alone does not prove that serving Hindi will always cost approximately six times more, nor does it establish that the language script itself is the root cause.

Similarly, the serving benchmark demonstrates that throughput improves only up to a certain operating point. The benchmark does not support the claim that throughput scales linearly with batch size or that longer prompts always improve serving efficiency.

The corrected conclusions below distinguish between direct measurements and unsupported extrapolations.


---

# 1. Tokenizer Analysis

## Claim 1
**Original claim:**
> Hindi fertility is 5.89× worse than English. Serving Hindi will cost roughly 6× more per request.

### Evidence

Running `fertility.py` with the provided GPT-2 tokenizer reproduces the reported measurements:

| Language | Fertility (tok/word) | Tokens/Character |
|----------|----------------------:|-----------------:|
| English | 1.27 | 0.226 |
| Hindi | 7.45 | 1.579 |

The reported ratio (7.45 / 1.27 ≈ 5.89) is correct for the supplied sample corpus.

### Analysis

The benchmark demonstrates that the GPT-2 tokenizer produces substantially more tokens for the provided Hindi sample than for the provided English sample.

However, the benchmark alone does **not** justify concluding that serving every Hindi request will cost approximately six times more. Actual serving cost depends on multiple factors, including prompt length, generated output length, batching behaviour, cache reuse, and the tokenizer used in production.

### Corrected Conclusion

The experiment shows significantly higher tokenization for the supplied Hindi corpus using the GPT-2 tokenizer. Additional measurements across larger corpora and production tokenizers are required before estimating serving costs.



---

## Claim 2

**Original claim:**
> The tok/char metric confirms the per-word fertility result.

### Evidence

Both metrics indicate that the Hindi sample generates more tokens than the English sample.

However, the two metrics measure different properties.

- Tokens per word measures tokenization relative to words.
- Tokens per character measures tokenization relative to characters.

### Analysis

The two metrics are related but they are **not independent validation** of each other. Since both metrics are computed from the same tokenization output, agreement between them does not independently confirm the conclusion.

### Corrected Conclusion

The two metrics consistently indicate higher tokenization for the provided Hindi sample, but they should be interpreted as complementary measurements rather than independent confirmation.



---

## Claim 3

**Original claim:**
> Root cause: Hindi simply has more Unicode characters per word, so any tokenizer will struggle. This is a property of the script, not the tokenizer.

### Evidence

The benchmark evaluates only a single tokenizer (GPT-2) on one English sample and one Hindi sample.

No comparison was performed using multilingual or Indic-specialized tokenizers.

### Analysis

The experiment does not isolate the cause of the observed difference.

Several factors could contribute to the higher fertility:

- GPT-2 was primarily trained on English-centric data.
- The tokenizer vocabulary may not efficiently represent Hindi text.
- The selected corpus may have different linguistic characteristics.
- Different tokenizers can produce significantly different tokenization behaviour for the same language.

Therefore, the benchmark cannot conclude that the script itself is responsible.

### Corrected Conclusion

The experiment demonstrates higher fertility for the provided Hindi corpus using the GPT-2 tokenizer. Additional experiments with multilingual and Indic-specific tokenizers are required before attributing the difference to the writing system.



---

## Recommendation Review

**Original recommendation:**
> Route all Indic traffic to a separate tokenizer/model and budget 6× serving cost. No further measurement is needed.

### Analysis

The recommendation is stronger than the available evidence.

The benchmark uses:
- one tokenizer,
- one English corpus,
- one Hindi corpus,
- and a limited experimental setup.

Before making production routing decisions, additional experiments should compare multiple tokenizers across larger and more representative datasets.

### Corrected Recommendation

The current benchmark indicates that GPT-2 tokenizes the provided Hindi sample less efficiently than the English sample. Before changing production infrastructure, the result should be validated using production workloads, representative multilingual datasets, and candidate production tokenizers.



---

# 2. Serving Benchmark Analysis

## Claim 1

**Original claim:**
> Longer prompts clearly give better GPU utilization.

### Evidence

For the provided benchmark:

| Scenario | Batch | Throughput (tok/s) |
|----------|------:|-------------------:|
| Short Prompt (512) | 16 | 883.2 |
| Long Prompt (3584) | 16 | 1311.4 |

At batch size 16, the long-prompt workload achieves higher throughput than the short-prompt workload.

### Analysis

This observation is valid **for the tested workload**.

However, the benchmark compares workloads that differ in both prompt length and generation length (512/256 vs. 3584/512). Therefore, it does not isolate prompt length as the only changing factor.

The benchmark also evaluates only a limited set of operating points on one GPU configuration.

### Corrected Conclusion

The benchmark indicates higher throughput for the tested long-prompt workload at batch size 16, but it does not prove that longer prompts always improve GPU utilization.



---

## Claim 2

**Original claim:**
> Throughput scales linearly with batch size. Batch 48 should achieve approximately 3200 tok/s.

### Evidence

Observed throughput for the long-prompt benchmark:

| Batch Size | Throughput (tok/s) |
|-----------:|-------------------:|
| 4 | 565.4 |
| 8 | 902.6 |
| 16 | 1311.4 |
| 24 | 1607.4 |
| 32 | 1384.0 |
| 48 | 1298.5 |

The highest measured throughput occurs at batch size 24.

Beyond this point, throughput decreases rather than increasing.

### Additional Evidence

Resource-related metrics also change significantly:

| Batch | Preempted Sequences | KV Cache Utilization |
|------:|--------------------:|---------------------:|
| 24 | 0 | 0.93 |
| 32 | 7 | 0.97 |
| 48 | 23 | 0.97 |

As the KV cache approaches full utilization, scheduler preemption increases and throughput declines.

### Analysis

The benchmark does not support linear scaling.

Instead, it demonstrates diminishing returns followed by performance degradation after the optimal operating point.

### Corrected Conclusion

Capacity planning should rely on measured throughput rather than linear extrapolation. The available benchmark suggests that throughput peaks near batch size 24 for this hardware configuration.



---

## Recommendation Review

**Original recommendation:**
> Encourage clients to pack more context per request. Assume approximately 1600 tok/s per L4 and scale linearly with batch size.

### Analysis

The recommendation extends beyond the available evidence.

Although higher throughput is observed for some larger workloads, throughput does not continue increasing as batch size grows. The benchmark shows resource saturation, increased scheduler preemption, and reduced throughput at larger batch sizes.

### Corrected Recommendation

Capacity planning should be based on measured operating points rather than linear extrapolation. Additional benchmarking across different workloads, prompt lengths, and hardware configurations should be completed before defining production scaling policies.