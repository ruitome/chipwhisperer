# -*- coding: utf-8
from collections import OrderedDict


import numpy as np
import scipy.io as sio
import os
import datetime

__author__ = "Rui Tomé"

class CTCW():

    def __init__(self, name, author, number_traces, number_points, output_path):
        self.PROJECT_NAME = name
        self.PROJECT_AUTHOR = author
        self.NUMBER_TRACES = number_traces
        self.NUMBER_POINTS = number_points
        self.output_path = os.path.join(output_path)
        self.output_traces_path = os.path.join(self.output_path + self.PROJECT_NAME + "_data/" + "traces/")
        self.timestamp =  '{:%Y.%m.%d-%H.%M.%S}'.format(datetime.datetime.now())
        self.path_config_file = ""
        if not os.path.exists(self.output_traces_path):
            os.makedirs(self.output_traces_path)

    def config_gen(self):
        extension = ".cfg"
        filename = "config_" + self.timestamp + "_" + extension
        #relative path
        self.path_config_file = self.PROJECT_NAME + "_data/" + "traces/" + filename
        config_file = open(self.output_path + self.path_config_file, "w")
        info = OrderedDict()
        module = "[Trace Config]"
        info['numTraces'] = str(self.NUMBER_TRACES)
        info['format'] = "native"
        info['numPoints'] = str(self.NUMBER_POINTS)
        info['prefix'] = self.timestamp + "_"
        config_file.write(module + '\n')
        config_file.write('\n'.join([x + " = " + y for x, y in info.items()]) + '\n')
        config_file.close()

    def cwp_gen(self):
        extension = ".cwp"
        filename = self.PROJECT_NAME + extension
        config_file = open(self.output_path + filename, "w")
        settings = OrderedDict()
        module = "[Trace Management]"
        trace_file = "tracefile0 = " + self.path_config_file
        enabled = "enabled0 = True"
        module_cwp = "[ChipWhisperer]"
        module_general = "[[General Settings]]"
        settings = {'Project Name': self.PROJECT_NAME, 'Program Name': "ChipWhisperer",
                    'Project File Version': "1.00", 'Project Author': self.PROJECT_AUTHOR,
                    'Program Version': "V3.5.4"}
        config_file.write(module + "\n")
        config_file.write(trace_file + "\n")
        config_file.write(enabled + "\n")
        config_file.write(module_cwp + "\n")
        config_file.write(module_general + "\n")
        config_file.write('\n'.join([x + " = " + y for x, y in settings.items()]) + '\n')
        config_file.close()

    def load_key(self, filenames):
        for x in filenames:
            with open(x) as f:
                for line in f:
                    key = line.strip()
                    dec_key = np.array([int(key[x:x+2], 16) for x in range(0, len(key), 2)])
                    # print(dec_key)
                    np.save(os.path.abspath(self.output_traces_path + self.timestamp + "_knownkey.npy"), dec_key)


    def load_keylist(self, filenames):
        pt = []
        for x in filenames:
            with open(x) as f:
                for line in f:
                    key = line.strip()
                    dec_key = np.array([[int(key[x:x+2], 16) for x in range(0, len(key), 2)]])
                    # print(dec_key)
                    pt.append(dec_key)
        pt = np.repeat(pt, self.NUMBER_TRACES, axis=0)
        pt_x = np.vstack(pt)
        np.save(os.path.abspath(self.output_traces_path + self.timestamp + "_keylist.npy"), pt_x)


    def load_plaintexts(self, filename):
        pt_x = self.txt2npy_data(filename)
        np.save(os.path.abspath(self.output_traces_path + self.timestamp + "_textin.npy"), pt_x)


    def load_ciphertexts(self, filename):
        pt_x = self.txt2npy_data(filename)
        np.save(os.path.abspath(self.output_traces_path + self.timestamp + "_textout.npy"), pt_x)


    def txt2npy_data(self, filenames):
        # convert hex string to decimal
        pt = []
        for x in filenames:
            with open(x) as f:
                for line in f:
                    key = line.strip()
                    dec_key = np.array([[int(key[x:x + 2], 16) for x in range(0, len(key), 2)]])
                    pt.append(dec_key)
        pt_x = np.vstack(pt)
        return pt_x


    def load_traces(self, filenames):
        # Load Traces
        traces = []
        for x in filenames:
            traces_mat = sio.loadmat(x)
            traces.append(traces_mat[[x for x in traces_mat.keys() if not x.startswith("__")][0]])

        traces = np.vstack(traces)
        np.save(os.path.abspath(self.output_traces_path + self.timestamp + "_traces.npy"), traces)
