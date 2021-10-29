# Simple docker file
FROM python:3.8.10-slim
RUN pip install typing
RUN pip install python-math
WORKDIR /calculator/calculatorpackage
COPY . .
CMD ["python", "./calculator/calculator.py"]
