from serial.tools.list_ports import comports # New in version 2.6.
from threading import Thread
from traits.api import Instance
from traits.has_traits import HasTraits
from traits.trait_types import Enum, Bool, Int
from traitsui.editors.boolean_editor import BooleanEditor
from traitsui.handler import Handler
from traitsui.item import Item
from traitsui.ui_info import UIInfo
from traitsui.view import View
import os
import serial
import time
import traceback


class BackgroundHandler (Handler):

    # The UIInfo object associated with the UI:
    info = Instance(UIInfo)

    # Is the demo currently running:
    running = Bool(True)

    # Is the thread still alive?
    alive = Bool(True)

    def init(self, info):
        self.info = info
        Thread(target=self._update).start()

    def closed(self, info, is_ok):
        self.running = False
        while self.alive:
            time.sleep(.05)

    def _update(self):
        try:
            while self.running:
                self.loop()
                time.sleep(0.1)
        except Exception:
            traceback.print_exc()
            os._exit(1)
        self.alive = False

    def loop(self):
        ''

__version__ = '0.0.0'


def readonly(name):
        return Item(name=name,
                    editor=BooleanEditor(),
                    enabled_when='0',
                    )


class Handler (BackgroundHandler):
    def loop(self):
        ''
        self.info.object.update()

ports = sorted([port for port, desc, hwid in sorted(comports())])
print ports


class BoardWrapper(HasTraits):
    port = Enum(ports)

    def _port_changed(self):
        if self.serialobj:
            self.serialobj.close()
            self.serialobj = None
        self.serialobj = serial.Serial(self.port)

    DCD = Bool(label='DCD (1)', desc='Data Carrier Detect')
#    RxD = String(label='RxD (2)')
#    TxD = String(label='TxD (3)')
    DTR = Bool(label='DTR (4)', desc='Data Terminal Ready')
#    GND = String(label='GND (5)')
    DSR = Bool(label='DSR (6)', desc='Data Set Ready')
    RTS = Bool(label='RTS (7)', desc='Request to Send')
    CTS = Bool(label='CTS (8)', desc='Clear To Send')
    RI = Bool(label='RI (9)', desc='Ring Indicator')

    serialobj = None
    update_interval = Int(100, desc='interval in msec')

    def update(self):
        if self.serialobj:
            self.DSR = self.serialobj.getDSR()
            self.CTS = self.serialobj.getCTS()
            self.RI = self.serialobj.getRI()
            self.DCD = self.serialobj.getCD()

            self.serialobj.setRTS(self.RTS)
            self.serialobj.setDTR(self.DTR)

        time.sleep(self.update_interval / 1000.0)

    traits_view = View(
        'port',

        '_',
        #
        readonly('DCD'),
#                       'RxD (2)',
#                       'TxD (3)',
        'DTR',
#                       'GND (5)',
        readonly('DSR'),
        'RTS',
        readonly('CTS'),
        readonly('RI'),


        buttons=['Undo', 'Revert', 'OK', 'Cancel'],
        kind='live',
        resizable=True,
        title='serial port tester',
        handler=Handler(),
    )


def main():
    '''
    '''

    obj = BoardWrapper()
    obj._port_changed()
    obj.configure_traits()

if __name__ == '__main__':
    main()
