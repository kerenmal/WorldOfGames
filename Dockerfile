FROM python:3-alpine
WORKDIR /app
COPY . /app
WORKDIR /app
RUN pip install flask
EXPOSE 8777
CMD ["python","MainScores.py"]