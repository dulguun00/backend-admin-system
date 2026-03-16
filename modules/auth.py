def can_view_reports(role: str) -> bool:
    return role in {"admin", "manager"}


def can_manage_users(role: str) -> bool:
    return role == "admin"
