The AirBnB Clone Project

The goal of this project is deploy a clone of the AirBnB website. We will implement some of the features of the website. The complete project will comprise of the following upon completion

1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

2. A website (the front-end) that shows the final product to everybody: static and dynamic

3. A database or files that store data (data = objects)

4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


The Command Interpreter

The command interpreter is the first step towards building the full web application: AirBnB clone. The Command Interpreter will help to,

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

4. create the first abstracted storage engine of the project: File storage.

5. create all unittests to validate all our classes and storage engine


The command Interpreter will be the same as the Shell but limited to a specific use-case. It will be able to manage the objects of our project:

1. Create a new object (ex: a new User or a new Place)

2. Retrieve an object from a file, a database etc…

3. Do operations on objects (count, compute stats, etc…)

4. Update attributes of an object

5. Destroy an object

