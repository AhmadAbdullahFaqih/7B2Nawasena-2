from fastapi import FastAPI
import model
from config import engine
import router
model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get('/index')
async def home():
    return 'welcome home'

app.include_router(router.router, prefix='/car',tags=['car'])