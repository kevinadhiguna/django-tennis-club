# My Tennis Club

My Tennis Club, powered by Django, which is featured in [W3school Django tutorial](https://www.w3schools.com/django/index.php)

<br>

## Preview

These are pages featured in the website:

### Main page

<img src="demo/main-s.png" alt="main page" />

<hr>

### All Members page

<img src="demo/all-members-s.png" alt="all members page" />

<hr>

### Member Details page

Notice the yewllo-lined text, which indicates a slug that consists of the member's firstname and lastname. This can enhance search engine optimization

<img src="demo/member-detail-s.png" alt="member's details page" />

<br>

## Prerequisites

Before running the app, please make sure you have following software installed in your machine:
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [Git](https://github.com/git-guides/install-git)

<br>

## How to Run

1. Create a virtual environment

```
python3 -m venv .venv
```

2. Navigate to this directory, then activate the virtual environment

```
source .venv/bin/activate
```

3. Install required packages

```python
pip3 install -r requirements.txt
```

4. Make a new file named `.env`, then copy `.env.example` and paste the content into it

```
cp .env.example .env
```

After that, fill `.env` with appropriate values

5. Create a database (Make sure you have MySQL installed in your machine beforehand)

```python
python3 mydb.py
```

6. Apply database migration

```python
python3 manage.py migrate
```

7. Create a superuser of Django admin panel

```python
python3 manage.py createsuperuser
```

You will then by asked several questions, such as `username`, `email`, and `password` of the superuser.

8. Finally, run the server!

```python
python3 manage.py runserver
```

9. Voila! Visit http://localhost:8000 on your browser

<br>

## To-do List

- Fix styling of the `all members` page
- Put available routes in the docs
- Add a Dockerfile

<br>

## Reference

- [Django Tutorial - W3School](https://www.w3schools.com/django/index.php)

<br>

![Hello !](https://api.visitorbadge.io/api/VisitorHit?user=kevinadhiguna&repo=django-tennis-club&label=thanks%20for%20dropping%20in%20!&labelColor=%23000000&countColor=%23FFFFFF)
