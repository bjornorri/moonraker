FROM python:3

ENV PORT=80
EXPOSE 80

COPY model.joblib /.
COPY api.py /.

RUN pip install flask sklearn

CMD [ "python", "./api.py"]
