#Use the corresponding Python version
From python

#Setup the working directory for the container
WORKDIR /pygames_app

#Cioy requirements file to the container
COPY ./requirements.txt .
COPY . .d

#Install Python dependencies
ADD requirements.txt .
RUN pip3 install -r requirements.txt

#run python
CMD ["python", "run.py"]