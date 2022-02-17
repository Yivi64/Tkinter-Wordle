import tkinter as tk


class Wordle:
    def __init__(self, word):
        root.bind("<KeyPress>", self.__key_press)
        self.__word = word
        self.__row = 0
        self.__col = 0
        self.__labels = []
        self.__current_row = ""
        for i in range(6):
            temp = []
            for j in range(5):
                label_border = tk.Frame(root, highlightbackground="black", highlightthickness=2)
                label = tk.Label(label_border, bg="#404040", font=("Arial", 25, "bold"), height=2, width=4, fg="white")
                label_border.grid(row=i, column=j)
                label.grid(row=i, column=j)
                temp.append(label)
            self.__labels.append(temp)

    def __key_press(self, event):
        if event.keysym == "BackSpace":
            if self.__col != 0:
                self.__labels[self.__row][self.__col - 1]["text"] = ""
                self.__col -= 1
                self.__current_row = self.__current_row[:-1]
        elif event.char.isalpha():
            self.__labels[self.__row][self.__col]["text"] = event.char.upper()
            self.__col += 1
            self.__current_row += event.char.lower()
            if self.__col == 5:
                if self.__row == 4:
                    self.__end_screen(False)
                    return
                self.__check_row()
                self.__row += 1
                self.__col = 0
                self.__current_row = ""

    def __check_row(self):
        word: str = self.__word
        if self.__current_row == self.__word:
            for i in range(5):
                self.__labels[self.__row][i]["bg"] = "#50C878"
            self.__end_screen(True)
            return
        for i, char in enumerate(self.__current_row):
            if char == self.__word[i]:
                self.__labels[self.__row][i]["bg"] = "#50C878"
            elif char in word:
                self.__labels[self.__row][i]["bg"] = "#FADA5E"
                word = word.replace(char, "-", 1)

    def __end_screen(self, win: bool):
        if win is True:
            text = "YOUWIN"
            index = 0
            for i in range(2, 4):
                for j in range(1, 4):
                    self.__labels[i][j]["bg"] = "#40E0D0"
                    self.__labels[i][j]["text"] = text[index]
                    index += 1
        else:
            root.bind("<KeyPress>", self.__do_nothing)
            text = "SUXLOL"
            index = 0
            for i in range(2, 4):
                for j in range(1, 4):
                    self.__labels[i][j]["bg"] = "#CA3433"
                    self.__labels[i][j]["text"] = text[index]
                    index += 1

        for i in range(5):
            self.__labels[5][i]["bg"] = "#50C878"
            self.__labels[5][i]["text"] = self.__word[i].upper()

    def __do_nothing(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wordle")
    Wordle("sussy")
    root.mainloop()
