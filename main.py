import random
from replit import clear
from art import logo

def baralho():
	"Retorna uma carta aleatória do baralho"
	cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	carta = random.choice(cartas)
	return carta

def calculate_score(cartas):
	if sum(cartas)==21 and len(cartas) ==2:
		return 0

	if 11 in cartas and sum(cartas) >21:
		cartas.remove(11)
		cartas.remove(1)

	return sum(cartas)

def compare(pontos_pessoa,pontos_pc):
	if pontos_pessoa >21 and pontos_pc > 21:
		return "você passou. Você perdeu"

	if pontos_pessoa == pontos_pc: 
		return "Empate"
	elif pontos_pc ==0: 
		return "Perde, o oponente tem Vinte e Um"
	elif pontos_pessoa == 0:
		return "Ganhe com um Vinte e Um"
	elif pontos_pessoa > 21:
		return "Você passou. Você perdeu"
	elif pontos_pc > 21:
		return "Oponente passou por cima. Você ganha"
	elif pontos_pessoa > pontos_pc:
		return "Você Venceu"
	else:
		return "Você Perdeu"

	def inicio_jogo():
		print(logo)


usuario_cartas = []
pc_cartas = []
final_jogo = False


for _ in range(2):
	usuario_cartas.append(baralho())
	pc_cartas.append(baralho())

while not final_jogo:

	pontos_pessoa = calculate_score(usuario_cartas)
	pontos_pc = calculate_score(pc_cartas)
	print(f"Suas cartas: {usuario_cartas} , Pontuação total: {pontos_pessoa}")
	print(f"Primeira carta do computador: {pc_cartas[0]}")

	if pontos_pessoa ==0 or pontos_pc ==0 or pontos_pessoa == 21:
		final_jogo = True
	else:
		
		poker_face = input(f"Digite 's' para ter outra carta, digite 'n' para passar: ")
		if poker_face == "s":
			usuario_cartas.append(baralho())
			final_jogo = True

	while pontos_pc != 0 and pontos_pc < 17:
		pc_cartas.appen(baralho())
		pontos_pc = calculate_score(pc_cartas)

	print(f"Sua mão final: {usuario_cartas}, Pontuação final: {pontos_pessoa}")
	print(f"Pc mão final: {pc_cartas}, Pontuação final: {pontos_pc}")
	print(compare(pontos_pessoa, pontos_pc))

	while input(f"Você quer jogar uma partida de VINTE E UM? Digite 's' ou 's':") == "y":
		clear()
		inicio_jogo()
