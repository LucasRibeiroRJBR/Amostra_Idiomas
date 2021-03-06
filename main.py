import tkinter.ttk as ttk
from tkinter import *

from ttkthemes import ThemedStyle

from uteis.comandos_botao import *

root = Tk()

style_alt = ThemedStyle(root)
style_alt.set_theme('breeze')


botao_ale = ttk.Button(root, text="Alemão", command=bt_alemao, width=15)
botao_ara = ttk.Button(root, text="Árabe", command=bt_arabe, width=15)
botao_arm = ttk.Button(root, text="Armênio", command=bt_armeno, width=15)
botao_bul = ttk.Button(root, text="Búlgaro", command=bt_bulgado, width=15)
botao_cro = ttk.Button(root, text="Croata", command=bt_croata, width=15)
botao_din = ttk.Button(root, text="Dinamarquês", command=bt_dinamarques, width=15)
botao_esl = ttk.Button(root, text="Eslovaco", command=bt_eslovaco, width=15)
botao_eslo = ttk.Button(root, text="Esloveno", command=bt_esloveno, width=15)
botao_esp = ttk.Button(root, text="Espanhol", command=bt_espanhol, width=15)
botao_est = ttk.Button(root, text="Estoniano", command=bt_estoniano, width=15)
botao_fil = ttk.Button(root, text="Filipino", command=bt_filipino, width=15)
botao_fin = ttk.Button(root, text="Finlandês", command=bt_finlandes, width=15)
botao_fra = ttk.Button(root, text="Francês", command=bt_frances, width=15)
botao_geo = ttk.Button(root, text="Georgiano", command=bt_georgiano, width=15)
botao_gre = ttk.Button(root, text="Grego", command=bt_grego, width=15)
botao_heb = ttk.Button(root, text="Hebraico", command=bt_hebraico, width=15)
botao_hin = ttk.Button(root, text="Hindi", command=bt_hindi, width=15)
botao_hol = ttk.Button(root, text="Holandês", command=bt_holandes, width=15)
botao_hun = ttk.Button(root, text="Húngaro", command=bt_hungaro, width=15)
botao_ind = ttk.Button(root, text="Indonésio", command=bt_indonesio, width=15)
botao_ing = ttk.Button(root, text="Inglês", command=bt_ingles, width=15)
botao_ita = ttk.Button(root, text="Italiano", command=bt_italiano, width=15)
botao_let = ttk.Button(root, text="Letoniano", command=bt_letoniano, width=15)
botao_lit = ttk.Button(root, text="Lituano", command=bt_lituano, width=15)
botao_mac = ttk.Button(root, text="Macedônio", command=bt_macedonio, width=15)
botao_mal = ttk.Button(root, text="Malaio", command=bt_malaio, width=15)
botao_man = ttk.Button(root, text="Mandarim", command=bt_mandarim, width=15)
botao_nor = ttk.Button(root, text="Norueguês", command=bt_noruegues, width=15)
botao_pol = ttk.Button(root, text="Polonês", command=bt_polones, width=15)
botao_por = ttk.Button(root, text="Português", command=bt_portugues, width=15)
botao_rom = ttk.Button(root, text="Romeno", command=bt_romeno, width=15)
botao_rus = ttk.Button(root, text="Russo", command=bt_russo, width=15)
botao_ser = ttk.Button(root, text="Sérvio", command=bt_servio, width=15)
botao_sue = ttk.Button(root, text="Sueco", command=bt_sueco, width=15)
botao_tail = ttk.Button(root, text="Tailandês", command=bt_tailandes, width=15)
botao_tai = ttk.Button(root, text="Taiwanês", command=bt_taiwanes, width=15)
botao_tch = ttk.Button(root, text="Tcheco", command=bt_tcheco, width=15)
botao_tur = ttk.Button(root, text="Turco", command=bt_turco, width=15)
botao_ucr = ttk.Button(root, text="Ucraniano", command=bt_ucraniano, width=15)
botao_vie = ttk.Button(root, text="Vietnamita", command=bt_vietnamita, width=15)

botao_ale.grid(row=0, column=0, padx=2, pady=2)
botao_ara.grid(row=0, column=1, padx=2, pady=2)
botao_arm.grid(row=0, column=2, padx=2, pady=2)
botao_bul.grid(row=0, column=3, padx=2, pady=2)
botao_cro.grid(row=0, column=4, padx=2, pady=2)
botao_din.grid(row=0, column=5, padx=2, pady=2)
botao_esl.grid(row=0, column=6, padx=2, pady=2)
botao_eslo.grid(row=0, column=7, padx=2, pady=2)
botao_esp.grid(row=1, column=0, padx=2, pady=2)
botao_est.grid(row=1, column=1, padx=2, pady=2)
botao_fil.grid(row=1, column=2, padx=2, pady=2)
botao_fin.grid(row=1, column=3, padx=2, pady=2)
botao_fra.grid(row=1, column=4, padx=2, pady=2)
botao_geo.grid(row=1, column=5, padx=2, pady=2)
botao_gre.grid(row=1, column=6, padx=2, pady=2)
botao_heb.grid(row=1, column=7, padx=2, pady=2)
botao_hin.grid(row=2, column=0, padx=2, pady=2)
botao_hol.grid(row=2, column=1, padx=2, pady=2)
botao_hun.grid(row=2, column=2, padx=2, pady=2)
botao_ind.grid(row=2, column=3, padx=2, pady=2)
botao_ing.grid(row=2, column=4, padx=2, pady=2)
botao_ita.grid(row=2, column=5, padx=2, pady=2)
botao_let.grid(row=2, column=6, padx=2, pady=2)
botao_lit.grid(row=2, column=7, padx=2, pady=2)
botao_mac.grid(row=3, column=0, padx=2, pady=2)
botao_mal.grid(row=3, column=1, padx=2, pady=2)
botao_man.grid(row=3, column=2, padx=2, pady=2)
botao_nor.grid(row=3, column=3, padx=2, pady=2)
botao_pol.grid(row=3, column=4, padx=2, pady=2)
botao_por.grid(row=3, column=5, padx=2, pady=2)
botao_rom.grid(row=3, column=6, padx=2, pady=2)
botao_rus.grid(row=3, column=7, padx=2, pady=2)
botao_ser.grid(row=4, column=0, padx=2, pady=2)
botao_sue.grid(row=4, column=1, padx=2, pady=2)
botao_tail.grid(row=4, column=2, padx=2, pady=2)
botao_tai.grid(row=4, column=3, padx=2, pady=2)
botao_tch.grid(row=4, column=4, padx=2, pady=2)
botao_tur.grid(row=4, column=5, padx=2, pady=2)
botao_ucr.grid(row=4, column=6, padx=2, pady=2)
botao_vie.grid(row=4, column=7, padx=2, pady=2)

root.mainloop()
