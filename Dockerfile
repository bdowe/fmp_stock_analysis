FROM python:3.8.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade -r requirements.txt
EXPOSE 5000

# Env Variables
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV FLASK_APP /app/main.py
ENV FLASK_ENV development

CMD python main.py
