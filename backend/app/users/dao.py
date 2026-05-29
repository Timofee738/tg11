from app.dao.base import BaseDao
from app.users.model import Users

class UsersDao(BaseDao):
    model = Users

