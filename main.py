from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Сошкина Полина Анатольевна"}

@app.get('/tools')
async def f_indexT():
    return "Не умею программировать"

@app.get('/users')
async def f_indexU():
    return "+79564374894"