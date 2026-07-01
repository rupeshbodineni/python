from fastapi import FastAPI

app=FastAPI()
users=[]


@app.get()
def get_users():
    return users

@app.post()
def add_user():
    for user in users:
        users.append=user
        return "user added successfully"
    else:
        raise