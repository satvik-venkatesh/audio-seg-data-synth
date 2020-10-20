from subprocess import Popen, PIPE
import glob

audio_files = glob.glob('audio/*.wav')

for a in audio_files:
	command = 'python doMusicAndSpeechDetection.py "' + a + '" "' + a.replace('.wav', '-preds.txt') + '"'
	print(command)
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
	output, err = p.communicate() 