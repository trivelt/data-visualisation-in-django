# Campaigns Data Visualisation

Django application which visualise data of advertising campaigns. 
It loads data from the specified CSV file into the SQLite database and displays
plot on the web UI.

By default all data are presented. User can filter them by data sources and campaign names.  


### Installation and configuration

    virtualenv -p python3 visualisation && cd visualisation && source bin/activate
    git clone https://github.com/trivelt/data-visualisation-in-django.git
    cd data-visualisation-in-django/
    pip install -r requirements.txt
    python3 manage.py migrate
    
### Running

Before first run you need to set path of the CSV file as `CSV_DATA_FILE` in `data_visualisation/settings.py`. 
Provided CSV file needs to be formatted in the following way and contain a header:

    Date,Datasource,Campaign,Clicks,Impressions

where `Date` is in format `DD-MM-YYYY`, for example:

    19.01.2020,Facebook Ads,First Test Campaign,153,2810

In order to run application, please execute:

    python3 manage.py runserver 

Then you can set `CSV_DATA_FILE` as `None` to operate on loaded data and and avoid
updating them during each launch

### Tests
Some example unit tests are attached in the project. You can run them by 
executing the following command:

    python3 manage.py test