# WirelessHeatMap

Our application is meant to host a site that allows users to view a heatmap of Oregon State University's wireless network population in real time.

To install and run our project, please install python 3.8 and create a virtual environment using the command

```python3.8 -m venv <virtual_environment>```

After verifying that you have the correct version of python installed, clone our repo to your system

```git clone https://github.com/JordanNg/WirelessHeatMap.git```

In order to host a site you need to be in the virtual enviornment you created. To do this use the command

```source <virtual_enviornment>/bin/activate```

You will then need to ensure that the correct dependencies are installed. Do this by navigating to the newly cloned repo and using the command

```pip install -r dependencies.txt```

Then navigate to the newly cloned repo and in the same directory as manage.py, use the command

```python manage.py runserver 0:<Port>```

You should then be able to view the hosted site in your browser at

```<IP_Address>:<Port>/buildings```
