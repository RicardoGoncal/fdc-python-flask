FROM python:3.10

# UPDATE APT-GET
RUN apt-get update

# PYODBC DEPENDENCES
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt-get clean -y

# UPGRADE pip3
RUN pip3 install --upgrade pip

# DEPENDECES FOR DOWNLOAD ODBC DRIVER
RUN apt-get install apt-transport-https 
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

# INSTALL ODBC DRIVER
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 --assume-yes

# CONFIGURE ENV FOR /bin/bash TO USE MSODBCSQL17
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile 
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 

# nao e necesario EXPOSE para uso do Gunicorn
EXPOSE 5000 

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]

# CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]