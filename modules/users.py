def list_users() -> list[dict[str, str]]:
    return [
        {"id": "1", "email": "admin@example.com", "role": "admin"},
        {"id": "2", "email": "staff@example.com", "role": "staff"},
    ]


def get_user(user_id: str) -> dict[str, str] | None:
    for user in list_users():
        if user["id"] == user_id:
            return user
    return None
