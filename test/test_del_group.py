from model.group import Group
from random import randrange


def test_delete_some_group(app):
    # метод позволяет вычислить кол-во групп не загружая список инфо о каждой группе
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # добавляем случайность, генерируется целое число
    index = randrange (len(old_groups))
    # вспомогательный метод в качестве параметра номер группы для удаления
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups [index:index+1] = []
    assert old_groups == new_groups
