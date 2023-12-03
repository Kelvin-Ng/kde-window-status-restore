#!/usr/bin/env python3

import subprocess
import dbus
import dbus.service
import os
import signal
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import sys
import os

SCRIPT_NAME = 'KdeWindowStatusRestore'

def get_xdg_data_home():
    xdg_data_home = os.getenv('XDG_DATA_HOME')
    if xdg_data_home is None:
        xdg_data_home = os.getenv('HOME') + '/.local/share'
    return xdg_data_home

def get_data_path():
    return get_xdg_data_home() + '/kde-window-status-restore'

class KdeWindowStatusRestore:
    def __init__(self, is_restore):
        DBusGMainLoop(set_as_default=True)
        self.sigCount = 0
        self.loop = GLib.MainLoop()
        self.bus = dbus.SessionBus()

        script_file_name = 'save'
        if is_restore:
            script_file_name = 'restore'

        signal.signal(signal.SIGINT, self.cleanup)
        self.script_id = self.dbus_send(
            service='org.kde.KWin', 
            path='/Scripting', 
            interface='org.kde.kwin.Scripting'
        ).loadScript(os.path.dirname(os.path.abspath(__file__)) + '/' + script_file_name + '.js', SCRIPT_NAME, signature='ss')

        if int(self.script_id) > -1:
            self.dbus_listen()
            self.dbus_send(
                service='org.kde.KWin', 
                path='/' + str(self.script_id), 
                interface='org.kde.kwin.Script'
            ).run()

            self.dbus_wait()

        self.cleanup()
            
    def cleanup(self, signal=None, frame=None):
        if self.sigCount == 0:
            self.sigCount+=1
            self.dbus_send(
                service='org.kde.KWin', 
                path='/Scripting', 
                interface='org.kde.kwin.Scripting'
            ).unloadScript(SCRIPT_NAME)

        if signal is not None:
            exit()
        
    
    def dbus_listen(self):
        self.DBusListen(self)

    def dbus_wait(self):
        self.loop.run()

    def dbus_send(self, service, path, interface ):
        obj = self.bus.get_object(service, path)
        return dbus.Interface(obj, interface)

    class DBusListen(dbus.service.Object):
        def __init__(self, caller):
            self.caller = caller
            self.loop = caller.loop
            bus = dbus.SessionBus()
            bus.request_name('org.kde.KWin.Script.' + SCRIPT_NAME)
            bus_name = dbus.service.BusName('org.kde.KWin.Scripting', bus=bus)
            dbus.service.Object.__init__(self, bus_name, '/callback')

        @dbus.service.method(dbus_interface="org.kde.kwin.Script",
                             in_signature="", out_signature="s")
        def Read(self):
            with open(get_data_path() + '/saved.txt', 'r') as f:
                return f.read()

        @dbus.service.method(dbus_interface="org.kde.kwin.Script",
                             in_signature="s", out_signature="")
        def Save(self, res):
            self.caller.cleanup()

            with open(get_data_path() + '/saved.txt', 'w') as f:
                f.write(res)

            self.loop.quit()

        @dbus.service.method(dbus_interface="org.kde.kwin.Script",
                             in_signature="", out_signature="")
        def Finish(self):
            self.caller.cleanup()

            self.loop.quit()

if __name__ == '__main__':
    if sys.argv[1] == 'save':
        KdeWindowStatusRestore(False)
    else:
        KdeWindowStatusRestore(True)

