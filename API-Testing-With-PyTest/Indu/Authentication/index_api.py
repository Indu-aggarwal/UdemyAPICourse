from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

# Init
app = FastAPI(debug=True)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token' : form_data.username + 'token'}

@app.get('/')
async def index(token: str = Depends(oauth2_schema)):
    return {'the_token' : token}


# Route
@app.get('/api/v1/student')
async def get_student():
    return{"students":1}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port="7000")



