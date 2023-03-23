from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def api_hello():
    return {"Message": "Hello universe"}

@app.get("/square")
def api_square(n : int):
    res = n * n
    return {"Square": res}

@app.get("/addtwo")
def api_add_two(x : int, y : int):
    res = x + y
    return {"AddTwo": res}

@app.get("/cube")
def api_cube(n : int):
    res = n ** 3
    return{"Number": n, "Result" : res}