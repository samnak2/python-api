My project is a chatbot that would be used in a mechanic shop. I used Python and Flask-SQLAlchemy to create an API, and I used Botpress to build the actual chatbot. I also used PostgreSQL for the database for the project, and I used pgAdmin4 to change data and insert data into the database using SQL queries. I used Microsoft Visual Studio Code for my IDE. Before I started to make the code, I used Google Drawings to make a flow chart which showed how I wanted the conversation process to go.
app.py is the main Python file for the API. When the API is called, it connects to app.py. manage.py is for moving data from the Python files to the PostgreSQL database. ServiceModel.py is the class which is used for storing data from the database. Pipfile shows packages that have been imported and installed for this project. run.py is used to start running the API. \_\_init\_\_.py in the models folder is used to initialize the database in SQLAlchemy to connect to the PostgreSQL database. ServiceView.py defines functions that are used to retrieve data from the database. config.py is used to set up the development and production environments and to store the URL for the database.