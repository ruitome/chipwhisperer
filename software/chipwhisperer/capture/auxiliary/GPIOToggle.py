#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, NewAE Technology Inc
# All rights reserved.
#
# Authors: Colin O'Flynn
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================
import logging
import time
from _base import AuxiliaryTemplate
from chipwhisperer.common.utils import timer
from chipwhisperer.common.api.CWCoreAPI import CWCoreAPI
from chipwhisperer.common.utils import util


class GPIOToggle(AuxiliaryTemplate):
    _name = 'GPIO Toggle'

    def __init__(self):
        AuxiliaryTemplate.__init__(self)
        self.pin = None
        self.lastPin = None
        self.getParams().addChildren([
                 {'name':'GPIO Pin', 'type':'list', 'key':'gpiopin', 'values':{'TargetIO1':0, 'TargetIO2':1, 'TargetIO3':2, 'TargetIO4':3}, 'value':2, 'action':self.settingsChanged},
                 {'name':'Standby State', 'type':'list', 'key':'inactive', 'values':{'High':True, 'Low':False}, 'value':False, 'action':self.settingsChanged},
                 {'name':'Toggle Length', 'type':'int', 'key':'togglelength', 'limits':(0, 10E3), 'value':250, 'suffix':'mS', 'action':self.settingsChanged},
                 {'name':'Post-Toggle Delay', 'type':'int', 'key':'toggledelay', 'limits':(0, 10E3), 'value':250, 'suffix':'mS', 'action':self.settingsChanged},
                 {'name':'Trigger', 'type':'list', 'key':'triggerloc', 'values':{'Campaign Init':0, 'Trace Arm':1, 'Trace Done':2, 'Campaign Done':3}, 'value':2, 'action':self.settingsChanged},
                 {'name':'Toggle Now', 'type':'action', 'action':self.trigger}
        ])
        self.settingsChanged()

    def settingsChanged(self, ignored=None):
        self.pin = self.findParam('gpiopin').getValue()
        self.standby = self.findParam('inactive').getValue()
        self.triglength = self.findParam('togglelength').getValue() / 1000.0
        self.postdelay = self.findParam('toggledelay').getValue() / 1000.0
        self.triglocation = self.findParam('triggerloc').getValue()

    def checkMode(self):
        cwa = CWCoreAPI.getInstance().getScope().advancedSettings.cwEXTRA

        if self.pin != self.lastPin:
            # Turn off last used pin
            if self.lastPin:
                cwa.setTargetIOMode(IONumber=self.lastPin, setting=0)

            # Setup new pin
            cwa.setTargetIOMode(IONumber=self.pin, setting=cwa.IOROUTE_GPIOE)

            # Don't do this again
            self.lastPin = self.pin

    def nonblockingSleep_done(self):
        self._sleeping = False

    def nonblockingSleep(self, stime):
        """Sleep for given number of seconds (~50mS resolution), but don't block GUI while we do it"""
        timer.Timer.singleShot(stime * 1000, self.nonblockingSleep_done)
        self._sleeping = True
        while(self._sleeping):
            time.sleep(0.01)
            util.updateUI()

    def trigger(self, _=None):
        logging.info('AUXIO: Trigger pin %d' % self.pin)
        self.checkMode()
        CWCoreAPI.getInstance().getScope().advancedSettings.cwEXTRA.setGPIOState(state=(not self.standby), IONumber=self.pin)
        self.nonblockingSleep(self.triglength)
        CWCoreAPI.getInstance().getScope().advancedSettings.cwEXTRA.setGPIOState(state=self.standby, IONumber=self.pin)
        self.nonblockingSleep(self.postdelay)

    def captureInit(self):
        self.checkMode()
        CWCoreAPI.getInstance().getScope().advancedSettings.cwEXTRA.setGPIOState(state=self.standby, IONumber=self.pin)

        if self.triglocation == 0:
            self.trigger()

    def captureComplete(self):
        if self.triglocation == 3:
            self.trigger()

    def traceArm(self):
        if self.triglocation == 1:
            self.trigger()

    def traceDone(self):
        if self.triglocation == 2:
            self.trigger()

    def testToggle(self):
        pass
