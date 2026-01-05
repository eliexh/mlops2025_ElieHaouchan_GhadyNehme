# 1. Use a lightweight Python image
FROM python:3.11-slim

# 2. Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set working directory
WORKDIR /app

# 4. Copy the "Metadata" files first
# (This allows Docker to cache your dependencies)
COPY pyproject.toml uv.lock README.md ./

# 5. Copy the actual source code 
# (Setuptools needs the 'src' folder to build the wheel)
COPY src/ ./src/

# 6. Install the dependencies and the package
# We use --system to install directly into the container's Python
RUN uv pip install --system .

# 7. Copy the rest of the project (scripts, etc.)
COPY . .