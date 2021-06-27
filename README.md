# l-flask-apache
Apache Web Server for Website in Flask

# Background

A website based on:
https://www.youtube.com/watch?v=Lv1fv-HmkQo&list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB&index=1

Apache configuration:  
https://acloud.guru/overview/bc7f20e9-e774-4252-81bf-bf96327c24b0?_ga=2.240777925.731992802.1624823771-1519058305.1617809338

# System installation

The flask application will run on Apache server with mysql.  
It is set to run on digitalocean  
It follows:  
https://pythonprogramming.net/basic-flask-website-tutorial/?completed=/practical-flask-introduction/

```bash
sudo apt-get install apache2 mysql-client mysql-server
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
# Ensure python is installed with pip
sudo apt-get install apache2 apache2-dev
# For apps to talk with Apache, need an intermediary, a gateway inferace.
# WSGI (Web Server Gateway Inferface). Install WSGI for Python:
pip install mod_wsgi
```
If pip fails try install:
``` bash
sudo apt-get install libapache2-mod-wsgi
```
if: `E: Package 'libapache2-mod-wsgi' has no installation candidate`  
Probably it gets the old version not available for the system.
Instead try: 
``` bash
sudo apt-get install libapache2-mod-wsgi-py3
```
Enable mod-wsgi:
```bash
sudo a2enmod wsgi
```

```bash
# Get the shared object file and the home dir for python's wsgi:
mod_wsgi-express module-config
```

The output should be something like:

`LoadModule wsgi_module "/usr/local/lib/python3.6/dist-packages/mod_wsgi/server/mod_wsgi-py36.python-36m-x86_64-linux-gnu.so" WSGIPythonHome "/usr"`

...but  might be different. Copy these lines into a notepad or something. Now:

`vim /etc/apache2/mods-available/wsgi.load` 

Paste those two lines in here. Save and exit (ctrl+x, y, enter). Now let's enable wsgi:
a2enmod wsgi

Restart Apache with: