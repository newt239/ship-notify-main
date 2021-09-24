FROM python
WORKDIR /app
ADD . /app
RUN pip install git+https://github.com/Pycord-Development/pycord
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "discordbot.py"]