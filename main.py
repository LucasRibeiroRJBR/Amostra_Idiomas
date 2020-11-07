import tkinter.ttk as ttk
from tkinter import *

from ttkthemes import ThemedStyle

from uteis.comandos_botao import *

root = Tk()

style_alt = ThemedStyle(root)
style_alt.set_theme('breeze')


botao = ttk.Button(root, text="Alemão", command=bt_alemao, width=15)
botao.grid(row=0, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Árabe", command=bt_arabe, width=15)
botao.grid(row=0, column=1, padx=10, pady=10)

botao = ttk.Button(root, text="Armênio", command=bt_armeno, width=15)
botao.grid(row=0, column=2, padx=10, pady=10)

botao = ttk.Button(root, text="Búlgaro", command=bt_bulgado, width=15)
botao.grid(row=0, column=3, padx=10, pady=10)

botao = ttk.Button(root, text="Croata", command=bt_croata, width=15)
botao.grid(row=0, column=4, padx=10, pady=10)

botao = ttk.Button(root, text="Dinamarquês", command=bt_dinamarques, width=15)
botao.grid(row=0, column=5, padx=10, pady=10)

botao = ttk.Button(root, text="Eslovaco", command=bt_eslovaco, width=15)
botao.grid(row=0, column=6, padx=10, pady=10)

botao = ttk.Button(root, text="Esloveno", command=bt_esloveno, width=15)
botao.grid(row=0, column=7, padx=10, pady=10)

botao = ttk.Button(root, text="Espanhol", command=bt_espanhol, width=15)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Estoniano", command=bt_estoniano, width=15)
botao.grid(row=1, column=1, padx=10, pady=10)

botao = ttk.Button(root, text="Filipino", command=bt_filipino, width=15)
botao.grid(row=1, column=2, padx=10, pady=10)

botao = ttk.Button(root, text="Finlandês", command=bt_finlandes, width=15)
botao.grid(row=1, column=3, padx=10, pady=10)

botao = ttk.Button(root, text="Francês", command=bt_frances, width=15)
botao.grid(row=1, column=4, padx=10, pady=10)

botao = ttk.Button(root, text="Georgiano", command=bt_georgiano, width=15)
botao.grid(row=1, column=5, padx=10, pady=10)

botao = ttk.Button(root, text="Grego", command=bt_grego, width=15)
botao.grid(row=1, column=6, padx=10, pady=10)

botao = ttk.Button(root, text="Hebraico", command=bt_hebraico, width=15)
botao.grid(row=1, column=7, padx=10, pady=10)

botao = ttk.Button(root, text="Hindi", command=bt_hindi, width=15)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Holandês", command=bt_holandes, width=15)
botao.grid(row=2, column=1, padx=10, pady=10)

botao = ttk.Button(root, text="Húngaro", command=bt_hungaro, width=15)
botao.grid(row=2, column=2, padx=10, pady=10)

botao = ttk.Button(root, text="Indonesiano", command=bt_indonesiano, width=15)
botao.grid(row=2, column=3, padx=10, pady=10)

botao = ttk.Button(root, text="Inglês", command=bt_ingles, width=15)
botao.grid(row=2, column=4, padx=10, pady=10)

botao = ttk.Button(root, text="Italiano", command=bt_italiano, width=15)
botao.grid(row=2, column=5, padx=10, pady=10)

botao = ttk.Button(root, text="Letoniano", command=bt_letoniano, width=15)
botao.grid(row=2, column=6, padx=10, pady=10)

botao = ttk.Button(root, text="Lituano", command=bt_lituano, width=15)
botao.grid(row=2, column=7, padx=10, pady=10)

botao = ttk.Button(root, text="Macedônio", command=bt_macedonio, width=15)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Malaio", command=bt_malaio, width=15)
botao.grid(row=3, column=1, padx=10, pady=10)

botao = ttk.Button(root, text="Mandarim", command=bt_mandarim, width=15)
botao.grid(row=3, column=2, padx=10, pady=10)

botao = ttk.Button(root, text="Norueguês", command=bt_noruegues, width=15)
botao.grid(row=3, column=3, padx=10, pady=10)

botao = ttk.Button(root, text="Polonês", command=bt_polones, width=15)
botao.grid(row=3, column=4, padx=10, pady=10)

botao = ttk.Button(root, text="Português", command=bt_portugues, width=15)
botao.grid(row=3, column=5, padx=10, pady=10)

botao = ttk.Button(root, text="Romeno", command=bt_romeno, width=15)
botao.grid(row=3, column=6, padx=10, pady=10)

botao = ttk.Button(root, text="Russo", command=bt_russo, width=15)
botao.grid(row=3, column=7, padx=10, pady=10)

botao = ttk.Button(root, text="Sérvio", command=bt_servio, width=15)
botao.grid(row=4, column=0, padx=10, pady=10)

botao = ttk.Button(root, text="Sueco", command=bt_sueco, width=15)
botao.grid(row=4, column=1, padx=10, pady=10)

botao = ttk.Button(root, text="Tailandês", command=bt_tailandes, width=15)
botao.grid(row=4, column=2, padx=10, pady=10)

botao = ttk.Button(root, text="Taiwanês", command=bt_taiwanes, width=15)
botao.grid(row=4, column=3, padx=10, pady=10)

botao = ttk.Button(root, text="Tcheco", command=bt_tcheco, width=15)
botao.grid(row=4, column=4, padx=10, pady=10)

botao = ttk.Button(root, text="Turco", command=bt_turco, width=15)
botao.grid(row=4, column=5, padx=10, pady=10)

botao = ttk.Button(root, text="Ucraniano", command=bt_ucraniano, width=15)
botao.grid(row=4, column=6, padx=10, pady=10)

botao = ttk.Button(root, text="Vietnamita", command=bt_vietnamita, width=15)
botao.grid(row=4, column=7, padx=10, pady=10)

root.mainloop()
