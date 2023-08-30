from lib.user_repository import UserRepository
from lib.user import User



def test_get_all(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    users = repository.all() 
    assert users == [
        User(1, 'user_1@makers.com', '123453455555!'),
        User(2, 'user_2@makers.com', '678944676787@'),
        User(3, 'user_3@makers.com', 'abcdef222222$')
    ]

def test_new_user_created(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "h@mail.com", "123678?"))
    result = repository.all()
    assert result == [
        User(1, 'user_1@makers.com', '123453455555!'),
        User(2, 'user_2@makers.com', '678944676787@'),
        User(3, 'user_3@makers.com', 'abcdef222222$'),
        User(4, "h@mail.com", "123678?")
    ]
