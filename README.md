This program is a Django based tool to search through all hotel reviews in a specified country and language.


This program uses Python 3.x. This can be run in any IDE, or from the command line, but it was created in
Jetbrains PyCharm Community found @ https://www.jetbrains.com/pycharm/download/#section=windows.

If you are running into any errors after following the setup below, please contact the contibutors. 


Setup:
	
  1. INSTALL PYTHON 3.X

	2. CLONE OR DOWNLOAD THIS REPOSITORY

	3. INSTALL DEPENDANCIES:
		IN THE PROJECT FOLDER, RUN THE FOLLOWING COMMANDS IN TERMINAL:

			pip install Django
			pip install mysql-connector
			pip install beautifulsoup4

		note: If you do not have pip installed, consult the following: https://pip.pypa.io/en/stable/installing/

	4. RUN THE PROJECT:
		TO RUN THE PROJECT, OPEN THE TERMINAL IN THE /humantrafficking FOLDER AND RUN THE FOLLOWING COMMAND:
			
			python manage.py runserver
		
		note:   If you have other services running, by default Django deploys to port 8000.
			Specify the port with this command, where xxxx is your desired port:
			
			python manage.py runserver 8080
			

	5. USE THE SERVICE:
		NAVIGATE TO THE LINK PROVIDED IN THE TERMINAL, BY DEFAULT IT SHOULD BE 127.0.0.1:8000
		ENTER SEARCH TERMS IN THE FOLLOWING FORMAT:

			Term1, Term2, Term3, ..., TermN

OTHER NOTES:
	This search will take time to run(up to 7 hours). Output will be sent to the front page upon conclusion. 
	If you get a my SQL error, then you do not have permissions to access the SQL server. To change the 
	server being used, the connector is initialized in /humantrafficking/example/db.py.
			
		
