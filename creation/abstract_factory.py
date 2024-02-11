import os
from abc import ABC, abstractmethod


# abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class TextField(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


# concrete Products
class WindowsButton(Button):
    def paint(self) -> None:
        print("You have created WindowsButton.")


class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created WindowsCheckbox.")


class WindowsTextField(TextField):
    def paint(self) -> None:
        print("You have created WindowsTextField.")


class LinuxButton(Button):
    def paint(self) -> None:
        print("You have created LinuxButton.")


class LinuxCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created LinuxCheckbox.")


class LinuxTextField(TextField):
    def paint(self) -> None:
        print("You have created LinuxTextField.")


class GuiFactory(ABC):
    """
    The abstract factory pattern provides a way to encapsulate
    a group of individual factories that have a common theme
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass


class WindowsGuiFactory(GuiFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_text_field(self) -> TextField:
        return WindowsTextField()


class LinuxGuiFactory(GuiFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

    def create_text_field(self) -> TextField:
        return LinuxTextField()


class Application:
    button: Button
    checkbox: Checkbox
    text_field: TextField

    def __init__(self, factory: GuiFactory):
        self.factory = factory

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        self.text_field = self.factory.create_text_field()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()
        self.text_field.paint()


if __name__ == "__main__":
    os_name = os.name
    factory: GuiFactory

    if os_name == "posix":
        factory = LinuxGuiFactory()
    elif os_name == "nt":
        factory = WindowsGuiFactory()
    else:
        raise ValueError("Unknown operating system")

    app = Application(factory)
    app.create_ui()
    app.paint()
