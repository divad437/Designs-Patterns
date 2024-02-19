import pytest

from structural.bridge import AdvancedRemote, BasicRemote, Device, Radio, Remote, Tv


class TestBridgePattern:
    def test_can_not_instantiate_device_abstract_class(self):
        with pytest.raises(TypeError):
            Device()

    def test_create_radio_divice(self):
        radio = Radio()
        assert radio.is_enabled() is False
        assert radio.get_volume() == 30
        assert radio.get_channel() == 1
        assert radio.enable() is None
        assert radio.disable() is None
        assert radio.set_volume(10) is None
        assert radio.set_channel(10) is None
        assert radio.print_status() is None

    def test_radio_is_instance_of_device(self):
        radio = Radio()
        assert isinstance(radio, Device)

    def create_tv_divice(self):
        tv = Tv()
        assert tv.is_enabled() is False
        assert tv.get_volume() == 30
        assert tv.get_channel() == 1
        assert tv.enable() is None
        assert tv.disable() is None
        assert tv.set_volume(10) is None
        assert tv.set_channel(10) is None
        assert tv.print_status() is None

    def test_tv_is_instance_of_device(self):
        tv = Tv()
        assert isinstance(tv, Device)

    def test_can_not_instantiate_remote_abstract_class(self):
        with pytest.raises(TypeError):
            Remote()

    def test_basic_remote_instance_of_remote(self):
        tv = Tv()
        basic_remote = BasicRemote(tv)
        assert isinstance(basic_remote, Remote)

    def test_create_basic_remote(self):
        radio = Radio()
        basic_remote = BasicRemote(device=radio)
        assert basic_remote.power() is None
        assert basic_remote.volume_down() is None
        assert basic_remote.volume_up() is None
        assert basic_remote.channel_down() is None
        assert basic_remote.channel_up() is None

    def test_basic_remote_can_power_on_device(self):
        radio = Radio()
        basic_remote = BasicRemote(device=radio)
        basic_remote.power()
        assert radio.is_enabled() is True

    def test_basic_remote_can_power_off_device(self):
        tv = Tv()
        tv.enable()
        basic_remote = BasicRemote(device=tv)
        basic_remote.power()
        assert tv.is_enabled() is False

    def test_basic_remote_can_volume_down_device_with_default_values(self):
        radio = Radio()
        basic_remote = BasicRemote(device=radio)
        basic_remote.volume_down()
        assert radio.get_volume() == 29

    def test_basic_remote_can_volume_down_with_min_value(self):
        tv = Tv()
        tv.set_volume(0)
        basic_remote = BasicRemote(device=tv)
        basic_remote.volume_down()
        assert tv.get_volume() == 0

    def test_basic_remote_can_volume_up_device_with_default_values(self):
        radio = Radio()
        basic_remote = BasicRemote(device=radio)
        basic_remote.volume_up()
        assert radio.get_volume() == 31

    def test_basic_remote_can_volume_up_with_max_value(self):
        tv = Tv()
        tv.set_volume(100)
        basic_remote = BasicRemote(device=tv)
        basic_remote.volume_up()
        assert tv.get_volume() == 100

    def test_basic_remote_can_channel_down_with_default(self):
        tv = Tv()
        basic_remote = BasicRemote(device=tv)
        basic_remote.channel_down()
        assert tv.get_channel() == 0

    def test_basic_remote_can_channel_down_with_custum(self):
        radio = Radio()
        radio.set_channel(10)
        basic_remote = BasicRemote(device=radio)
        basic_remote.channel_down()
        assert radio.get_channel() == 9

    def test_basic_remote_can_channel_up_with_default(self):
        tv = Tv()
        basic_remote = BasicRemote(device=tv)
        basic_remote.channel_up()
        assert tv.get_channel() == 2

    def test_basic_remote_can_channel_up_with_custum(self):
        radio = Radio()
        radio.set_channel(10)
        basic_remote = BasicRemote(device=radio)
        basic_remote.channel_up()
        assert radio.get_channel() == 11

    def test_create_advanced_remote(self):
        radio = Radio()
        advanced_remote = AdvancedRemote(device=radio)
        assert advanced_remote.mute() is None
        assert advanced_remote.power() is None
        assert advanced_remote.volume_down() is None
        assert advanced_remote.volume_up() is None
        assert advanced_remote.channel_down() is None
        assert advanced_remote.channel_up() is None

    def test_advanced_remote_can_mute_device(self):
        radio = Radio()
        advanced_remote = AdvancedRemote(device=radio)
        advanced_remote.mute()
        assert radio.get_volume() == 0
