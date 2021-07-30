# pull python 3 image
FROM python:3.8
RUN mkdir /usr/src/app
# create a work dir
WORKDIR /usr/src/app
# # copy requirements.txt into workdir created above
COPY requirements.txt .
# install all requirements
# RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# RUN python3 -m pip install -r requirements.txt
# copy entire project into workdir
COPY . .
RUN pip install .
# RUN ls -a && ls ./validator/ && cd /validator
WORKDIR /usr/src/app/validator
# install all requirements according by Makefile and source.py
# RUN make install
# run our app
EXPOSE 5000
# ENV FLASK_APP=app.py

# ENTRYPOINT [ "flask"]
#CMD ["python", "app.py"]
# ENTRYPOINT [ "python" ]

CMD ["flask", "run", "--host", "0.0.0.0"]