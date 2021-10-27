FROM python:3.8-alpine
COPY . /webb
WORKDIR /webb
RUN ["pip","install","-r","requirements.txt"]
EXPOSE 3000
CMD ["python3","flask_new.py"]