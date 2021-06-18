# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        #функция которая инициализирует фикстуру создает объект класса aplication
        #при инициализации фикстуры нужно передавать параметр
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(password="secret", username="admin")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

#добавляем хук(зацепку)
def pytest_addoption(parser):
    #если параметр браузер не указан то по дефолту будет запускаться фаерфокс
    parser.addoption("--browser", action="store", default="firefox")

