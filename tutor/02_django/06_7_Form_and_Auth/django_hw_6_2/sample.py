class Person:
    def __init__(self, info={'name': '', 'age': ''}):
        self.name = info['name']
        self.age = info['age']

p1 = Person()
print(f'인자 없이 만든 p1 인스턴스는 아무런 정보 없이 만들어진다.')
print(p1.name)
info = {
    'name': '홍길동',
    'age': 23
}
p2 = Person(info)
print(p2.name)