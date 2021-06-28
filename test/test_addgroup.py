from model.group import Group


#сценарий
def test_add_group(app, json_groups):
    #переменная групп полуает знаение которое задано в каестве параметра
    group = json_groups
    #загружаем список групп
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




