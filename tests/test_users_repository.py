from lib.users_repository import UsersRepository
from lib.users import Users



def test_get_all(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UsersRepository(db_connection)
    users = repository.all() 
    assert users == [
        Users(1, 'user_1@makers.com', '123453455555!'),
        Users(2, 'user_2@makers.com', '678944676787@'),
        Users(3, 'user_3@makers.com', 'abcdef222222$')
    ]

def test_new_user_created(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UsersRepository(db_connection)
    repository.new_user_created(Users(None, "h@mail.com", "123678?"))
    result = repository.all()
    assert result == [
        Users(1, 'user_1@makers.com', '123453455555!'),
        Users(2, 'user_2@makers.com', '678944676787@'),
        Users(3, 'user_3@makers.com', 'abcdef222222$'),
        Users(4, "h@mail.com", "123678?")
    ]
