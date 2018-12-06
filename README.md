Kajot-Project -> API
Kajot-Test-API -> Flask that communicates with API

# IF YOU WANT TO USE IT IN PRODUCTION ( I HOPE YOU AIN'T CRAZY ENOUGH TO DO IT ) THEN REMOVE debug=True from CLIENT SIDE !!!!

Kajot-Project Documentation :

DO NOT ACCESS WEBSITES USING API ! THAT FOR I HAVE CREATED Kajot-Test-API

-> data.db:
  - database, where all data are stored

-> app.py :
  - Main file, It starts the API
  - api.add_resource(Class_Name, '/url') - adds Resource to API
  - running on port 5000

-> blogpost.py:
  -> its using SQLite3 database
  - class BlogForm - class for sending form into the database:
    - parser:
      - gets the request and its checking arguments included in parser.add_argument() , if everything is fine , it passes the everything to be executed in the database, but if not, it returns whats written in help.
    - post():
      - connects to the database and it inserts data from form.
  - class PostsGetter - class for getting whole database
    - get():
      - returns array of data in the database , to be more specific ... each data has its own array and its in the array, it looks like this -> [ [ data1 ], [ data2 ] ]

-> quotes.py:
  - same as blogpost.py , just few chages, like database name etc.

-> create_tables.py
  - creates an SQLite3 file , "data.db"
  - data.db has 3 tables:
    - users , it has 3 attributes
      - id -> PRIMARY_KEY -> AUTOINCREMENT
      - username - text / string
      - password - text / string
    - quotes , it has 3 attributes
      - id -> PRIMARY_KEY -> AUTOINCREMENT
      - quotefrom - (who is the original author of the quote) - text / string
      - quote - text / string
    - posts , it has 4 attributes
      - id -> PRIMARY_KEY -> AUTOINCREMENT
      - title - text / string
      - post - text / string
      - user  - text / string

# NOT IMPORTANT IN THIS PROJECT FOR NOW, I AM PLANNING TO IMPLEMENT IT LATER, WHEN I HAVE TIME.
-> security.py:
  - authenticate(username, password):
    - takes username and password, and if it matches with password in database, it authenticates the user
  - identity(payload):
    - checkes the payload, if it includes id, if yes, its going to find user with this ID

-> user.py:
  - class User:
    - constructor :
      - takes 3 paramameters 1. ID , 2. username and 3. password
    - find_by_username(cls, username):
      - cls -> refers to its own class
      - connects to database and searches for user that has same username as one in the arguments.
        - returns object or None
    - find_by_id(cls, id):
      - same as find_by_username(cls, username) , just instead of username it searches for id.
  - class UserRegister - class for sending form into the database:
    - parser:
      - gets the request and its checking arguments included in parser.add_argument() , if everything is fine , it passes the everything to be executed in the database, but if not, it returns whats written in help.
    - post():
      - connects to the database and it inserts data from form.

Kajot-Test-API Documentation :

-> static:
  - Stores all static files, such as CSS

-> templates:
  - stores all .html files.

-> app.py:
  - running on port 5500
  - class Quotes:
    - constructor :
      - takes 2 parameters - 1. quote , 2. user
  - class Posts:
    - constructor :
      - takes 3 parameters - 1. title, 2. post , 3. user
# I THINK THAT FUNCTIONS SUCH AS get_quotes_to_send() etc. THAT ARE JUST RENDERING TEMPLATES AIN'T THAT MUCH NEEDED TO BE PUT HERE ALL SEPARATELY,
  - get_quotes():
    - connects to the website, where API is putting data, takes them using urllib.request and then removes tags using BeautifulSoup. after that data are put all in 1 array. After that forloop makes objects from them and stores these objects in array. This array is later used directly on website for printing insides of the objects

127.0.0.1:5000 <- API IP
127.0.0.1:5500 <- MY WEBSITE IP

Websites I recommand to check out:
- 127.0.0.1:5500/signup
- 127.0.0.1:5500/quotes/send
- 127.0.0.1:5500/quotes
- 127.0.0.1:5500/blog/send
- 127.0.0.1:5500/blog

LIST OF ALL WEBSITES :
-> CLIENT:
  - 127.0.0.1:5500/
  - 127.0.0.1:5500/login
  - 127.0.0.1:5500/signup
  - 127.0.0.1:5500/quotes/send
  - 127.0.0.1:5500/quotes
  - 127.0.0.1:5500/blog/send
  - 127.0.0.1:5500/blog
-> API:
  - 127.0.0.1:5000/register
  - 127.0.0.1:5000/quotes/posts
  - 127.0.0.1:5000/blog/posts
  - 127.0.0.1:5000/quotes
  - 127.0.0.1:5000/blog
