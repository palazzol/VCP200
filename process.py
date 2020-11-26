# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:55:43 2020

@author: palazzol
"""
import sys
import numpy as np
import struct

# Firstly, we acquired most of Port B of the VCP200 (MC6804J2)
# in ROM VERIFY Mode
# We convert the sigrok file to binary, and parse it according to
# the channels
index = {}
index['PB7'] = 0
index['PB6'] = 1
index['PB5'] = 2
index['PB3'] = 4
index['PB2'] = 6
index['PB0'] = 7

word_clock = []
crcdata1 = []
crcdata2 = []

address = []
serdata = []

# This is plenty to process
count = 8*2*12*0x4010*3

print('Reading data file and sampling on clock edges...')

with open('testdata_romverify.bin','rb') as fp:
	oldb = int.from_bytes(fp.read(1),byteorder='big')
	b = fp.read(1)
	while b != b'':
	    b = int.from_bytes(b,byteorder='big')
		# Falling edge of PB7, sample PB6, PB3, and PB2
	    if (((oldb >> index['PB7']) & 0x01) == 1) and (((   b >> index['PB7']) & 0x01) == 0):
	        word_clock.append((b >> index['PB6']) & 0x01)
	        crcdata1.append((b >> index['PB3']) & 0x01)
	        crcdata2.append((b >> index['PB2']) & 0x01)
		# Rising edge of PB7, sample PB5 and PB0
	    elif (((oldb >> index['PB7']) & 0x01) == 0) and (((   b >> index['PB7']) & 0x01) == 1):
	        address.append((b >> index['PB5']) & 0x01)
	        serdata.append((b >> index['PB0']) & 0x01)
	    oldb = b
	    b = fp.read(1)
	    count = count - 1
	    if count == 0:
	        break
	fp.close()

# PB7 seems to be our bit word_clock
# PB6 seems to be high once every 12 bits, a frame clock
# PB5 seems to be the address value
# PB3 and PB2 look random, probably the CRC values
# PB0 looks like our serial program data!

word_clock = np.array(word_clock)
address = np.array(address)
serdata = np.array(serdata)
crcdata1 = np.array(crcdata1)
crcdata2 = np.array(crcdata2)

# In this section, we assemble bytes from bits

print('Assembling words from bits...')

address_valuelist = []
serdata_valuelist = []
crcdata1_valuelist = []
crcdata2_valuelist = []

address_value = -1
serdata_value = 0
serdata_phase = 1
crcdata1_value = 0
crcdata2_value = 0
last_value = 0
for i in range(0,len(word_clock)-1):
    if word_clock[i] == 1:  # This seems to start the frame
        if address_value != -1:
            address_valuelist.append(address_value)
            # just checking some patterns
            if ((crcdata1_value & 0xc00) == 0xd00) or ((crcdata1_value & 0xc00) == 0xe00):
                print('Error 1!')
                sys.exit(-1)
            if ((crcdata2_value & 0xc00) == 0xd00) or ((crcdata2_value & 0xc00) == 0xe00):
                print('Error 2!')
                sys.exit(-1)
            crcdata1_valuelist.append(crcdata1_value & 0xfff)
            crcdata2_valuelist.append(crcdata2_value & 0xfff)
            #serdata_valuelist.append(serdata_value)
            #if (serdata_value & 0x3 != 0x3):
            #    print('Error 3!')
            #    sys.exit(-1)
            if serdata_phase == 0:
                last_value = serdata_value
                serdata_valuelist.append(last_value)
            else:
                serdata_valuelist.append(last_value)
            serdata_phase = serdata_phase + 1
            if serdata_phase == 2:
                serdata_phase = 0
        address_value = 0
        serdata_value = 0
    if address_value != -1:
        address_value = (address_value >> 1) + address[i]*(0x800)
        serdata_value = (serdata_value >> 1) + serdata[i]*(0x800)
        crcdata1_value = (crcdata1_value >> 1) + crcdata1[i]*(0x800)
        crcdata2_value = (crcdata2_value >> 1) + crcdata2[i]*(0x800)

crcdata1_valuelist = np.array(crcdata1_valuelist)
crcdata2_valuelist = np.array(crcdata2_valuelist)
serdata_valuelist = np.array(serdata_valuelist)
serdata_valuelist = (serdata_valuelist & 0x3fc) >> 2

#print(hex(len(address_valuelist)),hex(address_valuelist[1]),hex(address_valuelist[-1]))

# Now we have more than one copy of the data
# Just put one copy in a dictionary

print('Limiting ourselves to one copy of the data...')

data = {}
last_address = -1
for i in range(0,len(address_valuelist)):
    if last_address == -1:
        last_address = address_valuelist[i]
    else:
        address = address_valuelist[i]
        if address != last_address:
            if address in data.keys():
                if serdata_valuelist[i] != data[address]:
                    print('***', address, i, serdata_valuelist[i], data[address])
            else:
                #print('filling: data['+str(count)+'] ='+str(serdata_valuelist[i]))
                data[address] = serdata_valuelist[i]
            last_address = address

print('Writing binary file...')

# One copy is 4K, even if it's clear that we have only 2K of space
with open('vcp200.bin','wb') as fp:
	for i in range(0,4096):
	    fp.write(struct.pack("B", data[(i+2)%4096]))

print('Done!')
