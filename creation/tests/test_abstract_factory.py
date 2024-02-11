from abc import ABC

import pytest

from creation.abstract_factory import (
    Button,
    Checkbox,
    GuiApplication,
    GuiFactory,
    LinuxButton,
    LinuxCheckbox,
    LinuxGuiFactory,
    LinuxTextField,
    TextField,
    WindowsButton,
    WindowsCheckbox,
    WindowsGuiFactory,
    WindowsTextField,
)


class TestAbstractFactory:
    def test_create_ui_with_windows_gui_factory(self) -> None:
        factory: GuiFactory = WindowsGuiFactory()
        app = GuiApplication(factory)
        app.create_ui()
        app.paint()
        assert isinstance(app.button, WindowsButton)
        assert isinstance(app.checkbox, WindowsCheckbox)
        assert isinstance(app.text_field, WindowsTextField)

    def test_create_ui_with_linux_gui_factory(self) -> None:
        factory: GuiFactory = LinuxGuiFactory()
        app = GuiApplication(factory)
        app.create_ui()
        app.paint()
        assert isinstance(app.button, LinuxButton)
        assert isinstance(app.checkbox, LinuxCheckbox)
        assert isinstance(app.text_field, LinuxTextField)

    def test_unknow_os_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            os_name = "unknown"
            factory_mapping = {
                "nt": WindowsGuiFactory,
                "posix": LinuxGuiFactory,
            }
            factory = factory_mapping.get(os_name, None)
            if factory is None:
                raise ValueError(f"Unknown operating system {os_name}")

    def test_abstract_classes(self) -> None:
        assert issubclass(GuiFactory, ABC)
        assert issubclass(Button, ABC)
        assert issubclass(Checkbox, ABC)
        assert issubclass(TextField, ABC)

    def test_concrete_classes(self) -> None:
        assert issubclass(WindowsGuiFactory, GuiFactory)
        assert issubclass(LinuxGuiFactory, GuiFactory)
        assert issubclass(WindowsButton, Button)
        assert issubclass(LinuxButton, Button)
        assert issubclass(WindowsCheckbox, Checkbox)
        assert issubclass(LinuxCheckbox, Checkbox)
        assert issubclass(WindowsTextField, TextField)
        assert issubclass(LinuxTextField, TextField)
