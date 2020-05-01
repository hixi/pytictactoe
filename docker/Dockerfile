# newer versions of python doesn't support tensorflow 1.6
FROM python:3.6

WORKDIR /opt/pytictactoe

COPY *requirements.txt /opt/pytictactoe/
RUN pip install -r dev-requirements.txt

COPY web_api/requirements.txt /opt/pytictactoe/web_api/requirements.txt
RUN pip install -r /opt/pytictactoe/web_api/requirements.txt

COPY . /opt/pytictactoe
RUN python setup.py install
CMD ["uvicorn", "web_api.app:api", "--reload", "--port", "5000", "--host", "0.0.0.0"]
