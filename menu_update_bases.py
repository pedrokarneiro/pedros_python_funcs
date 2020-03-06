# Menu para Atualização das Bases
# 05/02/2020
# Pedro Carneiro Junior
# CGE-GO / AICI
# Ref.: https://www.youtube.com/watch?v=f3D-w6XMTN8
#       https://www.youtube.com/watch?v=TRaXgtTauuE

def menu():
# ini menu()
	print('Escolha a opção:')
	print('1. BuscaDadosTCM.py')
	print('2.  BuscaDadosJUCEG_BuscaCNPJ.py')
	print('3.  BuscaDadosDETRAN_CPF_novo.py')
	print('4.  BuscaDadosDETRAN_CNPJ.py')
	print('5.  BuscaDadosJUCEG_JUCEG.py')
	print('6.  BuscaDadosDETRAN.py')
	print('7.  BuscaDadosDETRAN_CPF.py')
	print('8.  BuscaDadosDETRAN_sociosCNPJ.py')
	print('9.  BuscaDadosDETRAN_sociosCPF.py')
	print('10. BuscaDadosJUCEG.py')
	print('11. BuscaDadosJUCEG_BaixadosRFB.py')
	print('12. BuscaDadosJUCEG_CorrigeEndereco.py')
	print('13. BuscaDadosRFB_BuscaCNPJ.py')
	print('99. Sair')
	
	while True:
		try:
			escolha = int(input('Escolha a opção:'))
			if escolha == 1:
				print('Opção 1')
				BuscaDadosTCM()
				break()
			elif escolha == 2:
				print('Opção 2')
				BuscaDadosJUCEG_BuscaCNPJ()
				break()
			elif escolha == 3:
				print('Opção 3')
				BuscaDadosDETRAN_CPF_novo()
				break()
			elif escolha == 4:
				print('Opção 4')
				BuscaDadosDETRAN_CNPJ()
				break()
			elif escolha == 5:
				print('Opção 5')
				BuscaDadosJUCEG_JUCEG()
				break()
			elif escolha == 6:
				print('Opção 6')
				BuscaDadosDETRAN()
				break()
			elif escolha == 7:
				print('Opção 7')
				BuscaDadosDETRAN_CPF()
				break()
			elif escolha == 8:
				print('Opção 8')
				BuscaDadosDETRAN_sociosCNPJ()
				break()
			elif escolha == 9:
				print('Opção 9')
				BuscaDadosDETRAN_sociosCPF()
				break()
			elif escolha == 10:
				print('Opção 10')
				BuscaDadosJUCEG()
				break()
			elif escolha == 11:
				print('Opção 11')
				BuscaDadosJUCEG_BaixadosRFB()
				break()
			elif escolha == 12:
				print('Opção 12')
				BuscaDadosJUCEG_CorrigeEndereco()
				break()
			elif escolha == 13:
				print('Opção 13')
				BuscaDadosRFB_BuscaCNPJ()
				break()
			elif escolha == 99:
				# Sair
				break()
			else:
				print('Opção inválida.')
				menu()
		except ValueError:
			print('Opção inválida.')
	exit
				
# fim menu()

menu()

def BuscaDadosTCM():
	print("BuscaDadosTCM")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosJUCEG_BuscaCNPJ():
	print("BuscaDadosJUCEG_BuscaCNPJ")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN_CPF_novo():
	print("BuscaDadosDETRAN_CPF_novo")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN_CNPJ():
	print("BuscaDadosDETRAN_CNPJ")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosJUCEG_JUCEG():
	print("BuscaDadosJUCEG_JUCEG")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN():
	print("BuscaDadosDETRAN")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN_CPF():
	print("BuscaDadosDETRAN_CPF")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN_sociosCNPJ():
	print("BuscaDadosDETRAN_sociosCNPJ")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosDETRAN_sociosCPF():
	print("BuscaDadosDETRAN_sociosCPF")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosJUCEG():
	print("BuscaDadosJUCEG")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosJUCEG_BaixadosRFB():
	print("BuscaDadosJUCEG_BaixadosRFB")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosJUCEG_CorrigeEndereco():
	print("BuscaDadosJUCEG_CorrigeEndereco")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
def BuscaDadosRFB_BuscaCNPJ():
	print("BuscaDadosRFB_BuscaCNPJ")
	anykey=input("Pressione qualquer tecla para voltar ao menu.")
	menu()
	
