# Running ensemble extraction against Qwen3.5-122B (TP=2 Ray cluster)

Use this when you want higher-quality extractions and have time to spare.
The 122B run produces better facts but takes roughly 2× longer per chapter than the 80B MoE setup.

## Prerequisites: spin up the Ray cluster

From the **workstation** (not a Spark), after tearing down the single-box containers:

```bash
ssh spark  'docker rm -f vllm-chat'
ssh spark2 'docker rm -f vllm-chat'
PROFILE=qwen35 ./spin-up-vllm-2box-rdma.sh
```

This creates the `vllm-2box` container on both boxes. spark1 becomes Ray HEAD
(serves `spark1:8001`); spark2 is a worker with no independent endpoint.
Full perf record: `~/src/dgx/qwen35-122b-2box-observations.md`.

**Model id served:** `Qwen/Qwen3.5-122B-A10B-FP8`
**Context:** 256K (`--max-model-len 262144`), TP=2, RoCE/IB cable active.

spark2's `vllm-embed` (port 8000, `Qwen/Qwen3-Embedding-0.6B`) keeps running
throughout — it is unaffected by the Ray cluster spin-up.

## Changes to run.py

```python
# Single endpoint only — spark2 is a Ray worker, not an independent client endpoint
ENDPOINTS = "http://192.168.1.147:8001/v1"
MODEL     = "Qwen/Qwen3.5-122B-A10B-FP8"

# Embed: spark2 vllm-embed (unchanged)
EMBED_ENDPOINT = "http://192.168.1.121:8000"
EMBED_MODEL    = "Qwen/Qwen3-Embedding-0.6B"

# Reduce chapter concurrency — single endpoint, denser model, slower tokens
CHAPTER_PARALLEL = 2
```

In the `subprocess.run` call, change `--chunk-parallel` from `4` to `3` to
avoid overloading the single endpoint's queue:

```python
"--chunk-parallel", "3",
```

## Critical: disable the unit timeout

The 122B model generates 10K–30K thinking tokens before emitting JSON.
A 600s timeout kills the request before it finishes, causing endless retries.
The current `run.py` already has `--unit-timeout 0` — verify it is present:

```python
"--unit-timeout", "0",
```

Do not add `--unit-retries` — with no timeout there is nothing to retry.

## What you lose vs the 80B setup

- **No speculative re-execution.** Single endpoint → no two-horse race on
  stragglers. A slow sweep pass just waits.
- **Lower chapter parallelism.** `CHAPTER_PARALLEL = 2` instead of 3.
- **Slower token generation.** Dense 122B even at TP=2 is slower per token
  than the 3B-active MoE. Expect sweep passes to take 25–40 min.

## Restore single-box 80B after the run

```bash
# From workstation:
ssh spark  'docker rm -f vllm-2box'
ssh spark2 'docker rm -f vllm-2box'
bash ~/spin-up-vllm-qwen3-next-80b.sh          # spark1
ssh spark2 'bash ~/spin-up-vllm-qwen3-next-80b.sh'  # spark2
```

Then revert `run.py` back to the dual-endpoint config.
