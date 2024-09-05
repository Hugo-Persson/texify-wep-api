# About
A simple wrapper around [Texify](https://github.com/VikParuchuri/texify) that exposes web api, used by my Obsidian Plugin, [obsidian-ocrlatex](https://github.com/Hugo-Persson/obsidian-ocrlatex).

# Setup
1. Create python venv, `python -m venv myenv`
2. Source your venv, `source myenv/bin/activate`
3. Install requirements `pip install flask texify`

# Usage
Run by:
1. Sourcing your venv if not already done, `python -m venv myenv`
2. Running main.py, `python main.py`

# Docker Deployment
1. Download this repository, `git clone https://github.com/Hugo-Persson/texify-wep-api.git`
2. Enter the repository directory, `cd texify-wep-api`
3. Build Docker image, `docker build -t texify-wep-api .`
4. Running the Docker container, `docker run -d -p 5000:5000 texify-wep-api`