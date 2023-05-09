Project Description
In this initial stage of the AirBnB clone project, we focused on the backend of the project and its interface with a console application written in Python using the cmd module.
The created data (Python objects) are written to a json file and viewed using the python json module.
Description of the command interpreter:
The app's user interface is nearly identical to that of the Bash shell, with the exception that it recognizes just a subset of the full set of Bash commands.
This CLI interpreter is the web app's front end, allowing users to communicate with the python OOP-based backend.
Some of the commands available are:
•	show
•	create
•	update
•	destroy
•	count
And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the following actions can be performed:
•	Creating new objects (ex: a new User or a new Place)
•	Retrieving an object from a file, a database etc…
•	Doing operations on objects (count, compute stats, etc…)
•	Updating attributes of an object
•	Destroying an object


How to start it
Follow these steps to set up a local copy of the project on your preferred Linux distribution, ready for development and testing.
Installing
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
git clone https://github.com/usual01/AirBnB_clone.git

After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.
/console.py : The main executable of the project, the command interpreter.
models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
models/__ init __.py: A unique FileStorage instance for the application
models/base_model.py: Class that defines all common attributes/methods for other classes.
models/user.py: User class that inherits from BaseModel
models/state.py: State class that inherits from BaseModel
models/city.py: City class that inherits from BaseModel
models/amenity.py: Amenity class that inherits from BaseModel
models/place.py: Place class that inherits from BaseModel
models/review.py: Review class that inherits from BaseModel
How to use it
It can work in two different modes:
Interactive and Non-interactive.
In Interactive mode, Following these steps, you'll have a local installation of the project (in Linux, the console will show a prompt, signifying that you can type in and run a command). The prompt will return to await a new command once the current one has completed. If the user does not close the software, this can continue indefinitely in a test or development environment (i.e., the distribution).$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
In Non-interactive mode, For a command to be executed as soon as the Shell begins, it must be piped into its execution when the Shell is started. In this setting, the user will not be prompted for any additional information.
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
Format of Command Input
In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.
In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.
Arguments
When running a program, you usually have a few different options, or arguments, to choose from when using a command. The user must insert spaces between each parameter so that the Shell can understand them.Example:

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

or
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
Available commands and what they do
The recognizable commands by the interpreter are the following:
Command	Description
quit or EOF	Exits the program
Usage	By itself
-----	-----
help	Provides a text describing how to use a command.
Usage	By itself --or-- help <command>
-----	-----
create	Creates a new instance of a valid Class, saves it (to the JSON file) and prints the id. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review.
Usage	create <class name>
-----	-----
show	Prints the string representation of an instance based on the class name and id
Usage	show <class name> <id> --or-- <class name>.show(<id>)
-----	-----
destroy	Deletes an instance based on the class name and id (saves the change into a JSON file).
Usage	destroy <class name> <id> --or-- .destroy()
-----	-----
all	Prints all string representation of all instances based or not on the class name.
Usage	By itself or all <class name> --or-- <class name>.all()
-----	-----
update	Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file).
Usage	update <class name> <id> <attribute name> "<attribute value>" ---or--- <class name>.update(<id>, <attribute name>, <attribute value>) --or-- <class name>.update(<id>, <dictionary representation>)
-----	-----
count	Retrieve the number of instances of a class.
Usage	<class name>.count()

