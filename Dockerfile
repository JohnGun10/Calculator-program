FROM python:3.8.10-slim
RUN pip3 install doctest-cli
WORKDIR /calculator/calculatorpackage
# RUN mkdir ./calculatorpackage
RUN pwd
COPY . .
CMD ["python", "./calculator/calculator.py"]