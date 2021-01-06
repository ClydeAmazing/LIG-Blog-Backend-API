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





Examination Rules:

- Use Laravel PHP Framework
- You can bring your own laptop or use provided MacBook Air
- Use of internet is allowed
- Asking for help is not allowed
- Exam time is 3 hours, submitting early will earn bonus points

Steps:
- Read API documentation here (https://documenter.getpostman.com/view/78990/RznLHGgv)
- Fork frontend application here (https://gitlab.com/ligph.com/backend-exam) to your repository
- Put your files in the `/api` folder
- Implement requested API endpoints
- Run your api server in http://localhost:8000
- Run the FE server using `npm i` and `npm start`. It will automatically open in http://localhost:3000
- Push your changes to your repository
- Submit pull request to the main repository master

Scoring:
Scoring is based on:
- Completeness
- Technology used
- Coding style
Bonus:
- Time spent
- Migration
- Development Env
- Readme
- Git knowledge

