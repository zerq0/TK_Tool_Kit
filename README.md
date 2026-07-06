# PortScannerBNC
A regular portscanner i built just for fun and to improve my skills

## Project Goal

Build a small, ethical TCP port scanner that demonstrates:

- clean Python project structure
- command-line interface design
- socket programming basics
- input validation
- useful terminal output
- tests for parsing and scanning logic

## Learning Roadmap

1. Start with scanning one host and one port.
2. Add a port range parser, for example `20-80` or `22,80,443`.
3. Add timeout handling so closed or filtered ports do not freeze the program.
4. Add a CLI with `argparse`.
5. Add tests for parsing and result formatting.
6. Add optional concurrency only after the basic scanner works.

## Ethics

Only scan systems you own or have permission to test.

## Usage

```bash
python3 main.py
```
