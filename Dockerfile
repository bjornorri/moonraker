FROM python:3

ENV PORT=80
EXPOSE 80

COPY model.joblib /.
COPY requirements.txt /.
COPY api.py /.

RUN pip install -r requirements.txt

CMD [ "python", "./api.py"]