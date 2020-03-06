print("Menu")
print('A. BuscaDadosDETRAN.py')
print('B. BuscaDadosDETRAN_CNPJ.py')
print('C. BuscaDadosDETRAN_CPF.py')
print('D. BuscaDadosDETRAN_CPF_novo.py')
print('E. BuscaDadosDETRAN_sociosCNPJ.py')
print('F. BuscaDadosDETRAN_sociosCPF.py')
print('G. BuscaDadosJUCEG.py')
print('H. BuscaDadosJUCEG_BaixadosRFB.py')
print('I. BuscaDadosJUCEG_BuscaCNPJ.py')
print('J. BuscaDadosJUCEG_CorrigeEndereco.py')
print('K. BuscaDadosJUCEG_JUCEG.py')
print('L. BuscaDadosRFB_BuscaCNPJ.py')
print('M. BuscaDadosTCM.py')
print('X. Sair')

letra = input("Escolha uma rotina:").upper()
if letra = "A":
	import BuscaDadosDETRAN
	BuscaDadosDETRAN.main()
if letra = "B":
	import BuscaDadosDETRAN_CNPJ
	BuscaDadosDETRAN_CNPJ.main()
if letra = "C":
	import BuscaDadosDETRAN_CPF
	BuscaDadosDETRAN_CPF.main()
if letra = "D":
	import BuscaDadosDETRAN_CPF_novo
	BuscaDadosDETRAN_CPF_novo.main()
if letra = "E":
	import BuscaDadosDETRAN_sociosCNPJ
	BuscaDadosDETRAN_sociosCNPJ.main()
if letra = "F":
	import BuscaDadosDETRAN_sociosCPF
	BuscaDadosDETRAN_sociosCPF.main()
if letra = "G":
	import BuscaDadosJUCEG
	BuscaDadosJUCEG.main()
if letra = "H":
	import BuscaDadosJUCEG_BaixadosRFB
	BuscaDadosJUCEG_BaixadosRFB.main()
if letra = "I":
	import BuscaDadosJUCEG_BuscaCNPJ
	BuscaDadosJUCEG_BuscaCNPJ.main()
if letra = "J":
	import BuscaDadosJUCEG_CorrigeEndereco
	BuscaDadosJUCEG_CorrigeEndereco.main()
if letra = "K":
	import BuscaDadosJUCEG_JUCEG
	BuscaDadosJUCEG_JUCEG.main()
if letra = "L":
	import BuscaDadosRFB_BuscaCNPJ
	BuscaDadosRFB_BuscaCNPJ.main()
if letra = "M":
	import BuscaDadosTCM
	BuscaDadosTCM.main()
else:
	print("Entrada inválida. Escolha uma letra de A a M ou X para sair.")
	exit()




	
	