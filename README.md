# SanjayJindal_Beckend
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
It is designed to be easy to use and to provide high performance for building production-ready APIs.

FastAPI uses the latest advances in Python type hints and async/await syntax to provide code autocompletion and validation,making it easier to write correct, 
understandable, and maintainable code. It is built on top of the Starlette framework for the asynchronous HTTP server and uses Pydantic for data validation 
and serialization.

FastAPI is designed to be easy to use, with a simple and intuitive API that makes it easy to define endpoints, query parameters, and request/response models.
It also provides built-in support for popular API documentation tools like Swagger UI and ReDoc.

Overall, FastAPI is a great choice for building modern and high-performance APIs with Python.

Firstly  import fast API and after installing fast api through pip install and with it we import necessary other imports and we import  basemodel because 
we need to make the pattern of dict in this regard we will take request

app=fast API it basically initialise fast api in variable called app
As given in assignment we can add any db so we are using mock database in which there is json structure which has only two data and two rows 
and the necessary field given in assignment

then we add trade and trade detail json as given in assignment and according to that we have establish the mock database
 So we have first API list rate which is in the root we can open it on directly with localhost its doing two things first we can list out the list that if we directly 
 search with slash we can list out everything and can get every data present in mock data and print every rows 
 and another thing is we use (slash question mark search equal to)  to search anything then the  given  searching  field given in list trades we will match 
 in it so basically if we write search = boxsmith it will match boxsmith with field and that particular row as output otherwise it won't do anything
 So listAPI has two things firstly it will return return everything and if we are giving query parameter it will return return searched value 

Another API we have for single trade to get value for single trade
