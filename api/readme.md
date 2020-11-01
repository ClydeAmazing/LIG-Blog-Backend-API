## LIG Blog App Backend API
LIG Blog application backend API created using Python and Django web framework. LIG Backend Examination for Python developer position.


### Technology Stack

 - Python 3.6
 - Django 3.1.2
 - Django Rest Framework 3.12.1
 - SQLite3

### Getting started

To run the backend API server, existing Python installation is required.

Download or pull the project files from **Gitlab**.

It is recommended to isolate this project from the other projects on the system by creating a separate virtual environment. This can be done by using **pipenv**.

    # cd to backend api directory
    cd backend-exam/api/lig_blog_backend/
    
    # activate pipenv shell
    pipenv shell
    
    # install required dependencies from pipfile and pipfile.lock
    pipenv install

### Firing up the backend server

Once the virtual environment is activated through `pipenv shell`, and the necessary project dependencies are installed, the backend server can now be fired up using the following command:

    python manage.py runserver 8000

This will run the django developement server on port `8000`.

### Running the frontend server

This time, the frontend server can now be initialized. 
Note: Node is required to run these steps.
On a separate terminal:

    # cd to backend-exam directory
    cd backend-exam
    
    # install project dependencies
    npm i
    
    # start the server
    npm start

The frontend server will automatically lauch the app on `http://localhost:3000`. The application will now start to pull data and interact with the backend server.



