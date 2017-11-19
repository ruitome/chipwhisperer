#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
# All rights reserved.
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
import random
from chipwhisperer.common.utils import util
from _base import AcqKeyTextPattern_Base

try:
    from Crypto.Cipher import AES
except ImportError:
    logging.warn('No AES Module, Using rand() instead!')
    AES = None

class AcqKeyTextPattern_CRITTest(AcqKeyTextPattern_Base):
    _name = "CRI T-Test"
    _description = "Welsch T-Test with random/fixed plaintext."

    def __init__(self, target=None):
        AcqKeyTextPattern_Base.__init__(self)
        self._interleavedPlaintext = []
        self._key = []

        self.getParams().addChildren([
            {'name':'Encryption Key', 'key':'key', 'type':'str', 'value':"", 'readonly':True},
            {'name':'Interleaved Plaintext', 'key':'text', 'type':'str', 'value':"", 'readonly':True},
        ])

        self.setTarget(target)

    def _initPattern(self):
        pass

    def initPair(self):
        length = self.keyLen()
        if length <= 32:
            self._key = util.hexStrToByteArray("01 23 45 67 89 ab cd ef 12 34 56 78 9a bc de f0 23 45 67 89 ab cd ef 01 34 56 78 9a bc de f0 12")[:length]
        else:
            raise ValueError("Invalid key length: %d bytes" % length)
        self.findParam("key").setValue(" ".join(["%02X"%b for b in self._key]), init=True)

        self._textin1 = util.hexStrToByteArray("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")

        if length == 16:
            self._interleavedPlaintext = util.hexStrToByteArray("da 39 a3 ee 5e 6b 4b 0d 32 55 bf ef 95 60 18 90")
        elif length == 24:
            self._interleavedPlaintext = util.hexStrToByteArray("da 39 a3 ee 5e 6b 4b 0d 32 55 bf ef 95 60 18 88")
        elif length == 32:
            self._interleavedPlaintext = util.hexStrToByteArray("da 39 a3 ee 5e 6b 4b 0d 32 55 bf ef 95 60 18 95")
        else:
            raise ValueError("Invalid key length: %d bytes" % length)
        self.findParam("text").setValue(" ".join(["%02X" % b for b in self._interleavedPlaintext]), init=True)

        self.group1 = True

    def newPair(self):
        if self.group1:
            self.group1 = False
            self._textin = self._textin1

            if AES is not None:
                cipher = AES.new(str(self._key), AES.MODE_ECB)
                self._textin1 = bytearray(cipher.encrypt(str(self._textin1)))
            else:
                self._textin1 = bytearray(16)
                for i in range(0, 16):
                    self._textin1[i] = random.randint(0, 255)
        else:
            self.group1 = True
            self._textin = self._interleavedPlaintext

        # Check key works with target
        self.validateKey()

        return (self._key, self._textin)
