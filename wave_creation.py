import sys
import wave, struct, math, random

fname = None
try:
    fname = sys.argv[1]
except:
    print("{} <file name>".format(sys.argv[0]))
    sys.exit(1)

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sound.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)


fd = open(fname, 'r')

lines = fd.readlines()

fd.close()

for i in range(1001):
    for line in lines:
        value = int(line)
        value = value * 1000
        data = struct.pack('<h', value)
        obj.writeframesraw( data )

obj.close()
