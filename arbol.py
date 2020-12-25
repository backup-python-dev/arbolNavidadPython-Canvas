
from tkinter import Tk,Canvas
from random import randint


class ChristmasTree:

    def __init__(self,master):
        self.master = master
        self.master.title("Christmas Tree")
        self.master.geometry('420x420')
        self.master.config(bg="#000")
        
        self.canvas = Canvas(self.master, 
         width=420,height=420,bg="white")
        
        self.canvas.place(x=0,y=0)
        self.snow = []
        self.contador = 0
       
        self.create_snowflakes()
        self.master.after(300,self.animation)
        
        self.canvas.create_rectangle(0,0,420,420,fill='black')
        self.canvas.create_polygon(60,160,340,160,200,90,fill='green')
        self.canvas.create_polygon(60,210,340,210,200,130,fill='green')
        self.canvas.create_polygon(60,270,340,270,200,170,fill='green')
        self.canvas.create_oval(320,160,350,175,fill='#17EED0')
        self.canvas.create_oval(60,160,90,175,fill='#08ECF7')
        self.canvas.create_oval(320,210,350,225,fill='#05A4FF')
        self.canvas.create_oval(60,210,90,225,fill='#2F45EC')
        self.canvas.create_oval(320,260,350,275,fill='#3C61A6')
        self.canvas.create_oval(60,260,90,275,fill='#EF5E06')
        self.canvas.create_rectangle(170,270,230,390,fill='brown')
        
        
        self.points =[200,140,210,110,
                    240,100,210,90,200,60,
                    190,90,160,100,190,110]
        
        self.star = self.canvas.create_polygon(self.points,
                                    fill='yellow', width=3)
        

    def create_snowflakes(self):
        r = randint(-400,400)
        self.flake = self.canvas.create_oval(r,20,r+3,13,fill='white')
        self.contador+=1
        self.snow.append(self.flake)
        if self.contador<100:
            self.master.after(30,self.create_snowflakes)
    
    def animation(self):
        while True:
            try:
                self.canvas.create_text(200,40,fill="white",font="Chilanka 20 bold",
                        text="¡Feliz Navidad coders!")
                for flake in self.snow:
                    coordenadas=self.canvas.coords(flake)
                    x,y=1,1
                    if coordenadas[0]>=400:
                        x=-400
                    if coordenadas[1]>=400:
                        y=-400
                    self.canvas.move(flake,x,y)
                self.canvas.update()
            except Exception:
                break
           
if __name__ == '__main__':
    root = Tk()
    window = ChristmasTree(root)
    window.animation()
    root.mainloop()