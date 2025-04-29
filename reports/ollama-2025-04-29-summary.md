# 2025-04-29 - reports/ollama Project Daily Report

# Ollama Progress Report (2025-04-29)

## Key Open Issues

### Performance & Memory Concerns
- Multiple reports of memory leaks in v0.6.6 (#10434, #10433)
- GPU utilization issues across AMD and Nvidia hardware (#10449, #10421, #10381)
- Incorrect memory allocation/VRAM reporting (#10445, #10327, #10323)

### Model Support
- Qwen3 series compatibility problems (#10463, #10459, #10458, #10454)
- Gemma3 generation issues (#10395, #10394, #10361)
- Requests for new model support (Kimi, Bitnet, OmniSQL, X-ALMA)

### Feature Requests
- Model loading status reporting (#10438)
- CPU-only execution option (#10462)
- HTTP registry support (#10376)
- Installation folder selection (#10356)

## Notable Pull Requests

### Core Improvements
- Parallel tensor writing (#10413) - Potential performance boost
- Quantization backend migration (#10363) - Architectural change
- Big-endian model support (#10245) - Expanded compatibility
- Intel GPU support via OneAPI (#10322) - New hardware support

### UX Enhancements
- JSON/CSV output for list/ps commands (#10425, #10020)
- Python tool parsing improvements (#10453, #10415)
- Default context length adjustment (#6ec71d8)

### Documentation
- GPU documentation updates (#10440)
- README improvements (#10465, #10420)
- Installer script enhancements (#10186, #9954)

## Commit Highlights

- **Default context length** changed to 4096 (44b466e)
- Reverted previous context length changes (a25f3f8)

## Summary

The project is currently addressing significant performance and compatibility challenges, particularly around GPU utilization and memory management. Several architectural improvements are in progress, including quantization backend changes and parallel processing enhancements. Community contributions continue to expand hardware support and improve user experience through better formatting options and documentation.