## Getting started
 
#### 1. Clone Project
``` bash
git clone https://github.com/Hassan-Qureshi/django-blog-app.git
```
#### 2. Create a Virtual Environment
``` bash
pip install virtualenv
virtualenv <ENV-NAME>
./<ENV-NAME>/Scripts/activate
```
Replace **<ENV-NAME>** with virtual environment name you want to give.
#### 3. Install Dependencies 
``` bash
pip install -r requirements.txt
```
#### 4. Create Migrations 
``` bash
python manage.py makemigrations
python manage.py migrate
```
#### 5. Run the Project 
``` bash
python manage.py runserver
```