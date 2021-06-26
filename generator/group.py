from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys

#параметризуем данные
try:
    opts, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f=a

#делаем генератор тестовых случайных данных (код создания тестовых данных)
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

#дописываем код, который сохранит сгенерированные данные в файл
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
#открываем его на запись
with open(file, "w") as out:
    #dumps функция превращает данные в строку в формате джейсн
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))