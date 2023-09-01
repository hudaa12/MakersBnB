from lib.user_repository import UserRepository
from lib.user import User
from lib.space import Space
from lib.booking import Booking



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

def test_find_with_spaces_and_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    assert repository.find_with_spaces_and_bookings(1) == User(
        1, 'user_1@makers.com', '123453455555!', [
        Space(1, 'House_1', 'nice house', 150.00, '2023/01/01', '2023/10/01', 1)
        ], [Booking(3, '2023/9/20', True, 1, 3)])


def test_check_user_login(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user_id = repository.check_user_login('user_1@makers.com', '123453455555!')
    assert user_id == 1

def test_check_user_login_incorrect(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user_id = repository.check_user_login('user_1@makerss.com', '123453455555!')
    assert user_id == None

