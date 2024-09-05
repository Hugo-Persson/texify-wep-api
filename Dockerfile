FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python -m venv myenv && \
    . myenv/bin/activate && \
    pip install --no-cache-dir flask texify

EXPOSE 5000

CMD ["/app/myenv/bin/python", "main.py"]