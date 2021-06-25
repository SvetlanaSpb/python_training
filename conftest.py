# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
import json

# определяем глобальную переменную
fixture = None
target = None

@pytest.fixture
def app(request):
    #указываем что собираеися использовать глобальную переменную
    global fixture
    global target
    browser = request.config.getoption("--browser")
    #пишем проверку
    if target is None:
    #читаем файл джейсон
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        #функция которая инициализирует фикстуру создает объект класса aplication
        #при инициализации фикстуры нужно передавать параметр
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
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
    #хранить конфигурацию будем в формате джейсн
    parser.addoption("--target", action="store", default="target.json")

