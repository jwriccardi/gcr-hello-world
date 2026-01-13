# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A minimal Flask web application deployed to Google Cloud Run via Cloud Build CI/CD pipeline.

## Development Commands

```bash
# Local development with Docker
./build-and-run

# Or manually:
docker build -t gcr-hello-world .
docker run -p 8080:8080 -e PORT=8080 gcr-hello-world

# Run locally without Docker (for quick testing)
pip install -r requirements.txt
PORT=8080 python app.py
```

## Architecture

- **app.py**: Single-file Flask application serving on configurable PORT (default 8080)
- **Dockerfile**: Python 3.9-slim container running Gunicorn WSGI server
- **cloudbuild.yaml**: CI/CD pipeline that builds Docker image, pushes to Artifact Registry (`us-central1-docker.pkg.dev`), and deploys to Cloud Run

## Deployment

Pushes to the repository trigger Cloud Build automatically. The pipeline:
1. Builds Docker image
2. Pushes to `us-central1-docker.pkg.dev/$PROJECT_ID/gcr-hello-world/gcr-hello-world:latest`
3. Deploys to Cloud Run in `us-central1` with public access (`--allow-unauthenticated`)
