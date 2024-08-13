def immutable(func):
    def wrapper(*args, **kwargs):
        raise AttributeError("Attempted to modify immutable object")

    return wrapper


class Immutable:
    """
    В начале определяем декоратор immutable, который принимает функцию func.
    Декоратор состоит из функции wrapper, которая вызывается вместо функции func, которую он оборачивает.
    Внутри wrapper вызывается исключение AttributeError с сообщением "Attempted to modify immutable object".

def immutable(func):
    def wrapper(*args, **kwargs):
        raise AttributeError("Attempted to modify immutable object")
    return wrapper
    
    Затем определяем класс Immutable, который создаёт неизменяемый объект.
    Класс имеет атрибут _value, который инициализируется в методе __init__. Атрибут __value не будет общедоступным,
    поскольку его имя начинается с символа 2 подчеркивания, но к нему можно обратиться через свойство value.

class Immutable:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self.__value
        
    В классе Immutable определен setter для свойства value, который помечен декоратором immutable.
    Это означает, что попытка установить новое значение для свойства value приведет к вызову функции-обёртки wrapper,
    определенной в декораторе immutable и следовательно, вызовет исключение AttributeError.

@value.setter
@immutable
def value(self, value):
    pass

    В конце, создается объект immutable_obj класса Immutable с начальным значением 42.

immutable_obj = Immutable(42)

    Таким образом, при попытке изменить значение атрибута value объекта immutable_obj,
    будет вызвано исключение AttributeError, и изменение не будет выполнено.

    """
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    @immutable
    def value(self, value):
        pass


if __name__ == "__main__":
    immutable_obj = Immutable(42)
    print(immutable_obj.value + 5)
    print(immutable_obj.value)
    immutable_obj.value += 5
    print(immutable_obj.value)
    Immutable.value += 42
    print(Immutable.value)
