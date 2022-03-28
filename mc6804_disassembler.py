# -*- coding: utf-8 -*-
"""
Created on Tues Sep 29 2020

@author: abzman, palazzol

"""

decoder = { 
        0x00: ['BNE', 'REL'],
        0x01: ['BNE', 'REL'],
        0x02: ['BNE', 'REL'],
        0x03: ['BNE', 'REL'],
        0x04: ['BNE', 'REL'],
        0x05: ['BNE', 'REL'],
        0x06: ['BNE', 'REL'],
        0x07: ['BNE', 'REL'],
        0x08: ['BNE', 'REL'],
        0x09: ['BNE', 'REL'],
        0x0a: ['BNE', 'REL'],
        0x0b: ['BNE', 'REL'],
        0x0c: ['BNE', 'REL'],
        0x0d: ['BNE', 'REL'],
        0x0e: ['BNE', 'REL'],
        0x0f: ['BNE', 'REL'],
        0x10: ['BNE', 'REL'],
        0x11: ['BNE', 'REL'],
        0x12: ['BNE', 'REL'],
        0x13: ['BNE', 'REL'],
        0x14: ['BNE', 'REL'],
        0x15: ['BNE', 'REL'],
        0x16: ['BNE', 'REL'],
        0x17: ['BNE', 'REL'],
        0x18: ['BNE', 'REL'],
        0x19: ['BNE', 'REL'],
        0x1a: ['BNE', 'REL'],
        0x1b: ['BNE', 'REL'],
        0x1c: ['BNE', 'REL'],
        0x1d: ['BNE', 'REL'],
        0x1e: ['BNE', 'REL'],
        0x1f: ['BNE', 'REL'],

        0x20: ['BEQ', 'REL'],
        0x21: ['BEQ', 'REL'],
        0x22: ['BEQ', 'REL'],
        0x23: ['BEQ', 'REL'],
        0x24: ['BEQ', 'REL'],
        0x25: ['BEQ', 'REL'],
        0x26: ['BEQ', 'REL'],
        0x27: ['BEQ', 'REL'],
        0x28: ['BEQ', 'REL'],
        0x29: ['BEQ', 'REL'],
        0x2a: ['BEQ', 'REL'],
        0x2b: ['BEQ', 'REL'],
        0x2c: ['BEQ', 'REL'],
        0x2d: ['BEQ', 'REL'],
        0x2e: ['BEQ', 'REL'],
        0x2f: ['BEQ', 'REL'],
        0x30: ['BEQ', 'REL'],
        0x31: ['BEQ', 'REL'],
        0x32: ['BEQ', 'REL'],
        0x33: ['BEQ', 'REL'],
        0x34: ['BEQ', 'REL'],
        0x35: ['BEQ', 'REL'],
        0x36: ['BEQ', 'REL'],
        0x37: ['BEQ', 'REL'],
        0x38: ['BEQ', 'REL'],
        0x39: ['BEQ', 'REL'],
        0x3a: ['BEQ', 'REL'],
        0x3b: ['BEQ', 'REL'],
        0x3c: ['BEQ', 'REL'],
        0x3d: ['BEQ', 'REL'],
        0x3e: ['BEQ', 'REL'],
        0x3f: ['BEQ', 'REL'],

        0x40: ['BCC', 'REL'],
        0x41: ['BCC', 'REL'],
        0x42: ['BCC', 'REL'],
        0x43: ['BCC', 'REL'],
        0x44: ['BCC', 'REL'],
        0x45: ['BCC', 'REL'],
        0x46: ['BCC', 'REL'],
        0x47: ['BCC', 'REL'],
        0x48: ['BCC', 'REL'],
        0x49: ['BCC', 'REL'],
        0x4a: ['BCC', 'REL'],
        0x4b: ['BCC', 'REL'],
        0x4c: ['BCC', 'REL'],
        0x4d: ['BCC', 'REL'],
        0x4e: ['BCC', 'REL'],
        0x4f: ['BCC', 'REL'],
        0x50: ['BCC', 'REL'],
        0x51: ['BCC', 'REL'],
        0x52: ['BCC', 'REL'],
        0x53: ['BCC', 'REL'],
        0x54: ['BCC', 'REL'],
        0x55: ['BCC', 'REL'],
        0x56: ['BCC', 'REL'],
        0x57: ['BCC', 'REL'],
        0x58: ['BCC', 'REL'],
        0x59: ['BCC', 'REL'],
        0x5a: ['BCC', 'REL'],
        0x5b: ['BCC', 'REL'],
        0x5c: ['BCC', 'REL'],
        0x5d: ['BCC', 'REL'],
        0x5e: ['BCC', 'REL'],
        0x5f: ['BCC', 'REL'],
        
        0x60: ['BCS', 'REL'],
        0x61: ['BCS', 'REL'],
        0x62: ['BCS', 'REL'],
        0x63: ['BCS', 'REL'],
        0x64: ['BCS', 'REL'],
        0x65: ['BCS', 'REL'],
        0x66: ['BCS', 'REL'],
        0x67: ['BCS', 'REL'],
        0x68: ['BCS', 'REL'],
        0x69: ['BCS', 'REL'],
        0x6a: ['BCS', 'REL'],
        0x6b: ['BCS', 'REL'],
        0x6c: ['BCS', 'REL'],
        0x6d: ['BCS', 'REL'],
        0x6e: ['BCS', 'REL'],
        0x6f: ['BCS', 'REL'],
        0x70: ['BCS', 'REL'],
        0x71: ['BCS', 'REL'],
        0x72: ['BCS', 'REL'],
        0x73: ['BCS', 'REL'],
        0x74: ['BCS', 'REL'],
        0x75: ['BCS', 'REL'],
        0x76: ['BCS', 'REL'],
        0x77: ['BCS', 'REL'],
        0x78: ['BCS', 'REL'],
        0x79: ['BCS', 'REL'],
        0x7a: ['BCS', 'REL'],
        0x7b: ['BCS', 'REL'],
        0x7c: ['BCS', 'REL'],
        0x7d: ['BCS', 'REL'],
        0x7e: ['BCS', 'REL'],
        0x7f: ['BCS', 'REL'],
        
        0x80: ['JSR', 'EXT'],
        0x81: ['JSR', 'EXT'],
        0x82: ['JSR', 'EXT'],
        0x83: ['JSR', 'EXT'],
        0x84: ['JSR', 'EXT'],
        0x85: ['JSR', 'EXT'],
        0x86: ['JSR', 'EXT'],
        0x87: ['JSR', 'EXT'],
        0x88: ['JSR', 'EXT'],
        0x89: ['JSR', 'EXT'],
        0x8a: ['JSR', 'EXT'],
        0x8b: ['JSR', 'EXT'],
        0x8c: ['JSR', 'EXT'],
        0x8d: ['JSR', 'EXT'],
        0x8e: ['JSR', 'EXT'],
        0x8f: ['JSR', 'EXT'],
        
        0x90: ['JMP', 'EXT'],
        0x91: ['JMP', 'EXT'],
        0x92: ['JMP', 'EXT'],
        0x93: ['JMP', 'EXT'],
        0x94: ['JMP', 'EXT'],
        0x95: ['JMP', 'EXT'],
        0x96: ['JMP', 'EXT'],
        0x97: ['JMP', 'EXT'],
        0x98: ['JMP', 'EXT'],
        0x99: ['JMP', 'EXT'],
        0x9a: ['JMP', 'EXT'],
        0x9b: ['JMP', 'EXT'],
        0x9c: ['JMP', 'EXT'],
        0x9d: ['JMP', 'EXT'],
        0x9e: ['JMP', 'EXT'],
        0x9f: ['JMP', 'EXT'],
    
        0xa0: ['Reserved Opcode', ''],
        0xa1: ['Reserved Opcode', ''],
        0xa2: ['Reserved Opcode', ''],
        0xa3: ['Reserved Opcode', ''],
        0xa4: ['Reserved Opcode', ''],
        0xa5: ['Reserved Opcode', ''],
        0xa6: ['Reserved Opcode', ''],
        0xa7: ['Reserved Opcode', ''],
    
        0xa8: ['INC', 'X'],
        0xa9: ['INC', 'Y'],
        0xaa: ['INC', 'V'],
        0xab: ['INC', 'W'],
        0xac: ['LDA', 'X'],
        0xad: ['LDA', 'Y'],
        0xae: ['LDA', 'V'],
        0xaf: ['LDA', 'W'],
        
        0xb0: ['MVI', 'IMM2'],
        
        0xb1: ['Reserved Opcode', ''],
        
        0xb2: ['RTI', ''],
        0xb3: ['RTS', ''],
        0xb4: ['COMA', ''],
        0xb5: ['ROLA', ''],
        0xb6: ['STOP', ''],
        0xb7: ['WAIT', ''],
        
        0xb8: ['DEC', 'X'],
        0xb9: ['DEC', 'Y'],
        0xba: ['DEC', 'V'],
        0xbb: ['DEC', 'W'],
        0xbc: ['STA', 'X'],
        0xbd: ['STA', 'Y'],
        0xbe: ['STA', 'V'],
        0xbf: ['STA', 'W'],

        0xc0: ['BRCLR', 'BTB'],
        0xc1: ['BRCLR', 'BTB'],
        0xc2: ['BRCLR', 'BTB'],
        0xc3: ['BRCLR', 'BTB'],
        0xc4: ['BRCLR', 'BTB'],
        0xc5: ['BRCLR', 'BTB'],
        0xc6: ['BRCLR', 'BTB'],
        0xc7: ['BRCLR', 'BTB'],
        0xc8: ['BRSET', 'BTB'],
        0xc9: ['BRSET', 'BTB'],
        0xca: ['BRSET', 'BTB'],
        0xcb: ['BRSET', 'BTB'],
        0xcc: ['BRSET', 'BTB'],
        0xcd: ['BRSET', 'BTB'],
        0xce: ['BRSET', 'BTB'],
        0xcf: ['BRSET', 'BTB'],
        
        0xd0: ['BCLR', 'BSC'],
        0xd1: ['BCLR', 'BSC'],
        0xd2: ['BCLR', 'BSC'],
        0xd3: ['BCLR', 'BSC'],
        0xd4: ['BCLR', 'BSC'],
        0xd5: ['BCLR', 'BSC'],
        0xd6: ['BCLR', 'BSC'],
        0xd7: ['BCLR', 'BSC'],
        0xd8: ['BSET', 'BSC'],
        0xd9: ['BSET', 'BSC'],
        0xda: ['BSET', 'BSC'],
        0xdb: ['BSET', 'BSC'],
        0xdc: ['BSET', 'BSC'],
        0xdd: ['BSET', 'BSC'],
        0xde: ['BSET', 'BSC'],
        0xdf: ['BSET', 'BSC'],
        
        0xe0: ['LDA', '[X]'],
        0xe1: ['STA', '[X]'],
        0xe2: ['ADD', '[X]'],
        0xe3: ['SUB', '[X]'],
        0xe4: ['CMP', '[X]'],
        0xe5: ['AND', '[X]'],
        0xe6: ['INC', '[X]'],
        0xe7: ['DEC', '[X]'],
        
        0xe8: ['LDA', 'IMM'],
        
        0xe9: ['Illegal Opcode', ''],
        
        0xea: ['ADD', 'IMM'],
        0xeb: ['SUB', 'IMM'],
        0xec: ['CMP', 'IMM'],
        0xed: ['AND', 'IMM'],
 
        0xee: ['Illegal Opcode', ''],
        0xef: ['Illegal Opcode', ''],

        0xf0: ['LDA', '[Y]'],
        0xf1: ['STA', '[Y]'],
        0xf2: ['ADD', '[Y]'],
        0xf3: ['SUB', '[Y]'],
        0xf4: ['CMP', '[Y]'],
        0xf5: ['AND', '[Y]'],
        0xf6: ['INC', '[Y]'],
        0xf7: ['DEC', '[Y]'],
        
        0xf8: ['LDA', 'DIR'],
        0xf9: ['STA', 'DIR'],
        0xfa: ['ADD', 'DIR'],
        0xfb: ['SUB', 'DIR'],
        0xfc: ['CMP', 'DIR'],
        0xfd: ['AND', 'DIR'],
        0xfe: ['INC', 'DIR'],
        0xff: ['DEC', 'DIR']
        
}

J2DataLabels = {
    0x00: "PORTA",
    0x01: "PORTB",
    0x04: "DDRA",
    0x05: "DDRB",
    0x09: "TSTATUS",
    0x80: "X",
    0x81: "Y",
    0x82: "V",
    0x83: "W",
    0xFD: "PRESCALE",
    0xFE: "TCOUNT",
    0xFF: "A"
}

# Hex Formatting Functions
def Hex8(v):
    return f'{v:02X}'

def Hex12(v):
    return f'{v:03X}'

# Format Operands for various Addressing Modes
def Relative(PC, x):
    offs = x & 0x1f
    if offs > 15:
        offs = offs - 32
    return '$'+Hex12(PC+1+offs)

def Extended(x1, x2):
    offs = ((x1 & 0x0f)<<8) + x2
    return '$'+Hex12(offs)

def Immediate2(x1, x2):
    return J2DataLabels[x1]+',#$'+Hex8(x2)

def BitTestBranch(PC, x1, bytetotest, offs):
    bittotest = x1 & 0x7
    if offs > 127:
        offs = offs - 256
    return str(bittotest)+','+J2DataLabels[bytetotest]+',$'+Hex12(PC+3+offs)

def BitSetClear(x1, x2):
    bittotest = x1 & 0x07
    return str(bittotest)+','+J2DataLabels[x2]

def Immediate(x):
    return '#$'+Hex8(x)

def Direct(x):
    return J2DataLabels[x]

# Format up to 3 Raw Bytes for display
def FormatRawBytes(xlist):
    s = ''
    for b in xlist:
        s = s + Hex8(b)
        s = s + ' '
    if len(xlist) < 3:
        for i in range(0,3-len(xlist)):
            s = s + '   ' # Space for no Hex value
    return s
    
for i in range(0x18, 0x60):
    J2DataLabels[i] = "ROM"+Hex8(i)
for i in range(0x84, 0xA0):
    J2DataLabels[i] = "RAM"+Hex8(i)
for i in range(0x00, 0x100):
    if i not in J2DataLabels.keys():
        J2DataLabels[i] = '$'+Hex8(i)

# Read file contents into bytearray
with open('vcp200_program_rom.bin','rb') as f:
    data = f.read(0x1000)

# Skip to the code
addr = 0xae0

# Disassemble into string array
disassembly = []

while (addr < 0x1000):
    a=data[addr]
    opcode, mode = decoder[a]
    if mode == 'REL':
        nextaddr = addr + 1
        rawbytes = FormatRawBytes([a])
        operand = Relative(addr, a)
    elif mode == 'EXT':
        nextaddr = addr + 2
        b=data[addr+1]
        rawbytes = FormatRawBytes([a, b])
        operand = Extended(a, b)
    elif mode == 'IMM2':
        nextaddr = addr + 3
        b=data[addr+1]
        c=data[addr+2]
        rawbytes = FormatRawBytes([a, b, c])
        operand = Immediate2(b, c)            
    elif mode == 'BTB':
        nextaddr = addr + 3
        b=data[addr+1]
        c=data[addr+2]
        rawbytes = FormatRawBytes([a, b, c])
        operand = BitTestBranch(addr, a, b, c)          
    elif mode == 'BSC':
        nextaddr = addr + 2
        b=data[addr+1]
        rawbytes = FormatRawBytes([a, b])
        operand = BitSetClear(a, b) 
    elif mode == 'IMM':
        nextaddr = addr + 2
        b=data[addr+1]
        rawbytes = FormatRawBytes([a, b])
        operand = Immediate(b)
    elif mode == 'DIR':
        nextaddr = addr + 2
        b=data[addr+1]
        rawbytes = FormatRawBytes([a, b])
        operand = Direct(b)
    else:
        nextaddr = addr + 1
        rawbytes = FormatRawBytes([a])
        operand = mode
    disassembly.append(Hex12(addr)+': ' + rawbytes + '   ' + opcode + ' ' + operand + '\n')
    addr = nextaddr

# Write out file
with open('disassemblynew.txt','w') as f:
    for line in disassembly:
        f.write(line)


