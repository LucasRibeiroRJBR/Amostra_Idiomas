from tkinter import *

from uteis.textos import *


class JanelaIdioma():
    def __init__(self, idioma, texto, bandeira):
        self.idioma = idioma
        self.texto = texto
        self.bandeira = bandeira

    def criar_janela(self):
        if self.idioma == "Armênio":
            self.texto = armeno

            root_armeno = Toplevel()
            root_armeno.title("Armênio")

            bandeira = Label(root_armeno, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_armeno = Label(root_armeno, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_armeno.grid(row=1, column=0)

        if self.idioma == "Árabe":
            self.texto = arabe

            root_arabe = Toplevel()
            root_arabe.title("Árabe")

            bandeira = Label(root_arabe, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_arabe = Label(root_arabe, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_arabe.grid(row=1, column=0)

        if self.idioma == "Búlgaro":
            self.texto = bulgado

            root_bulgado = Toplevel()
            root_bulgado.title("Búlgaro")

            bandeira = Label(root_bulgado, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_bulgado = Label(root_bulgado, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_bulgado.grid(row=1, column=0)

        if self.idioma == "Mandarim":
            self.texto = mandarim

            root_mandarim = Toplevel()
            root_mandarim.title("Mandarim")

            bandeira = Label(root_mandarim, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_mandarim = Label(root_mandarim, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_mandarim.grid(row=1, column=0)

        if self.idioma == "Taiwanês":
            self.texto = taiwanes

            root_taiwanes = Toplevel()
            root_taiwanes.title("Taiwanês")

            bandeira = Label(root_taiwanes, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_taiwanes = Label(root_taiwanes, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_taiwanes.grid(row=1, column=0)

        if self.idioma == "Croata":
            self.texto = croata

            root_croata = Toplevel()
            root_croata.title("Croata")

            bandeira = Label(root_croata, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_croata = Label(root_croata, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_croata.grid(row=1, column=0)

        if self.idioma == "Tcheco":
            self.texto = tcheco

            root_tcheco = Toplevel()
            root_tcheco.title("Tcheco")

            bandeira = Label(root_tcheco, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_tcheco = Label(root_tcheco, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_tcheco.grid(row=1, column=0)

        if self.idioma == "Dinamarquês":
            self.texto = dinamarques

            root_dinamarques = Toplevel()
            root_dinamarques.title("Dinamarquês")

            bandeira = Label(root_dinamarques, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_dinamarques = Label(root_dinamarques, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_dinamarques.grid(row=1, column=0)

        if self.idioma == "Holandês":
            self.texto = holandes

            root_holandes = Toplevel()
            root_holandes.title("Holandês")

            bandeira = Label(root_holandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_holandes = Label(root_holandes, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_holandes.grid(row=1, column=0)

        if self.idioma == "Inglês":
            self.texto = ingles

            root_ingles = Toplevel()
            root_ingles.title("Inglês")

            bandeira = Label(root_ingles, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_ingles = Label(root_ingles, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_ingles.grid(row=1, column=0)

        if self.idioma == "Estoniano":
            self.texto = estoniano

            root_estoniano = Toplevel()
            root_estoniano.title("Estoniano")

            bandeira = Label(root_estoniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_estoniano = Label(root_estoniano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_estoniano.grid(row=1, column=0)

        if self.idioma == "Filipino":
            self.texto = filipino

            root_filipino = Toplevel()
            root_filipino.title("Filipino")

            bandeira = Label(root_filipino, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_filipino = Label(root_filipino, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_filipino.grid(row=1, column=0)

        if self.idioma == "Finlandês":
            self.texto = finlandes

            root_finlandes = Toplevel()
            root_finlandes.title("Finlandês")

            bandeira = Label(root_finlandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_finlandes = Label(root_finlandes, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_finlandes.grid(row=1, column=0)

        if self.idioma == "Francês":
            self.texto = frances

            root_frances = Toplevel()
            root_frances.title("Francês")

            bandeira = Label(root_frances, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_frances = Label(root_frances, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_frances.grid(row=1, column=0)

        if self.idioma == "Georgiano":
            self.texto = georgiano

            root_georgiano = Toplevel()
            root_georgiano.title("Georgiano")

            bandeira = Label(root_georgiano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_georgiano = Label(root_georgiano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_georgiano.grid(row=1, column=0)

        if self.idioma == "Alemão":
            self.texto = alemao

            root_alemao = Toplevel()
            root_alemao.title("Alemão")

            bandeira = Label(root_alemao, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_alemao = Label(root_alemao, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_alemao.grid(row=1, column=0)

        if self.idioma == "Grego":
            self.texto = grego

            root_grego = Toplevel()
            root_grego.title("Grego")

            bandeira = Label(root_grego, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_grego = Label(root_grego, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_grego.grid(row=1, column=0)

        if self.idioma == "Hebraico":
            self.texto = hebraico

            root_hebraico = Toplevel()
            root_hebraico.title("Hebraico")

            bandeira = Label(root_hebraico, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_hebraico = Label(root_hebraico, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_hebraico.grid(row=1, column=0)

        if self.idioma == "Hindi":
            self.texto = hindi

            root_hindi = Toplevel()
            root_hindi.title("Hindi")

            bandeira = Label(root_hindi, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_hindi = Label(root_hindi, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_hindi.grid(row=1, column=0)

        if self.idioma == "Húngaro":
            self.texto = hungaro

            root_hungaro = Toplevel()
            root_hungaro.title("Húngaro")

            bandeira = Label(root_hungaro, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_hungaro = Label(root_hungaro, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_hungaro.grid(row=1, column=0)

        if self.idioma == "Indonésio":
            self.texto = indonesio

            root_indonesio = Toplevel()
            root_indonesio.title("Indonésio")

            bandeira = Label(root_indonesio, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_indonesio = Label(root_indonesio, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_indonesio.grid(row=1, column=0)

        if self.idioma == "Italiano":
            self.texto = italiano

            root_italiano = Toplevel()
            root_italiano.title("Italiano")

            bandeira = Label(root_italiano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_italiano = Label(root_italiano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_italiano.grid(row=1, column=0)

        if self.idioma == "Letoniano":
            self.texto = letoniano

            root_letoniano = Toplevel()
            root_letoniano.title("Letoniano")

            bandeira = Label(root_letoniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_letoniano = Label(root_letoniano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_letoniano.grid(row=1, column=0)

        if self.idioma == "Lituano":
            self.texto = lituano

            root_lituano = Toplevel()
            root_lituano.title("Lituano")

            bandeira = Label(root_lituano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_lituano = Label(root_lituano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_lituano.grid(row=1, column=0)

        if self.idioma == "Macedônio":
            self.texto = macedonio

            root_macedonio = Toplevel()
            root_macedonio.title("Macedônio")

            bandeira = Label(root_macedonio, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_macedonio = Label(root_macedonio, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_macedonio.grid(row=1, column=0)

        if self.idioma == "Malaio":
            self.texto = malaio

            root_malaio = Toplevel()
            root_malaio.title("Malaio")

            bandeira = Label(root_malaio, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_malaio = Label(root_malaio, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_malaio.grid(row=1, column=0)

        if self.idioma == "Norueguês":
            self.texto = noruegues

            root_noruegues = Toplevel()
            root_noruegues.title("Norueguês")

            bandeira = Label(root_noruegues, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_noruegues = Label(root_noruegues, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_noruegues.grid(row=1, column=0)

        if self.idioma == "Polonês":
            self.texto = polones

            root_polones = Toplevel()
            root_polones.title("Polonês")

            bandeira = Label(root_polones, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_polones = Label(root_polones, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_polones.grid(row=1, column=0)

        if self.idioma == "Português":
            self.texto = portugues

            root_portugues = Toplevel()
            root_portugues.title("Português")

            bandeira = Label(root_portugues, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_portugues = Label(root_portugues, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_portugues.grid(row=1, column=0)

        if self.idioma == "Romeno":
            self.texto = romeno

            root_romeno = Toplevel()
            root_romeno.title("Romeno")

            bandeira = Label(root_romeno, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_romeno = Label(root_romeno, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_romeno.grid(row=1, column=0)

        if self.idioma == "Russo":
            self.texto = russo

            root_russo = Toplevel()
            root_russo.title("Russo")

            bandeira = Label(root_russo, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_russo = Label(root_russo, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_russo.grid(row=1, column=0)

        if self.idioma == "Sérvio":
            self.texto = servio

            root_servio = Toplevel()
            root_servio.title("Sérvio")

            bandeira = Label(root_servio, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_servio = Label(root_servio, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_servio.grid(row=1, column=0)

        if self.idioma == "Eslovaco":
            self.texto = eslovaco

            root_eslovaco = Toplevel()
            root_eslovaco.title("Eslovaco")

            bandeira = Label(root_eslovaco, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_eslovaco = Label(root_eslovaco, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_eslovaco.grid(row=1, column=0)

        if self.idioma == "Esloveno":
            self.texto = esloveno

            root_esloveno = Toplevel()
            root_esloveno.title("Esloveno")

            bandeira = Label(root_esloveno, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_esloveno = Label(root_esloveno, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_esloveno.grid(row=1, column=0)

        if self.idioma == "Espanhol":
            self.texto = espanhol

            root_espanhol = Toplevel()
            root_espanhol.title("Espanhol")

            bandeira = Label(root_espanhol, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_espanhol = Label(root_espanhol, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_espanhol.grid(row=1, column=0)

        if self.idioma == "Sueco":
            self.texto = sueco

            root_sueco = Toplevel()
            root_sueco.title("Sueco")

            bandeira = Label(root_sueco, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_sueco = Label(root_sueco, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_sueco.grid(row=1, column=0)

        if self.idioma == "Tailandês":
            self.texto = tailandes

            root_tailandes = Toplevel()
            root_tailandes.title("Tailandês")

            bandeira = Label(root_tailandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_tailandes = Label(root_tailandes, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_tailandes.grid(row=1, column=0)

        if self.idioma == "Turco":
            self.texto = turco

            root_turco = Toplevel()
            root_turco.title("Turco")

            bandeira = Label(root_turco, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_turco = Label(root_turco, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_turco.grid(row=1, column=0)

        if self.idioma == "Ucraniano":
            self.texto = ucraniano

            root_ucraniano = Toplevel()
            root_ucraniano.title("Ucraniano")

            bandeira = Label(root_ucraniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_ucraniano = Label(root_ucraniano, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_ucraniano.grid(row=1, column=0)

        if self.idioma == "Vietnamita":
            self.texto = vietnamita

            root_vietnamita = Toplevel()
            root_vietnamita.title("Vietnamita")

            bandeira = Label(root_vietnamita, image=self.bandeira)
            bandeira.grid(row=0, column=0)
            bandeira.image = self.bandeira

            letreiro_vietnamita = Label(root_vietnamita, text=self.texto, font=("Arial", 20, "bold"))
            letreiro_vietnamita.grid(row=1, column=0)
