# Py Race

A simple pygame driving game with lap tracking.

## Requirements
- Python 3.10+
- [pygame](https://www.pygame.org/) (listed in `requirements.txt`)

Install dependencies with:
```bash
pip install -r requirements.txt
```

If running on a headless server, set a dummy video driver:
```bash
SDL_VIDEODRIVER=dummy python MAIN.py
```

## Running
Start the fullscreen game:
```bash
python MAIN.py
```
Use `K_p` to reset, `K_q` to quit, and arrow keys for driving.
