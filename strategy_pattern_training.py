class message_handler:
    """
    Класс фабрики, который выдает по строке экземляры классов своих детей.
    Если ребенка нет, то он просто вернет себя (можно сделать любой другой вывод)
    Чтобы расширить количество классов, которые он создает, нужно  создать
    ребенка и указать ему handle_detection в качестве переменной, они являются ключами словаря
    """

    handle_detection = None

    def __init__(self):
        self.handlers_list = {cls.handle_detection: cls for cls in message_handler.__subclasses__()}
        self.a = 'factory'

    def create_class(self, handler_name: str):
        if handler_name not in self.handlers_list.keys():
            return message_handler()
        return self.handlers_list[handler_name]()


class message_hello_handle(message_handler):
    handle_detection = 'Привет'

    def __init__(self):
        self.a = 'imhelloclass'

    def foo(self):
        return "hello"


class message_goodbye_handler(message_handler):
    handle_detection = 'Пока'

    def __init__(self):
        self.a = 'imdeleteclass'

    def foo(self):
        return 'goodbye'


if __name__ == '__main__':
    factory = message_handler()
    hiclass = factory.create_class('Привет')
    print(hiclass.a)
    hiclass = factory.create_class('Пока')
    print(hiclass.a)
    hiclass = factory.create_class('мурмур')
    print(hiclass.a)
