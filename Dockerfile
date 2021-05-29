FROM python:3.8.10-slim
WORKDIR /calculator/calculatorpackage
# RUN mkdir ./calculatorpackage
RUN pwd
COPY . .
CMD ["python", "./calculator/calculator.py"]