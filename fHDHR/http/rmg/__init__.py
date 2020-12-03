
from .rmg_ident_xml import RMG_Ident_XML
from .device_xml import RMG_Device_XML
from .devices_discover import RMG_Devices_Discover
from .devices_probe import RMG_Devices_Probe
from .devices_devicekey import RMG_Devices_DeviceKey


class fHDHR_RMG():

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

        self.rmg_ident_xml = RMG_Ident_XML(fhdhr)
        self.device_xml = RMG_Device_XML(fhdhr)
        self.devices_discover = RMG_Devices_Discover(fhdhr)
        self.devices_probe = RMG_Devices_Probe(fhdhr)
        self.devices_devicekey = RMG_Devices_DeviceKey(fhdhr)