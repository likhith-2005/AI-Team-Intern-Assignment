# Recommendation Memo

## To: Engineering Leadership

### Subject: Review of Tokenizer and Serving Benchmark Findings

The benchmark results were independently reproduced using the provided starter kit and additional validation experiments were conducted. While the reported measurements are reproducible for the supplied datasets, several conclusions in the original report extend beyond what the available evidence supports.

---

## Tokenizer Findings

The GPT-2 tokenizer generates substantially more tokens for the evaluated Hindi, Kannada, and Telugu corpora than for the English corpus. This indicates that GPT-2 tokenizes these languages less efficiently on the selected datasets.

Additional experiments were performed during the audit:

- Recomputing fertility using **corpus-level aggregation (total tokens ÷ total words)** instead of averaging sentence-level fertility produced noticeably different values, particularly for English and Hindi. This shows that the original implementation can bias corpus-level measurements.
- Removing the **lowercasing** step produced only negligible changes in the reported fertility values, indicating that lowercasing is not a significant source of error for the evaluated corpus.
- Replacing `split(" ")` with `split()` produced identical results because the corpus contains clean whitespace formatting, although `split()` is a more robust implementation.
- Comparing multiple normalization metrics (tokens per word, character, UTF-8 byte, and sentence) demonstrated that different denominators lead to different interpretations of tokenizer efficiency.

These experiments indicate that tokenizer efficiency should not be evaluated using a single metric or a single tokenizer.

---

## Serving Findings

The serving benchmark shows that throughput improves as workload increases up to an optimal operating point. However, throughput does not scale linearly with batch size.

At larger batch sizes:

- KV-cache utilization approaches saturation.
- Scheduler preemption increases.
- Overall throughput declines instead of continuing to increase.

Therefore, production capacity planning should rely on measured operating points rather than linear extrapolation.

---

## Recommendations

Based on the available evidence, the following actions are recommended before making production infrastructure decisions:

1. Benchmark multiple production tokenizers, including multilingual and Indic-specific tokenizers.
2. Evaluate tokenizer efficiency using representative multilingual corpora rather than a single dataset.
3. Compute fertility using corpus-level aggregation instead of averaging sentence-level ratios.
4. Report multiple normalization metrics (tokens per word, character, and UTF-8 byte) to better understand tokenizer behavior.
5. Measure serving throughput across additional prompt lengths, workloads, and hardware configurations.
6. Determine optimal batch sizes using empirical measurements rather than assuming linear throughput scaling.

---

## Conclusion

The available benchmark provides useful preliminary measurements but is insufficient to justify the production recommendations made in the original report.

The additional experiments performed during this audit demonstrate that implementation choices, aggregation methods, and metric selection all influence the reported tokenizer statistics. Production decisions regarding tokenizer selection, routing policies, and serving capacity should therefore be based on broader evaluation using representative workloads, multiple tokenizers, and experimentally validated performance measurements.