# Part C – Decision Memo

## Recommendation

I recommend **Option (b): a small (≤1B parameter) inference-time rewriter model**. The main assistant model will first generate a response, and the rewriter will then convert it into a more natural, casual conversational style for supported Indian languages.

This approach requires significantly less effort than retraining the main model while providing more consistent improvements than prompt engineering alone.

---

## Assumptions

- One NVIDIA A100 80GB GPU is available for two weeks.
- One native-speaker reviewer is available for Hindi and Kannada for 10 hours per week.
- Launch review is scheduled in three weeks.
- No external API budget is available.
- The existing assistant already produces factually correct responses; only the conversational tone needs improvement.

---

## Back-of-the-envelope calculations

### Training data

Generate approximately **100,000 synthetic formal-to-casual response pairs**.

Assuming an average response length of **100 tokens**, the dataset contains roughly:

100,000 × 100 = **10 million tokens**

---

### Reviewer effort

Reviewer availability:

10 hours/week × 2 weeks = **20 hours**

If a reviewer validates approximately **100 examples per hour**:

20 × 100 = **2,000 reviewed examples**

These reviewed examples can be used as a high-quality validation set.

---

### Serving cost

A ≤1B parameter rewriter is much smaller than the main model.

Expected overhead:

- Approximately 10–20% additional inference latency.
- Much lower GPU memory usage than retraining or serving another large model.
- Easy to deploy as a second inference stage.

---

## Success metric

The rewriter should satisfy both conditions:

- At least **90%** of reviewed responses are judged by native speakers as sounding more natural than the original.
- The additional inference latency remains below **20%** compared to the current system.

---

## Kill criterion

After the first week of evaluation, if fewer than **80%** of reviewed responses are preferred over the original responses, or if the additional latency consistently exceeds **20%**, I would stop investing in the rewriter approach and instead reconsider prompt engineering or limited supervised fine-tuning.

---

## Day 1 experiment

Generate approximately **1,000 synthetic formal-to-casual response pairs** for Hindi and Kannada.

Train a small prototype rewriter on this dataset and evaluate it using a manually reviewed validation set. The goal is to determine whether conversational quality improves while maintaining factual correctness and acceptable latency before investing additional engineering effort.