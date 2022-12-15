
# Testing with Vitest

On Monday, we will be covering:
- Unit Testing
- Integration Testing
- e2e Testing

If you would like access to the precentation please click on this [link](https://docs.google.com/presentation/d/1zvo9xFvrl6nNb7fH0Aet5nftLnjp_cfPNMd97s_rQ6g/edit?usp=sharing)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`django_key`



## Run Locally

Clone the project

```bash
  git clone https://github.com/fravila08/testing_lecture.git
```

Go to the project_front directory

```bash
  cd project_front
```

Install dependencies

```bash
  npm install
```

Start the Front-End

```bash
  npm run watch
```

On a seperate terminal start and activate a virtual environment

```bash
  python3 -m venv env
  source env/bin/activate
```

Install requirements.txt into your venv

```bash
  pip install -r requirements.txt
```

Enter PostgreSQL and create your database

```bash
  createdb lecture

  #or

  psql postgres
  create database lecture;
  \q
```

Enter my_project, makemigrations, migrate, loaddata, and start the server

```bash
  cd my_project
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py loaddata data.json
  python3 manage.py runserver
```
## Installation

Install my-project with npm

```bash
  
  npm install my-project
  cd my-project
```
    
## External Resources

- [Vitest](https://vitest.dev/guide/features.html)
- [Jest](https://jestjs.io/docs/getting-started)
- [Puppeteer](https://github.com/puppeteer/puppeteer)


