#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Put this file in: .hts/tvheaden/input/iptv/networks/<network_id>/

from os import listdir
from json import loads

target_file = 'movistar_iptv.m3u'
network = 'Movistar Fibra'
tvheadend_ip = '10.0.0.1:9981'

with open(target_file, 'w') as playlist:
    playlist.write('#EXTM3U\n')
    for mux in listdir('./muxes'):
        with open('./muxes/%s/config' % mux) as json_file:
            file_list = json_file.readlines()
        for line in file_list:
            if line.split(':')[0].lstrip('\t') == '\"iptv_muxname\"':
                muxname = line.split(':')[1]
                playlist.write('#EXTINF:-1,%s / %s\n' % (muxname[2:-3], network))
                playlist.write('http://%s/stream/mux/%s\n' %(tvheadend_ip, mux))
