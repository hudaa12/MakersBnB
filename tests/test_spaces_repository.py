from lib.spaces_repository import SpacesRepository
from lib.space import Space


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = SpacesRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space('House_1', 'nice house', 150.00, '01/01/2023', '01/10/2023', 1),
        Space('House_2', 'nice pool', 250.00, '01/04/2023', '01/09/2023', 2),
        Space('House_3', 'nice garden', 350.00, '01/06/2023', '01/11/2023', 3)
    ]
