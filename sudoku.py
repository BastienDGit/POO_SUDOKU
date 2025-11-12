import numpy as np
from tkinter import Tk, Button, Entry, messagebox, StringVar, Label
import random
import time

def init_sudoku():
    return np.zeros((9, 9), dtype=int)

def est_valide(M, row, col, num):
    if num in M[row]:
        return False
    if num in M[:, col]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if M[r][c] == num:
                return False
    return True

def remplir_grille(M):
    for i in range(9):
        for j in range(9):
            if M[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if est_valide(M, i, j, num):
                        M[i][j] = num
                        if remplir_grille(M):
                            return True
                        M[i][j] = 0
                return False
    return True

def enlever_chiffres(solution, niveau):
    grille = solution.copy()
    nb_chiffres = {
        'facile': 30,
        'moyen': 40,
        'expert': 50,
        'maître': 60
    }.get(niveau, 30)

    cases = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cases)
    for _ in range(nb_chiffres):
        i, j = cases.pop()
        grille[i][j] = 0
    return grille

def reinitialiser_grille():
    global solution, grille, app
    app.vies = 3
    app.label_vies.config(text=f"❤️ Vies : {app.vies}")
    app.start_time = time.time()

    solution = init_sudoku()
    remplir_grille(solution)
    grille = enlever_chiffres(solution, app.niveau)

    for i in range(9):
        for j in range(9):
            entry, var = app.entries[i][j]
            entry.config(state='normal', bg=app.bg_color(i, j), fg="green")
            var.set('')
            if grille[i][j] != 0:
                var.set(str(grille[i][j]))
                entry.config(state='readonly', fg="black", disabledforeground="black")

class SudokuGUI:
    def __init__(self, root):
        global app
        app = self
        self.root = root
        self.root.title("🧩 Sudoku Deluxe")
        self.root.configure(bg="#f7f7f7")

        self.niveau = 'facile'
        self.vies = 3
        self.start_time = time.time()

        
        self.header = Label(self.root, text="🧩 Sudoku Deluxe", font=("Helvetica", 20, "bold"),
                            bg="#4C5B61", fg="white", pady=10)
        self.header.grid(row=0, column=0, columnspan=9, sticky="ew")

       
        self.entries = []
        for i in range(9):
            row_entries = []
            for j in range(9):
                var = StringVar()
                entry = Entry(self.root, width=2, font=('Arial', 30, 'bold'),
                              justify='center', bd=1, relief='solid',
                              bg=self.bg_color(i, j), textvariable=var, fg="green")
                entry.grid(row=i+1, column=j, padx=1, pady=1)
                entry.bind("<FocusIn>", self.on_focus_in)
                entry.bind("<FocusOut>", self.on_focus_out)
                var.trace_add("write", lambda *args, r=i, c=j: self.verifier_case(r, c))
                row_entries.append((entry, var))
            self.entries.append(row_entries)

        
        self.bouton_verifier = Button(self.root, text="✅ Vérifier", command=self.verifier_solution,
                                      bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'), width=10)
        self.bouton_verifier.grid(row=10, column=0, columnspan=3, pady=10)

        self.bouton_reinitialiser = Button(self.root, text="🔁 Réinitialiser", command=reinitialiser_grille,
                                           bg="#2196F3", fg="white", font=('Arial', 12, 'bold'), width=12)
        self.bouton_reinitialiser.grid(row=10, column=3, columnspan=3, pady=10)

        self.menu_niveau = Button(self.root, text="🎯 Niveau: Facile", command=self.changer_niveau,
                                  bg="#FF9800", fg="white", font=('Arial', 12, 'bold'), width=14)
        self.menu_niveau.grid(row=10, column=6, columnspan=3, pady=10)

        
        self.label_vies = Label(self.root, text=f"❤️ Vies : {self.vies}", font=('Arial', 12, 'bold'),
                                bg="#f7f7f7", fg="#d32f2f")
        self.label_vies.grid(row=11, column=0, columnspan=4)

        self.timer_label = Label(self.root, text="⏱ Temps : 0s", font=('Arial', 12, 'bold'),
                                 bg="#f7f7f7", fg="#555")
        self.timer_label.grid(row=11, column=5, columnspan=4)

        self.update_timer()
        reinitialiser_grille()

    
    def bg_color(self, i, j):
        return "#e8e8e8" if (i//3 + j//3) % 2 == 0 else "#ffffff"

    
    def on_focus_in(self, event):
        event.widget.config(bg="#c6f6ff")

    def on_focus_out(self, event):
        i, j = self.find_entry(event.widget)
        event.widget.config(bg=self.bg_color(i, j))

    def find_entry(self, widget):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j][0] == widget:
                    return i, j
        return None, None

    
    def changer_niveau(self):
        niveaux = ['facile', 'moyen', 'expert', 'maître']
        index = niveaux.index(self.niveau)
        self.niveau = niveaux[(index + 1) % len(niveaux)]
        self.menu_niveau.config(text=f"🎯 Niveau: {self.niveau.capitalize()}")
        reinitialiser_grille()

    
    def flash_vies(self):
        for _ in range(3):
            self.label_vies.config(fg="red")
            self.root.update()
            self.root.after(150)
            self.label_vies.config(fg="#d32f2f")
            self.root.update()
            self.root.after(150)

    
    def victory_animation(self):
        colors = ["#b3ffb3", "#80ff80", "#f7f7f7"]
        for color in colors * 2:
            self.root.configure(bg=color)
            self.root.update()
            self.root.after(150)
        self.root.configure(bg="#f7f7f7")

    
    def game_over_animation(self):
        colors = ["#ffb3b3", "#ff6666", "#f7f7f7"]
        for color in colors * 2:
            self.root.configure(bg=color)
            self.root.update()
            self.root.after(150)
        self.root.configure(bg="#f7f7f7")

    
    def verifier_case(self, row, col, *args):
        entry, var = self.entries[row][col]
        value = var.get()
        if value.isdigit() and int(value) != 0:
            valeur = int(value)
            if valeur != solution[row, col]:
                entry.config(bg="#ffcccc")
                self.root.after(500, lambda: entry.config(bg=self.bg_color(row, col)))
                if self.vies > 0:
                    self.vies -= 1
                    self.label_vies.config(text=f"❤️ Vies : {self.vies}")
                    self.flash_vies()
                    messagebox.showwarning("Erreur", f"❌ Mauvaise valeur ! Il vous reste {self.vies} vies.")
                    var.set("")
                    if self.vies == 0:
                        self.game_over_animation()
                        messagebox.showerror("💀 Game Over", "Vous avez perdu toutes vos vies.")
                        reinitialiser_grille()
            else:
                entry.config(fg="green")
        else:
            entry.config(fg="green")

    
    def verifier_solution(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j][1].get()
                if value == '' or int(value) != solution[i, j]:
                    messagebox.showwarning("⚠️ Vérification", "Le puzzle n'est pas encore résolu correctement.")
                    return
        self.victory_animation()
        messagebox.showinfo("🎉 Victoire", "Félicitations ! Vous avez terminé le Sudoku.")

    
    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        self.timer_label.config(text=f"⏱ Temps : {elapsed}s")
        self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = Tk()
    app = SudokuGUI(root)
    solution = init_sudoku()
    grille = init_sudoku()
    root.mainloop()
