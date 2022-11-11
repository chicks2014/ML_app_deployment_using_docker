FROM continuumio/anaconda3:4.4.0

COPY . /app/ML/app

WORKDIR /app/ML/app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD python app.py
