from abc import ABC, abstractmethod


class Car:
    def __init__(self, engine: float = 0, transmission: bool = False, body: bool = False):
        self._engine = engine
        self._transmission = transmission
        self._body = body

    def __str__(self) -> str:
        result = self.__class__.__name__
        result += f"\nEngine:{self._engine}"
        if self._transmission:
            result += f"\nTransmission:{self._transmission}"
        if self._body:
            result += f"\nBody:{self._body}"
        return result

class SedanBuilder():
    def __init__(self):
        self._params = {}
        self.reset()

    def reset(self):
        self._params = {"engine": 0,
                        "transmission": False,
                        "body": False}

    def set_engine(self, engine: float):
        self._params["engine"] = engine
        return self

    def set_transmission(self):
        self._params["transmission"] = True
        return self

    def set_body(self):
        self._params["body"] = True
        return self

    def result(self):
        return Car(**self._params)


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        return (self.builder.set_body()
                .set_engine(1.6)
                .set_transmission()
                .result()
                )


sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)
