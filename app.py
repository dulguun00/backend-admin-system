from fastapi import FastAPI, HTTPException, Query, status

from modules.auth import can_manage_users, can_view_reports
from modules.reports import get_summary_report
from modules.users import get_user, list_users


app = FastAPI(title="Backend Admin System Demo")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/users")
def users(role: str = Query(default="admin")) -> list[dict[str, str]]:
    if not can_manage_users(role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to manage users",
        )
    return list_users()


@app.get("/users/{user_id}")
def user_detail(user_id: str, role: str = Query(default="admin")) -> dict[str, str]:
    if not can_manage_users(role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to view this user",
        )
    user = get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@app.get("/reports/summary")
def report_summary(role: str = Query(default="manager")) -> dict[str, int]:
    if not can_view_reports(role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to view reports",
        )
    return get_summary_report()
