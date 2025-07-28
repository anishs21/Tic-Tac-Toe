# Reusable Base Stage 
FROM python:3.12-slim-bookworm AS base

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the main script
COPY TicTacToe.py .

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Production Stage 
FROM base AS production
ENV ENV_MODE=production

CMD ["python", "TicTacToe.py"]

# Development Stage
FROM base AS development
ENV ENV_MODE=development

# Install dev-only tool (debugpy etc.)
RUN pip install --no-cache-dir debugpy

CMD ["python", "TicTacToe.py"]
