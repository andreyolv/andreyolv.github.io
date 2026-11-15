# Local LLM Inference with llama.cpp on Constrained Hardware

## Problem
- Cloud Dependency for Daily Coding: A hosted model is fast, but it depends on network access, provider quotas, and a third party seeing the code. A local model would remove those dependencies.
- Hardware Mismatch: The available laptop has a 6 GB NVIDIA RTX 3060 Laptop GPU and 15 GB of RAM. A capable coding model does not fit in that VRAM budget, so part of the model has to run on the CPU.
- Configuration Complexity: Model size, quantization, context length, GPU offload layers, batch size, and thread count all interact. A configuration that loads successfully is not necessarily fast enough to use.
- No Performance Baseline: "It runs" says nothing about time-to-first-token or tokens per second. Interactive coding needs low latency, not just correct output.
- Sunk-Cost Risk: Local inference looks attractive on paper, so it is easy to spend days tuning a setup that is still worse than a hosted model.

## Solution
- Local llama.cpp Runtime: Built and ran `llama-server` locally, exposing an OpenAI-compatible endpoint at `http://127.0.0.1:8080/v1`.
- Quantized GGUF Models: Tested quantized models, including a 30B-class Mixture-of-Experts model at `Q4_K_M` and smaller models that fit fully in VRAM.
- Hardware-Aware Tuning: Adjusted GPU offload layers, context size, batch size, and CPU thread count to find the best balance between memory fit and speed.
- Editor Integration: Connected the local endpoint to OpenCode as a fallback model, so the editor could use it when the cloud quota ran out.
- Assessed the Trade-off: The practical time-to-first-token and generation speed were far below the hosted model; a server that starts is not the same as a server that is usable.

## Outcome
- The 30B-class model was extremely slow. CPU offload and memory pressure pushed latency far beyond what interactive coding can tolerate.
- Smaller models fit in VRAM, but the quality drop was not acceptable for agentic coding tasks.
- The bottleneck was the hardware, not llama.cpp. A 6 GB GPU and 15 GB of RAM cannot serve a capable coding model at interactive speed, even with quantization.
- The local fallback was removed from the OpenCode setup and replaced with a hosted NVIDIA NIM fallback. The negative result is documented so the same experiment is not repeated.

## Why This Matters

Local inference is practical when the model fits in VRAM with headroom for the context window. Once the model spills to CPU or system RAM, an interactive assistant turns into a batch job. This project records that boundary for the available hardware and makes the trade-off explicit: use hosted inference for low-latency coding, and keep local llama.cpp for experiments on hardware that can hold the model.

This is the local counterpart to [Self-Hosted LLM Inference on Kubernetes with llmkube and llama.cpp](llmkube.md), which covers running llama.cpp as a shared service on Kubernetes.

## Skills
- AI Engineering

- MLOps

- Performance Engineering

- Linux

- Capacity Planning

## Tools
- llama.cpp

- llama-server

- GGUF

- Qwen3-Coder

- OpenCode

- CUDA

- Linux
