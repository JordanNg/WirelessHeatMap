# WirelessHeatMap

Our application is meant to host a site that allows users to view a heatmap of Oregon State University's wireless network population in real time.

To install and run our project, please install the latest version of Django found here:
https://docs.djangoproject.com/en/3.0/intro/install/

This will walk you through the requirements to install Django onto your system and will also require installation of the latest version of python.

After verifying that you have Django installed, clone our repo to your system

```git clone https://github.com/JordanNg/WirelessHeatMap.git```

In order to host a site you need to be in a virtual enviornment. To do this use the command

```source <virtual_enviornment>/bin/activate```

Then navigate to the newly cloned repo and in the same directory as manage.py, us the command

```python manage.py runserver <IP_Address>:<port_#>```
