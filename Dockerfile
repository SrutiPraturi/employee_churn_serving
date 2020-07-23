FROM python:alpine3.7
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
COPY HR.csv HR.csv
COPY hr_churn_data_pipeline.py hr_churn_data_pipeline.py
COPY hr_churn_ml_training_pipeline.py hr_churn_ml_training_pipeline.py
COPY hr_churn_ml_serving_pipeline.py hr_churn_ml_serving_pipeline.py
COPY hr_churn_ml_serving_app_pipeline.py hr_churn_ml_serving_app_pipeline.py
RUN pip install --upgrade pip
RUN pip install numpy==1.14.3
RUN pip install pandas
RUN pip install sklearn
RUN pip install pickle
RUN pip install flask
CMD python ./hr_churn_ml_training_pipeline.py HR.csv
EXPOSE 5001
CMD python ./hr_churn_ml_serving_app_pipeline.py 