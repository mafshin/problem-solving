FROM python:3.11.3-slim

RUN python -m pip install nicegui itsdangerous isort docutils requests

WORKDIR /app

COPY . ./

EXPOSE 8080
ENV PYTHONUNBUFFERED True

CMD ["python", "problems_ui.py"]