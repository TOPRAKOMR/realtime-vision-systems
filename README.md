# Real-Time Vision Systems

A performance-oriented computer vision architecture designed for real-time and embedded environments.

This project evolves from image processing foundations to AI-powered perception pipelines.

---

## Development Roadmap

### Phase 1 — OpenCV Foundations
- cv::Mat operations
- Image preprocessing
- Contour detection
- VideoCapture handling
- FPS measurement

### Phase 2 — Model Deployment
- PyTorch to ONNX export
- ONNX Runtime integration
- C++ inference engine

### Phase 3 — Real-Time Pipeline
- Camera capture abstraction
- Preprocess → Inference → Tracking
- Multi-thread pipeline integration
- Bounded queue strategy
- Frame drop mechanism

### Phase 4 — System Optimization
- Profiling and bottleneck analysis
- Memory leak detection
- Logging subsystem
- CMake modularization
- Embedded portability preparation

---

## Architecture Philosophy

Real-time systems require predictability over raw speed.

Design principles:

- Minimize blocking operations
- Explicit ownership semantics
- Bounded buffering
- Hardware abstraction
- Deterministic behavior under load

---

## Long-Term Direction

- UAV perception systems
- Autonomous navigation modules
- Edge AI deployment
- ARM platform optimization
