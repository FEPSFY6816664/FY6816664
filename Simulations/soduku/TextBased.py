import pygame as pg


vec = pg.Vector2
col = pg.color

DIM = vec(200, 200)

class Tile():
    def __init__(self, posib) -> None:
        


        pass





class Soduku():
    def __init__(self, n) -> None:
        self.display = pg.display.set_mode(DIM)




        self.n = n
        self.superBoard = [[[p+1 for p in range(n**2)] for x in range(n**2)] for y in range(n**2)]
        for i in self.superBoard:
            print(i)


        self.mainloop()


    def mainloop(self):
        



        pass


    def close(self):
        pass

        

        



if __name__ == "__main__":

    Soduku(2)



    pass