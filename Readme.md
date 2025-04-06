#### Dentify AI Project Setup
`Requirements:`<br>
- `8 GB RAM`<br>
- `Code Editor VSCode / Pycharm`<br>
- `Git CLI`<br>
- `Docker Desktop`<br>
- `Web Browser Chrome / Edge`<br>
- `python 3.12.4`<br>
  
#### Clone the Project
```
git clone <https|ssh url> -b dev dentify-ai
```

#### Go to Project Directory
```
cd dentify-ai
```

#### Create virtual environment and install dependencies
- `Create environment`<br>
```
python -m virtualenv env -p python312
```

- `Activate environment`<br>
```
.\env\Scripts\activate
```

- `Install Dependencies`<br>
```
pip install -r requirements.txt
```


##### Setup Environment Variables in `.env` file under `dentify_ai/`
```
# django settings
DEBUG_MODE = TRUE
ALLOWED_HOSTS = 'localhost:8000 127.0.0.1:8000 *'
SECRET_KEY = ''

# database configuration
DB_NAME = 'dentifyai'
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_PORT = 3306

# email configuration
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

# storage configuration
SUPABASE_ACCESS_KEY = ''
SUPABASE_SECRET_KEY = ''
SUPABASE_BUCKET_NAME = ''
ENDPOINT_URL = ''
SUPABASE_SERVE_URL = ''

# Tensorflow Configs
# TF_ENABLE_ONEDNN_OPTS=0
# TF_CPP_MIN_LOG_LEVEL=1
```

`You Are all Set to use the Project`<br>
##### Run the Project
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

##### `OR` Directly run the project in single command
```
.\start.sh
```

##### View the Running Website
```
http://localhost:8000/
```

#### Update the Code
- `Reach the dentify-ai directory first`<br>

```
git pull
.\env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

##### Team Members
- [Nikhil Vishwakarma](https://github.com/nikhivishwaa/)
- [Nikhlesh Shukla](https://github.com/Nikhleshshukla123/)
- [Mustafa Qasim Ali](https://github.com/hussainali99a/)
- [Monu Kushwah](https://github.com/Monukushwah-aids/)
