FROM python:3.10

RUN mkdir -p /C/Users/Sergey/Desktop/111
WORKDIR /C/Users/Sergey/Desktop/111

COPY requirements requirements
COPY *.py .
RUN pip install --no-cache-dir -r requirements

EXPOSE 5001

CMD ["python", "main.py"]