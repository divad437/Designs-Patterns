# The bridge pattern is a structural pattern that lets you split a large class
# or a set of closely related classes into two separate hierarchies—abstraction
# and implementation—which can be developed independently of each other.

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        pass

    @abstractmethod
    def print_status(self) -> None:
        pass


class Radio(Device):
    def __init__(self):
        self.__on: bool = False
        self.__volume: int = 30
        self.__channel: int = 1

    def is_enabled(self) -> bool:
        return self.__on

    def enable(self) -> None:
        self.__on = True

    def disable(self) -> None:
        self.__on = False

    def get_volume(self) -> int:
        return self.__volume

    def set_volume(self, percent: int) -> None:
        if percent > 100:
            self.__volume = 100
        elif percent < 0:
            self.__volume = 0
        else:
            self.__volume = percent

    def get_channel(self) -> int:
        return self.__channel

    def set_channel(self, channel: int) -> None:
        self.__channel = channel

    def print_status(self) -> None:
        print(
            f"Radio is {'enabled' if self.__on else 'disabled'},"
            f"Current volume is {self.__volume},"
            f"Current channel is {self.__channel}"
        )


class Tv(Device):
    def __init__(self):
        self.__on: bool = False
        self.__volume: int = 30
        self.__channel: int = 1

    def is_enabled(self) -> bool:
        return self.__on

    def enable(self) -> None:
        self.__on = True

    def disable(self) -> None:
        self.__on = False

    def get_volume(self) -> int:
        return self.__volume

    def set_volume(self, percent: int) -> None:
        if percent > 100:
            self.__volume = 100
        elif percent < 0:
            self.__volume = 0
        else:
            self.__volume = percent

    def get_channel(self) -> int:
        return self.__channel

    def set_channel(self, channel: int) -> None:
        self.__channel = channel

    def print_status(self) -> None:
        print(
            f"Tv is {'enabled' if self.__on else 'disabled'},"
            f"Current volume is {self.__volume},"
            f"Current channel is {self.__channel}"
        )


class Remote(ABC):
    @abstractmethod
    def power(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def channel_down(self) -> None:
        pass

    @abstractmethod
    def channel_up(self) -> None:
        pass


class BasicRemote(Remote):
    def __init__(self, device: Device) -> None:
        self._device = device

    def power(self) -> None:
        print("Remote: power toggle")
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self) -> None:
        print("Remote: volume down")
        device_volume = self._device.get_volume()
        self._device.set_volume(device_volume - 1)

    def volume_up(self) -> None:
        print("Remote: volume up")
        device_volume = self._device.get_volume()
        self._device.set_volume(device_volume + 1)

    def channel_down(self) -> None:
        print("Remote: channel down")
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self) -> None:
        print("Remote: channel up")
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedRemote(BasicRemote):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def mute(self) -> None:
        print("Remote: mute")
        self._device.set_volume(0)


if __name__ == "__main__":
    print("Test with basic remote")
    radio = Radio()
    basic_remote = BasicRemote(radio)
    basic_remote.power()
    radio.print_status()
    basic_remote.volume_up()
    radio.print_status()
    basic_remote.volume_down()
    radio.print_status()
    basic_remote.channel_up()
    radio.print_status()
    basic_remote.channel_down()
    radio.print_status()
    print("\nTest with advanced remote")
    tv = Tv()
    advanced_remote = AdvancedRemote(tv)
    advanced_remote.power()
    tv.print_status()
    advanced_remote.volume_up()
    tv.print_status()
    advanced_remote.volume_down()
    tv.print_status()
    advanced_remote.channel_up()
    tv.print_status()
    advanced_remote.channel_down()
    tv.print_status()
    advanced_remote.mute()
    tv.print_status()
