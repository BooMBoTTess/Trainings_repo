class Thing():
    def __init__(self, name):
        self.name = name
        self.verbs = {'is_a': IsA, 'is_not_a': IsNotA, 'is_the': IsThe,
                      'and_the': IsThe, 'being_the': IsThe, 'has': Has, 'having': Has,
                      'can': Can}
        print(self.__class__, 'init', name, self.name)

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item, self.name)
        if item in self.verbs:
            return self.verbs[item](self)
        elif item == f'is_{self.name}':
            return True
        return '123'

    def __setattr__(self, key, value):
        print(self.__class__, 'setattr', key, value)
        if key == 'name':
            if value[-1] == 's':
                value = value[:-1]
        super().__setattr__(key, value)
        return value

    def __get__(self, instance, owner):
        return str(getattr(self, 'name'))


class ThingTuple(Thing, tuple):
    def __init__(self, thing):

        self.obj = thing
        self.verbs = {'each': self.each}

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        if item in self.verbs:
            return self.verbs[item](self)
        return item

    def __setattr__(self, key, value):
        print(self.__class__, 'setattr', key, value)
        self.__dict__[key] = value
        return value

    def __repr__(self):
        return 'res'

    def each(self, item):
        for i in range(len(self.obj)):
            item(self.obj[i])
        return self

class IsA:
    def __init__(self, who):
        self.who = who

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        setattr(self.who, f'is_a_{item}', True)
        return self.who

class IsNotA:
    def __init__(self, who):
        self.who = who

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        setattr(self.who, f'is_a_{item}', False)
        return self.who

class IsThe:
    def __init__(self, who):
        self.who = who

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        verb = State(self.who, item)
        return verb


class State:
    def __init__(self, who, state):
        print(self.__class__, 'init', who, state)
        self.who = who
        self.state = state

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        t = Thing(item)
        setattr(self.who, self.state, item)
        return self.who

class Has:
    def __init__(self, who):
        self.who = who


    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)

        return item

    def __call__(self, num):
        print(self.__class__, 'call', num)
        h = Hasing(self.who, num)
        return h

class Hasing:
    def __init__(self, who, num):
        self.who = who
        self.num = num

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        if self.num == 1:
            t = Thing(item)
        else:
            t = ThingTuple([Thing(item) for _ in range(self.num)])
            setattr(t, 'name', item)
        setattr(self.who, item, t)
        return t

class Can:
    def __init__(self, who):
        self.who = who

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        v = Verb(self.who, item)
        return v

class Verb:
    def __init__(self, who, what):
        self.who = who
        self.what = what

    def __getattr__(self, item):
        print(self.__class__, 'getattr', item)
        return self.who

    def __call__(self, method, archive_name):
        print(self.__class__, 'call', method, archive_name)
        setattr(self.who, self.what, method)
        return self.who

if __name__ == '__main__':
    bob = Thing('bob')
    print(bob.name)
    bob.is_a.dog
    print(bob.is_a_dog)

    print('-'*100)

    jane = Thing('Jane')
    print(jane.name) # => 'Jane'
    jane.is_a.person
    print(jane.is_a_person) # => True

    print('-'*100)

    jane.is_a.woman.is_not_a.man
    print(jane.is_a_woman)
    print(jane.is_a_man)

    print(bob.name)
    # print(bob.is_a_woman)
    print('-' * 100)

    legs = jane.has(2).legs
    print('-' * 100)
    print(len(legs))
    print(isinstance(legs, Thing))
    print(jane.legs[0])
    print(legs)
    assert isinstance(legs, Thing) == True  # => True
    print(isinstance(jane.legs[0], Thing))  # => True
    print('-' * 100)

    jane.has(1).head.is_the.on_top_of.body
    print(isinstance(jane.head, Thing) ) # => True
    print(jane.head.on_top_of ) # => "body"
    print('-' * 100)

    jane.has(2).arms
    jane.has(2).hands.each(lambda h:h.having(5).fingers)
    print(jane.arms[0].name, '*' * 20)
    print(jane.arms.name, '*' * 20)
    print('-' * 100)

    jane.has(4).members.each(lambda m: m.having(2).segments).each(lambda m: m.having(1).joint)
    print('-' * 100)

    jane.is_the.parent_of.joe
    print(jane.parent_of)
    assert jane.parent_of == 'joe'
    print('-' * 100)

    jane.has(2).eyes.each(lambda thing: thing.being_the.color.green.having(1).pupil.being_the.color.black)
    print('-' * 100)


    def method(self_: Thing, phrase: str):
        return f"{self_.name} says: {phrase}"


    jane.can.speak(method, "spoke")

    jane.speak("hello")  # => "Jane says: hello"
    jane.speak("bye")  # => "Jane says: bye"

    # print('-'*50)
    # legs = jane.has(2).legs
    # print('-' * 50)
    # print(legs)
    # print(jane.legs)
