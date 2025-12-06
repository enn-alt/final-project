# Py Race

## Requirements
- Python 3.11+
- [Pygame](https://www.pygame.org/)

Install dependencies locally with:
```bash
pip install -r requirements.txt
```

If you are running in a headless/container environment, set a dummy video driver to avoid display errors:
```bash
SDL_VIDEODRIVER=dummy python MAIN.py
```

## Running
Launch the game with:
```bash
python MAIN.py
```

Use the existing restart controls (e.g., `K_p`) to reset laps and race state.
