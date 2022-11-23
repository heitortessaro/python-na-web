# python-na-web

Repository to follow the creation of an API based on python frameworks. The classes were part of Trybe Web Development Course.

## Configuration Steps

### Configuring the environment

1. Create virtual enviroment: python3 -m venv .venv
2. Activate virtual enviroment: source .venv/bin/activate
3. Install dependencies: python3 -m pip install -r dev-requirements.txt

### Testing the fastapi

1. Create a base file
2. Use uvicorn to run the service: uvicorn src.main:app --reload
3. Access the running page
4. Access the documentation adding "/docs" to the provided address

## Information

Python implements web servers using two patterns WSGI and ASGI. The Django frameworks uses the WSGI, while the fastapi uses the ASGI.

Like WSGI, ASGI describes a common interface between a Python web application and the web server. Unlike WSGI, ASGI allows multiple, asynchronous events per application. Plus, ASGI supports both sync and async apps. [source](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi5z7y0hsX7AhUyqZUCHY2OAgAQFnoECBUQAw&url=https%3A%2F%2Fwww.infoworld.com%2Farticle%2F3658336%2Fasgi-explained-the-future-of-python-web-development.html&usg=AOvVaw3SSPcozVPw3xmb-SRYKqps)

## References

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [SQLModel](https://sqlmodel.tiangolo.com/): SQLModel is a library for interacting with SQL databases from Python code, with Python objects.
