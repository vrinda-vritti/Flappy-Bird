from tkinter import *
from tkinter import messagebox as mb
import json
import random

root = Tk()
root.geometry("288x512")
root.title("Flappy's Trap !")

with open('quiz.json') as f:
    obj = json.load(f)

q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])
z = zip(q, options, a)
l = list(z)
random.shuffle(l)


class Quiz:
    def __init__(self):
        self.qn = 0
        self.qno = 1
        self.quest = StringVar()
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Flappy's Questions", width=16, bg="Yellow", fg="Green", font=("times", 20, "bold"))
        t.place(x=10, y=0)
        self.quest.set(str(self.qno) + ". " + q[qn])
        qn = Label(root, textvariable=self.quest, width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=50, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=50, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="yellow",
                         font=("times", 16, "bold"))
        nbutton.place(x=10, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="yellow", fg="green",
                            font=("times", 16, "bold"))
        quitbutton.place(x=150, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        self.qno += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.quest.set(str(self.qno) + "." + q[self.qn])
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))


quiz = Quiz()
root.mainloop()
