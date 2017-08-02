from collections import Counter, OrderedDict, defaultdict, namedtuple, Sequence

# ==============Counter=============

s = 'aaaabbbccd'
count_s = Counter(s)
# {'a': 4, 'b': 3, 'c': 2, 'd': 1}
l = [2, 4, 2, 23, 2, 4, 5]
# {2: 3, 4: 2, 5: 1, 23: 1}


# ===========OrderedDict===============
d1 = dict([('a', 10), ('b', 20), ('c', 15)])
# d1 hava no order
d2 = OrderedDict([('a', 10), ('b', 20), ('c', 15)])
# d2 hava order
od = OrderedDict({"adsf": 23})
print(od)
# ==============defaultdict=================
df1 = defaultdict(int)
# df1['a'] is 0
df2 = defaultdict(lambda: 10)
df3 = defaultdict(list)


# ===============namedtuple=================
Student_ = namedtuple('Student', ['name', 'id', 'age'])


def Student(name, id=None, age=None):
    return Student_(name, id, age)

s1 = Student("jack", 23)


# ===============deque======================
