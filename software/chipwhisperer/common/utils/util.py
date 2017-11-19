#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, NewAE Technology Inc
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

import ast
import collections
import os.path
import shutil
import weakref
import numpy as np

try:
    # OrderedDict is new in 2.7
    from collections import OrderedDict
    DictType = OrderedDict
except ImportError:
    DictType = dict


def getRootDir():
    path = os.path.join(os.path.dirname(__file__), "../../../")
    return os.path.normpath(path)


def copyFile(source, destination, keepOriginals = True):
    if keepOriginals:
        shutil.copy2(source, destination)
    else:
        shutil.move(source, destination)


def strippedName(fullFileName):
    (filepath, filename) = os.path.split(fullFileName)
    (base, toplevel) = os.path.split(filepath)
    return toplevel + "/" + filename


def appendAndForwardErrorMessage(msg, e):
    raise type(e)(msg + "\n  -> " + str(e))


def list2hexstr(data, delim='', prefix=''):
    """
    Convert a list of integers to a hex string, with optional deliminators/prefix

    delim is inserted between each list item

    prefix is inserted infront of each item (including first item)
    """

    rstr = ["%02x" % t for t in data]
    rstr = (delim + prefix).join(rstr)
    rstr = prefix + rstr
    return rstr


def hexstr2list(data):
    """Convert a string with hex numbers into a list of numbers"""

    data = str(data)

    newdata = data.lower()
    newdata = newdata.replace("0x", "")
    newdata = newdata.replace(",", "")
    newdata = newdata.replace(" ", "")
    newdata = newdata.replace("[", "")
    newdata = newdata.replace("]", "")
    newdata = newdata.replace("(", "")
    newdata = newdata.replace(")", "")
    newdata = newdata.replace("{", "")
    newdata = newdata.replace("}", "")
    newdata = newdata.replace(":", "")
    newdata = newdata.replace("-", "")

    datalist = [int(newdata[i:(i + 2)], 16) for i in range(0, len(newdata), 2)]

    return datalist


def strListToList(strlist):
    """
    Convert string in form of '"[33, 42, 43]", "[24, 43, 4]"'
    into a normal list.
    """

    strlist = strlist.replace('"', '')
    strlist = strlist.replace("'", "")
    try:
        listeval = ast.literal_eval(strlist)
        return listeval
    except ValueError:
        raise ValueError("Failed to convert %s to list" % (strlist))


def convert_to_str(data):
    """
    Converts all dictionary elements to string type - similar to what ConfigObj will
    be doing when it saves and loads the data.
    """
    if isinstance(data, collections.Mapping):
        return dict(map(convert_to_str, data.iteritems()))
    elif isinstance(data, collections.Iterable) and not isinstance(data, basestring):
        return type(data)(map(convert_to_str, data))
    else:
        return str(data)


def hexStrToByteArray(hexStr):
    ba = bytearray(hexstr2list(hexStr))
    return ba


def binarylist2bytearray(bitlist, nrBits=8):
    ret = []
    pos = 0
    while pos <= len(bitlist) - nrBits:
        out = 0
        for bit in range(nrBits):
            out = (out << 1) | bitlist[pos + bit]
        ret.append(out)
        pos += nrBits
    return ret


def bytearray2binarylist(bytes, nrBits=8):
    init = np.array([], dtype=bool)
    for byte in bytes:
        init = np.concatenate((init, np.unpackbits(np.uint8(byte))[8 - nrBits:]), axis=0)
    return init


def getPyFiles(dir, extension=False):
    scriptList = []
    if os.path.isdir(dir):
        for fn in os.listdir(dir):
            fnfull = dir + '/' + fn
            if os.path.isfile(fnfull) and fnfull.lower().endswith('.py') and (not fnfull.endswith('__init__.py')) and (not fn.startswith('_')):
                if extension:
                    scriptList.append(fn)
                else:
                    scriptList.append(os.path.splitext(fn)[0])
    return scriptList

def _make_id(target):
    if hasattr(target, '__func__'):
        return (id(target.__self__))
    return id(target)


class Signal(object):
    class Cleanup(object):
        def __init__(self, key, d):
            self.key = key
            self.d = d

        def __call__(self, wr):
            del self.d[self.key]

    def __init__(self):
        self.callbacks = {}  #observing object ID -> weak ref, methodNames

    def connect(self, observer):
        if not callable(observer):
            raise TypeError('Expected a method, got %s' % observer.__class__)

        ID = _make_id(observer)
        if ID in self.callbacks:
            s = self.callbacks[ID][1]
        else:
            try:
                target = weakref.ref(observer.__self__, Signal.Cleanup(ID, self.callbacks))
            except AttributeError:
                target = None
            s = set()
            self.callbacks[ID] = (target, s)

        if hasattr(observer, "__func__"):
            method = observer.__func__
        else:
            method = observer
        s.add(method)

    def disconnect(self, observer):
        ID = _make_id(observer)
        if ID in self.callbacks:
            if hasattr(observer, "__func__"):
                method = observer.__func__
            else:
                method = observer
            self.callbacks[ID][1].discard(method)
            if len(self.callbacks[ID][1]) == 0:
                del self.callbacks[ID]
        else:
            pass

    def disconnectAll(self):
        self.callbacks = {}  # observing object ID -> weak ref, methods

    def emit(self, *args, **kwargs):
        callbacks = self.callbacks.keys()
        for ID in callbacks:
            try:
                target, methods = self.callbacks[ID]
            except KeyError:
                continue
            for method in methods.copy():
                if target is None:  # Lambda or partial
                    method(*args, **kwargs)
                else:
                    targetObj = target()
                    if targetObj is not None:
                        method(targetObj, *args, **kwargs)


class Observable(Signal):
    def __init__(self, value):
        super(Observable, self).__init__()
        self.data = value

    def setValue(self, value):
        if value != self.data:
            self.data = value
            self.emit()

    def value(self):
        return self.data


_uiupdateFunction = None

def setUIupdateFunction(func):
    global _uiupdateFunction
    _uiupdateFunction= func

def updateUI():
    if _uiupdateFunction:
        _uiupdateFunction()


class WeakMethod(object):
    """A callable object. Takes one argument to init: 'object.method'.
    Once created, call this object -- MyWeakMethod() --
    and pass args/kwargs as you normally would.
    """
    def __init__(self, object_dot_method, callback=None):
        try:
            if callback is None:
                self.target = weakref.ref(object_dot_method.__self__)
            else:
                self.target = weakref.ref(object_dot_method.__self__, callback)
            self.method = object_dot_method.__func__
        except AttributeError:
            self.target = None
            self.method = object_dot_method

    def __call__(self, *args, **kwargs):
        """Call the method with args and kwargs as needed."""
        if self.is_dead():
            raise TypeError('Method called on dead object')
        if self.target is None:  # Lambda or partial
            return self.method(*args, **kwargs)
        else:
            return self.method(self.target(), *args, **kwargs)

    def is_dead(self):
        '''Returns True if the referenced callable was a bound method and
        the instance no longer exists. Otherwise, return False.
        '''
        return self.target is not None and self.target() is None


class Command:
    """Converts a method call with arguments to be ignored in a simple call with no/fixed arguments (replaces lambda)"""
    def __init__(self, callback, *args, **kwargs):
        self.callback = WeakMethod(callback)
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return apply(self.callback, self.args, self.kwargs)

if __name__ == '__main__':
    class test(object):
        def m(self):
            print "here"

        def __del__(self):
            print "deleted"

    x = test()
    y = x.m
    x = None
    y()
