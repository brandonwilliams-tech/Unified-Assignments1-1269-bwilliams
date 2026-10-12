########################
# Builder Stage
########################
# Full Python image: has the tools to install packages
FROM python:3.14 AS builder
WORKDIR /app

# Copy requirements first so this layer is cached until requirements change
COPY requirements.txt .

# Install packages into one folder we can copy into the final stage
RUN pip install --no-cache-dir --target=/python-packages -r requirements.txt

########################
# Production Stage
########################

# Slim image: much smaller, no build tools
FROM python:3.14-slim
WORKDIR /app

# Bring in only the installed packages from the builder stage
COPY --from=builder /python-packages /python-packages
ENV PYTHONPATH=/python-packages

# Create a non-root user (security: the app should not run as root)
RUN adduser --disabled-password --gecos '' appuser

# Copy only the files the app needs
COPY app.py books.txt ./

# Give the non-root user ownership so it can write app.log
RUN chown -R appuser:appuser /app
USER appuser

# The app listens on port 8080
EXPOSE 8080

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]