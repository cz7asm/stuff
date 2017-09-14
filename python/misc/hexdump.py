def dump16(s, offset=0):
	if len(s) > 16: s = s[:16]

	asciipart = ''.join( [(c if c.isalnum() else '.') for c in s] )
	hexpart = ' '.join( [hex(ord(c))[2:].zfill(2) for c in s] )
	hexpart = hexpart.ljust(16*3)

	print '%08x  %s %s |%s|' % (offset, hexpart[:8*3], hexpart[8*3:], asciipart)

def hexdump(s):
	for i in range((len(s)+15)/16):
		pos = i*16
		dump16(s[pos:pos+16], pos)

hexdump('Timto te zdravim a posilam pozdravy z meho velmi limitovaneho hexeditoru!')
