class message_handler:
    handle_detection = None
    def __init__(self):
        self.handlers_list = {cls.handle_detection: cls for cls in message_handler.__subclasses__()}

    def foo(self, handler_name: str):
        return self.handlers_list[handler_name].foo(self)

    def set_handler(self, handler):
        return handler


class message_hello_handle(message_handler):
    handle_detection = 'Привет'
    def foo(self):
        return "hello"


class message_goodbye_handler(message_handler):
    handle_detection = 'Пока'
    def foo(self):
        return 'goodbye'


if __name__ == '__main__':
    a = message_handler()
    print(a.foo('Привет'))
