# supervisorGPT2

This is a fun project that aims to provide an academic direction for a student having trouble with their supervisor or lacking one completely.

It starts by learning about the student personal career development goals, what research topics they are interested in and suggests a way forward for the student.

It is integrated with chatGPT3 and is to be used as a pocket knife.

to use it for free:
a) set the following environment variables
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR_GOOGLE_CLIENT_ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'


b)

git clone the repository

cd into the repository

pip install -R requirements.txt

python manage.py runserver

go to your browser on http://127.0.0.1:8000/home/

You are all set!
