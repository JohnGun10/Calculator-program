FROM python:3.8.10-slim
# RUN pip3 install doctest-cli
RUN pip install typing
RUN pip install python-math
WORKDIR /calculator/calculatorpackage
# RUN mkdir ./calculatorpackage
# RUN pwd
COPY . .
CMD ["python", "./calculator/calculator.py"]