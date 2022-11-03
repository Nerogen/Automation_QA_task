class Animal:

    def __init__(self, name: str, color: str, voice: str) -> None:
        self.__name: str = name
        self.__color: str = color
        self.__voice: str = voice

    def get_voice(self) -> str:
        return f"It says {self.__voice}."

    @property
    def name(self) -> str:
        return self.__name

    @property
    def color(self) -> str:
        return self.__color

    @property
    def voice(self) -> str:
        return self.__voice

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @color.setter
    def color(self, new_color: str) -> None:
        self.__color = new_color

    @voice.setter
    def voice(self, new_voice: str) -> None:
        self.__voice = new_voice
