import os

PULSE_LENGTH = 560
ONE_PULSE_TOTAL = 2250
ONE_MIN_PULSE = (ONE_PULSE_TOTAL - PULSE_LENGTH) * 0.9
ONE_MAX_PULSE = (ONE_PULSE_TOTAL - PULSE_LENGTH) * 1.1

fileName = 'data.txt'
os.system('mode2 -d /dev/lirc0 >> data.txt')

f = file(fileName)

lines = f.readlines()

type = map(lambda x: x.split()[0], lines)
size = map(lambda x: x.split()[1], lines)

# first bit of message should start at index 12 with pulse
first = size[13]
second = size[15]
third = size[17]

out = ''

if ONE_MIN_PULSE < first < ONE_MAX_PULSE:
	out += '1'
else:
	out += '0'

if ONE_MIN_PULSE < second < ONE_MAX_PULSE:
        out += '1'
else:
        out += '0'

if ONE_MIN_PULSE < third < ONE_MAX_PULSE:
        out += '1'
else:
        out += '0'


print out
os.remove(fileName)
