serial_port_tester is a Python GUI program for testing or monitoring the serial port signals. 

Links:
 * home: https://github.com/ponty/serial_port_tester
 * documentation: http://ponty.github.com/serial_port_tester

Features:
 - Python serial back-end: pySerial_ library (2.6)
 - following signals can be controled: RTS, DTR
 - following signals can be monitored: DSR, CTS, RI, DCD

Installation
=======================

General
----------

 * install Python_
 * install pip_
 * install pySerial_
 * install TraitsUI_
 * add user to dialout group
 
Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo apt-get install python-traitsui python-traits
    sudo apt-get install python-serial 
    sudo pip install -U pyserial   # 2.6 is needed


.. _python: http://www.python.org/
.. _pip: http://pip.openplans.org/
.. _pySerial: http://pyserial.sourceforge.net/
.. _TraitsUI: http://code.enthought.com/projects/traits_ui/


