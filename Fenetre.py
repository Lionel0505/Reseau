import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import Metier as f


class Affiche():
    fenetre = tk.Tk()
    fenetre.title("Configuration")
    t1 = ttk
    t2 = ttk
    t4 = ttk
    t5 = ttk
    classe = ttk
    adresseReseauV = ttk

    def frameElement(self):
        self.lbl1 = ttk.Label(self.fenetre, text='Adresse IP', font=("Arial", 12))
        self.lbl1.place(x=10, y=10)

        self.t1 = ttk.Entry(width="40")
        self.t1.place(x=100, y=10)

        self.lbl4 = ttk.Label(self.fenetre, text='Préfixe', font=("Arial", 12))
        self.lbl4.place(x=10, y=40)

        self.t5 = ttk.Entry(width="40")
        self.t5.place(x=100, y=40)

        self.lbl2 = ttk.Label(self.fenetre, text='IP version', font=("Arial", 12))
        self.lbl2.place(x=10, y=70)

        self.t2 = ttk.Combobox(self.fenetre, state="readonly",
                               values=["IPv4", "IPv6"], width=37)
        self.t2.place(x=100, y=70)

        style = ttk.Style()
        style.configure("BW.TLabel", font=
        ('calibri', 11, 'bold'),
                        borderwidth='4', background="crimson", foreground="white")

        self.b1 = ttk.Button(self.fenetre, text='Valider',
                             command=self.click, style='BW.TLabel')
        self.b1.place(x=10, y=100)

    def click(self):
        if self.t1.get() == "":
            messagebox.showwarning("", "Entrer l'IP")
            return None

        classe = ttk
        masque = ttk
        adresseReseau = ttk
        adresseDiffusion = ttk
        prermierOrdre = ttk
        dernierOrdre = ttk
        hote = ttk
        nombreAdresse = ttk

        classeV = ttk
        masqueV = ttk
        adresseReseauV = ttk
        adresseDiffusionV = ttk
        prermierOrdreV = ttk
        dernierOrdreV = ttk
        hoteV = ttk
        nombreAdresseV = ttk

        ip = ttk
        ipV = ttk

        if self.t5.get() == "" and self.t2.get() == "IPv4":

            try:
                f.checkIpv4Format(self.t1.get(), self)
                f.getClass(self.t1.get())
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None

            frameIpv4 = tk.Tk()
            frameIpv4.title("IPv4")
            frameIpv4.geometry('450x180')
            self.classe = ttk.Label(frameIpv4, text='Classe', font=("Arial", 12))
            self.classe.place(x=7, y=10)
            self.classeV = ttk.Label(frameIpv4, text=f.getClass(self.t1.get()), font=("Arial", 12))
            self.classeV.place(x=130, y=10)
            self.masque = ttk.Label(frameIpv4, text='Masque', font=("Arial", 12))
            self.masque.place(x=7, y=30)
            self.masqueV = ttk.Label(frameIpv4, text=f.getMask(self.t1.get()), font=("Arial", 12))
            self.masqueV.place(x=130, y=30)
            self.adresseReseau = ttk.Label(frameIpv4, text='Réseau', font=("Arial", 12))
            self.adresseReseau.place(x=7, y=50)
            self.adresseReseauV = ttk.Label(frameIpv4,
                                            text=f.getNetworkAddress(self.t1.get(), f.getMask(self.t1.get())),
                                            font=("Arial", 12))
            self.adresseReseauV.place(x=130, y=50)
            self.adresseBroadcast = ttk.Label(frameIpv4, text='Diffusion', font=("Arial", 12))
            self.adresseBroadcast.place(x=7, y=70)
            self.adresseBroadcastV = ttk.Label(frameIpv4,
                                               text=f.getBroadcatAddress(self.t1.get(), f.getMask(self.t1.get())),
                                               font=("Arial", 12))
            self.adresseBroadcastV.place(x=130, y=70)
            self.premierOrdre = ttk.Label(frameIpv4, text='1er valide', font=("Arial", 12))
            self.premierOrdre.place(x=7, y=90)
            self.premierOrdreV = ttk.Label(frameIpv4, text=f.getFirstOrder(self.t1.get(), f.getMask(self.t1.get())),
                                           font=("Arial", 12))
            self.premierOrdreV.place(x=130, y=90)
            self.dernierOrdre = ttk.Label(frameIpv4, text='Dernier valide', font=("Arial", 12))
            self.dernierOrdre.place(x=7, y=110)
            self.dernierOrdreV = ttk.Label(frameIpv4, text=f.getLastOrder(self.t1.get(), f.getMask(self.t1.get())),
                                           font=("Arial", 12))
            self.dernierOrdreV.place(x=130, y=110)
            self.hote = ttk.Label(frameIpv4, text='Hôte', font=("Arial", 12))
            self.hote.place(x=7, y=130)
            self.hoteV = ttk.Label(frameIpv4, text=f.hostBit(self.t1.get()), font=("Arial", 12))
            self.hoteV.place(x=130, y=130)
            self.nombreAdresse = ttk.Label(frameIpv4, text='Nombre adresse', font=("Arial", 12))
            self.nombreAdresse.place(x=7, y=150)
            self.nombreAdresseV = ttk.Label(frameIpv4, text=f.getAddressNumber(self.t1.get()), font=("Arial", 12))
            self.nombreAdresseV.place(x=130, y=150)
            frameIpv4.configure(bg='silver')
            frameIpv4.mainloop()

        if self.t2.get() == "":
            messagebox.showwarning("", "Insérer la version IP")

        if self.t2.get() == "IPv4":

            try:
                f.checkIpv4Format(self.t1.get(), self)
                f.checkPrefix(self.t5.get(), "IPv4")
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None

            frameIpv4 = tk.Tk()
            frameIpv4.geometry('450x180')

            self.masque = ttk.Label(frameIpv4, text='Masque', font=("Arial", 12))
            self.masque.place(x=7, y=30)
            self.masqueV = ttk.Label(frameIpv4, text=f.getMaskSpecial(int(self.t5.get())), font=("Arial", 12))
            self.masqueV.place(x=120, y=30)
            self.adresseReseau = ttk.Label(frameIpv4, text='Réseau', font=("Arial", 12))
            self.adresseReseau.place(x=7, y=50)
            self.adresseReseauV = ttk.Label(frameIpv4, text=f.getNetworkAddress(self.t1.get(),
                                                                                f.getMaskSpecial(int(self.t5.get()))),
                                            font=("Arial", 12))
            self.adresseReseauV.place(x=120, y=50)
            self.adresseBroadcast = ttk.Label(frameIpv4, text='Diffusion', font=("Arial", 12))
            self.adresseBroadcast.place(x=7, y=70)
            self.adresseBroadcastV = ttk.Label(frameIpv4, text=f.getBroadcatAddress(self.t1.get(), f.getMaskSpecial(
                int(self.t5.get()))), font=("Arial", 12))
            self.adresseBroadcastV.place(x=120, y=70)
            self.premierOrdre = ttk.Label(frameIpv4, text='1er valide', font=("Arial", 12))
            self.premierOrdre.place(x=7, y=90)
            self.premierOrdreV = ttk.Label(frameIpv4,
                                           text=f.getFirstOrder(self.t1.get(), f.getMaskSpecial(int(self.t5.get()))),
                                           font=("Arial", 12))
            self.premierOrdreV.place(x=120, y=90)
            self.dernierOrdre = ttk.Label(frameIpv4, text='Dernier valide', font=("Arial", 12))
            self.dernierOrdre.place(x=7, y=110)
            self.dernierOrdreV = ttk.Label(frameIpv4,
                                           text=f.getLastOrder(self.t1.get(), f.getMaskSpecial(int(self.t5.get()))),
                                           font=("Arial", 12))
            self.dernierOrdreV.place(x=120, y=110)
            self.hote = ttk.Label(frameIpv4, text='Hôte', font=("Arial", 12))
            self.hote.place(x=7, y=130)
            self.hoteV = ttk.Label(frameIpv4, text=f.hostBitSpecial(int(self.t5.get())), font=("Arial", 12))
            self.hoteV.place(x=120, y=130)
            self.nombreAdresse = ttk.Label(frameIpv4, text='Nombre adresse', font=("Arial", 12))
            self.nombreAdresse.place(x=7, y=150)
            self.nombreAdresseV = ttk.Label(frameIpv4, text=f.getAddressNumberSpecial(int(self.t5.get())),
                                            font=("Arial", 12))
            self.nombreAdresseV.place(x=120, y=150)
            frameIpv4.configure(bg='silver')
            frameIpv4.mainloop()

        if self.t2.get() == "IPv6":
            try:
                f.checkIpv6Format(self.t1.get())
                f.checkPrefix(self.t5.get(), "IPv6")
            except Exception as e:
                messagebox.showwarning("", str(e))
                return None

            frameIpv6 = tk.Tk()
            frameIpv6.title("IPv6")
            frameIpv6.geometry('450x100')
            self.ip = ttk.Label(frameIpv6, text='IP', font=("Arial", 12))
            self.ip.place(x=7, y=30)
            self.ipV = ttk.Label(frameIpv6, text=f.compressedIpv6(self.t1.get()), font=("Arial", 12))
            self.ipV.place(x=130, y=30)
            self.adresseReseau = ttk.Label(frameIpv6, text='Adresse réseau', font=("Arial", 12))
            self.adresseReseau.place(x=7, y=50)
            self.adresseReseauV = ttk.Label(frameIpv6, text=f.networkAddress(self.t1.get(), int(self.t5.get())),
                                            font=("Arial", 12))
            self.adresseReseauV.place(x=130, y=50)
            frameIpv6.configure(bg='white')
            frameIpv6.mainloop()

    def frame(self):
        self.fenetre.geometry('360x144')
        self.fenetre.configure(bg='white')
        self.frameElement()
        self.fenetre.mainloop()


class Main:
    def main():
        Affiche().frame()

    if __name__ == '__main__':
        main()
