from fastapi import FastAPI, Depends
from .api import accounts
from .core.config import engine, get_db
from sqlalchemy.orm import Session
from .db import models
from .db.schemas import AccountSchema
from typing import List


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.on_event('startup')
async def on_startup():
    pass
    

@app.get('/get-accounts')
async def get_data():
    _accounts = accounts.get_all_accounts()
    return _accounts


@app.post('/add-accounts')
async def add_account(new_accounts: List[AccountSchema], db: Session = Depends(get_db)):
    results = {}
    
    for _new_account in new_accounts:
        _account = accounts.create_new_account(_new_account.login, _new_account.password, db)
        results[_account.id] = _account
        
    return {'success': results}
