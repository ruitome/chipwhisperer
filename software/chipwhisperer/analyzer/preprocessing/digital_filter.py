#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
# All rights reserved.
#
# Author: Colin O'Flynn
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
#
#    Date         Author                Changes
#    -----------  --------------------  -----------------------------------
#    20-Jun-2016  marc                  Added "bandstop" filter option

from ._base import PreprocessingBase
from scipy import signal


class Filter(PreprocessingBase):
    """
    Generic filter, pulls in from SciPy for doing the actual filtering of things
    """
    _name = "Digital Filter"
    _description = "Frequency specific filter."

    def __init__(self, traceSource=None):
        PreprocessingBase.__init__(self, traceSource)
        self.importsAppend("import scipy as sp")
        self.getParams().addChildren([
            {'name':'Form', 'key':'form', 'type':'list', 'values':{"Butterworth":"sp.signal.butter"}, 'default':"sp.signal.butter", 'value':"sp.signal.butter", 'action':self.updateScript},
            {'name':'Type', 'key':'type', 'type':'list', 'values':["low", "high", "bandpass", "bandstop"], 'default':'low', 'value':'low', 'action':self.updateScript},
            {'name':'Critical Freq #1 (0-1)', 'key':'freq1', 'type':'float', 'limits':(0, 1), 'step':0.05, 'default':0.1, 'value':0.1, 'action':self.updateScript},
            {'name':'Critical Freq #2 (0-1)', 'key':'freq2', 'type':'float', 'limits':(0, 1), 'step':0.05, 'default':0.8, 'value':0.8, 'action':self.updateScript},
            {'name':'Order', 'key':'order', 'type':'int', 'limits':(1, 32), 'default':5, 'value':5, 'action':self.updateScript},
        ])
        self.updateScript()

    def setFilterForm(self, filtform=signal.butter):
        """Set the filter type in object"""
        self.filterForm = filtform

    def setFilterParams(self, form='low', freq=0.8, order=5):
        self.b, self.a = self.filterForm(order, freq, form)

    def updateScript(self, _=None):
        self.addFunction("init", "setEnabled", "%s" % self.findParam('enabled').getValue())
        
        ftype = self.findParam('type').getValue()
        freq1 = self.findParam('freq1').getValue()
        freq2 = self.findParam('freq2').getValue()
        
        if ftype == "bandpass" or ftype == "bandstop":
            self.findParam('freq2').show()
            freqs = "(%f, %f)" % (freq1, freq2)
        else:
            self.findParam('freq2').hide()
            freqs = "%f" % freq1

        self.addFunction("init", "setFilterForm", self.findParam('form').getValue())
        self.addFunction("init", "setFilterParams", "form='%s', freq=%s, order=%d" %
                         (ftype, freqs, self.findParam('order').getValue()))
   
    def getTrace(self, n):
        if self.enabled:
            trace = self._traceSource.getTrace(n)
            if trace is None:
                return None
            return signal.lfilter(self.b, self.a, trace)
        else:
            return self._traceSource.getTrace(n)
