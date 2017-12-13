import os
import zlib

krc2lrc_path = "C:/KuGou/Lyric/"
songname = "hengyanjun-xiangweiwochangshouge"
songFile = os.path.join(krc2lrc_path,songname+'.krc')

fkrc = open(songFile,'rb').read()

decodeSet = [64, 71, 97, 119, 94, 50, 116, 71, 81, 54, 49, 45, 206, 210, 110, 105]
fkrc_1 = fkrc[4:]

len_fkrc_1 = len(fkrc_1)

f_decoding = fkrc_1

res = ''
for i in range(len_fkrc_1):
	a = i % 16
	res = res + chr(ord(f_decoding[i]) ^ decodeSet[a])

zobj = zlib.decompressobj() 
f_decoding = zobj.decompress(res)

f2 = open(krc2lrc_path + songname + '.txt', 'w')
f2.write(f_decoding)
#f2.write('UTF-8'.decode('zlib'))
f2.close()


