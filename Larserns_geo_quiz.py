# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:38:04 2021

@author: larsh
"""

import random
from world import states
from world import countries
from datetime import datetime  
from random import randint

def print_menu():
	print("\nVelkommen til Larserns GEO QUIZ!! Hva vil du gjøre?")
	print("1. Spill Amerika-quiz.")
	print("2. Spill World-quiz.")
	print("3. Spill Gangetabell-quiz.")
	print("4. Se på historikk fra tidligere spill.")
	print("5. Vis liste over gale svar fra forrige spill.")
	print("6. Slett historikk.")
	print("7. Avslutt spill.")
	

def valid_choice(choice):
	try:
		valg = int(choice)
		if 0 < valg < 8:
			return True
	except:
		pass
	
	return False


def world_quiz():
	print("Velkommen til WORLD-Quiz!!")
	country_list = list(countries)
	korrekt = 0
	antall = input("Hvor mange spørsmål vil du ha?\n")
	while not antall.isdigit():
		print("Du må taste en gyldig verdi.")
		antall = input("Hvor mange spørsmål vil du ha? ")
	navn = input("Hva er navnet ditt? ")
	antall_int = int(antall)
	print("Du kan når som helst avslutte spillet ved å tryke: 'Q'.")
	navn_type = "World-Quiz: "+navn
	for spm in range(antall_int):
		num = random.randint(0,197)
		land = country_list[num]
		svar = input(f"Hva er hovedstaden i {land}? ").upper()
		if svar == 'Q':
			break
		elif svar == countries[land]:
			korrekt += 1
			print(f"{countries[land]} er riktig.")
		else:
			print(f"Det er feil. Riktig svar er {countries[land]}.")
			wrongs.append(f"{navn} svarte feil på dette landet:")
			wrongs.append(land)
			wrongs.append(f"Hovedtaden er {countries[land]}. Ditt svar: {svar}.")
		
	dato = datetime.now().strftime("%Y-%m-%d %H:%M")
	print(f"\nGratulerer, {navn}! Du fikk {korrekt} riktige spørsmål av {antall_int} mulige.")
	legge_til_historie(navn_type, korrekt, antall_int,dato)


def america_quiz():
	print("Velkommen til Amerika-Quiz!!")
	statesList = list(states)
	korrekt = 0
	antall = input("Hvor mange spørsmål ønsker du? \n")
	while not antall.isdigit():
		print("Du må taste inn et tall, prøv på nytt.")
		antall = input("Hvor mange spørsmål ønsker du? ")
	navn = input("Skriv inn navnet ditt:\n")
	antall_int = int(antall)
	print("Du kan når som helst avslutte spillet ved å tryke: 'Q'.")
	navn_type = "Amerika-Quiz: "+navn
	for spm in range(antall_int):
		num = random.randint(0,49)
		stater = statesList[num]
		svar = input(f"Hva er hovedstaden i {stater}? ").upper()
		if svar == 'Q':
			break
		elif svar == states[stater]:
			korrekt += 1
			print(f"{states[stater]} er riktig.")
		else:
			wrongs.append(f"{navn} svarte feil på denne delstaten:")
			wrongs.append(stater)
			wrongs.append(f"Hovedstaden er {states[stater]}. Ditt svar: {svar}.")
			print(f"Feil. Riktig svar er: {states[stater]}. ")
	dato = datetime.now().strftime("%Y-%m-%d %H:%M") 		
	print(f"\nGratulerer, {navn}! Du fikk {korrekt} riktige spørsmål av {antall_int} mulige .")
	legge_til_historie(navn_type,korrekt,antall_int,dato)


def wrong_answers():
	if len(wrongs) == 0:
		print("\nDu har ingen feil fra denne runden.")
		print("Vennligst start et nytt spill.")
	else:
		print("\nFeil fra forrige runde:")
		for wrong in wrongs:
			print(wrong)

def gangetabellen():

	navn = input("Skriv ditt navn og avslutt med enter.\n")

	ant_stk = 5
	ant_rett = 0
	for i in range(5):
		tall_en = randint(1,10)
		tall_to = randint(1,10)
		print(f"Hva er {tall_en} ganger {tall_to}? Avslutt spillet? trykk 'q'")
		svar = input()
	
	if svar == 'q':
		print("Avslutter programmet.")
  	
		
	if int(svar) == tall_en * tall_to:
		print(f"Ja, svaret er {svar}\n")
		ant_rett = ant_rett + 1
		
	elif int(svar) != tall_en * tall_to: 
		print(f"Nei,svaret er ikke {svar}. Det riktige svaret er {str(tall_en * tall_to)}")
		
	else:
		print("Du tastet en ugyldig verdi.")
		print(f"Godt jobba, {navn}!! Du fikk {ant_rett} av {ant_stk} riktige.")
	
	


def delete_history():
	print("\nSletter all oppført historikk...")
	file = open("historie.txt", "r")

	lines = file.readlines()
	file.close()

	new_file = open("historie.txt", "w")
	for line in lines:
		  if line.strip("\n") == "line":

			         new_file.write(line)



def legge_til_historie(navn,korrekt,antall,dato):
	with open("historie.txt", 'a') as f:
		f.write(f"Dato: {dato} {navn} klarte {korrekt} av {antall}. Det gir {korrekt / antall *100:.2f} % uttelling. \n")

	
def vis_historie():
	with open("historie.txt", 'r') as f:
		lines = f.readlines()
		
	for line in lines[-20:]:
		print(line, end="")


wrongs = []
while True:
	print_menu()
	valg = input("Hva vil du gjøre?\n")
	while not valid_choice(valg):
		print("Ugyldig valg, prøv på nytt.")
		print_menu()
		valg = input("Hva vil du gjøre?\n")
	if int(valg) == 1:
		america_quiz()
	elif int(valg) == 2:
		world_quiz()
	elif int(valg) == 3:
		gangetabellen()
	elif int(valg) == 4:
 		vis_historie()
	elif int(valg) == 5:
		wrong_answers()
	elif int(valg) == 6:
		delete_history()
	elif int(valg) == 7:
		print("\nSpill avsluttet! På gjensyn...")
		break