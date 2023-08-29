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
    repository.create(Users(None, "h@mail.com", "123678?"))
    result = repository.all()
    assert result == [
        Users(1, 'user_1@makers.com', '123453455555!'),
        Users(2, 'user_2@makers.com', '678944676787@'),
        Users(3, 'user_3@makers.com', 'abcdef222222$'),
        Users(4, "h@mail.com", "123678?")
    ]

def test_password_checker_correct_length(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UsersRepository(db_connection)
    result = repository.new_user_created("new_user@makers.com", "1234567!")
    assert result == True


# def test_password_checker_error():
#     example = PasswordChecker()
#     with pytest.raises(Exception) as e:
#         example.check("1234")
#     error_message = str(e.value)
#     assert error_message == "Invalid password, must be 8+ characters."