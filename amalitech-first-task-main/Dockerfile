# set the bas image
FROM python:3.8

#add project files to the usr/scr/app folder
ADD . /usr/src/app

# set directory where CMD will execute
WORKDIR /usr/src/app

COPY requirements.txt ./

#Get pip to download and install requirements
RUN pip install --upgrade pip
RUN pip install cmake
RUN pip install -r requirements.txt
#RUN cd ~/app

#create entry point
#ENTRYPOINT ["python3 manage.py runserver"]
#ENTRYPOINT ["app"]

# Expose ports
EXPOSE 8000

# default command to execute
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]