from fastapi import FastAPI

app = FastAPI(
    title="TutorApp"
)


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'user', 'name': 'Alice'},
    {'id': 3, 'role': 'user', 'name': 'John'},
    {'id': 4, 'role': 'admin', 'name': 'Emma'},
    {'id': 5, 'role': 'user', 'name': 'Michael'}
]

@app.post("/user/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_name = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_name["name"] = new_name
    return {"status": 200, "data": current_name}