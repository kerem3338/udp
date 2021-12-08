import sys
import executer


try:
	if sys.argv[1] == "run":
		try:
			executer.Executer(sys.argv[2])
		except IndexError:
			print("Hata: 'run' için bir argüman gereklidir örnek run dosya.udp")
	else:
		print("Ergüman Hatası yardım için -h")
except IndexError:
	print("Ergüman Hatası yardım için -h")