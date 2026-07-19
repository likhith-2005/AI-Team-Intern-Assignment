# Recommendation Memo

## To: Engineering Leadership

### Subject: Review of Tokenizer and Serving Benchmark Findings

The benchmark results were independently reproduced using the provided starter kit. While the reported measurements are accurate for the supplied datasets, several conclusions in the original report extend beyond what the available evidence supports.

### Tokenizer Findings

The GPT-2 tokenizer generates substantially more tokens for the provided Hindi corpus than for the English corpus. However, this observation is limited to the tested corpus and tokenizer. The experiment does not demonstrate that all Hindi workloads incur approximately six times the serving cost, nor does it establish that the writing system is the primary cause of the observed difference.

Before making production decisions, additional evaluation should be performed using representative production data together with multilingual and Indic-specific tokenizers.

### Serving Findings

The benchmark shows that throughput improves as workload increases up to an optimal operating point. However, throughput does not scale linearly with batch size. At larger batches, throughput declines while KV-cache utilization approaches saturation and scheduler preemption increases.

Therefore, production capacity planning should rely on measured operating points rather than linear extrapolation.

### Recommended Next Steps

1. Benchmark multiple production tokenizers using representative multilingual datasets.
2. Evaluate throughput across additional prompt lengths and request mixes.
3. Determine the optimal batch size from empirical measurements instead of assuming linear scaling.
4. Validate all conclusions before making production infrastructure decisions.

## Conclusion

The available benchmark provides useful preliminary measurements but is insufficient to justify the production recommendations made in the original report. Additional experiments should be completed before modifying tokenizer selection or serving strategy.