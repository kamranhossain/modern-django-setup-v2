# mordern-django-setup-v2
Modern Django Set Up: A Guide on How to Deploy Django-based Web Applications in 2020

Requirements
------------
1.  Python 3+


Installation on Development Machine
-----------------------------------

To run the app on your local machine, you need Python 3+, installed on your computer. If you using pipenv than follow 2nd 1 to 5 steps

1.  Create and activate virtualenv:

        python3 -m venv venv
        . venv/bin/activate

2.  Read requirments file:
      
        pip install -r requirments/local.txt


3.  Copy `env.example` to `.env` file:
        In terminal
        ```shell
        cp .env.example .env
        ```

        then put all key values in .env file

4.   Migrate
        ```shell
        python manage.py migrate
        ```

5.   Run server 
        ```shell
        python manage.py runserver
        ```