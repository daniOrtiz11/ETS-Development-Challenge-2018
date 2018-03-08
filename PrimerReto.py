"""
Primer Reto ETS CHALLENGE 2018
Autor: Daniel Ortiz Sanchez
"""

class CaminoCorto(object):
    
    def cargarDatos(self,n):
        i = 0
        mapa = {}
        while (i < n):
            mapa[i] = {}
            i = i +1
        
        mapa[0][1] = 30
        mapa[1][2] = 10
        mapa[1][4] = 115
        mapa[2][3] = 70
        mapa[3][4] = 75
        mapa[3][6] = 15
        mapa[4][5] = 75
        mapa[4][6] = 70
        mapa[4][8] = 30
        mapa[5][9] = 15 
        mapa[5][11] = 70
        mapa[6][10] = 70
        mapa[7][8] = 15
        mapa[7][10] = 10
        mapa[8][9] = 40
        mapa[9][12] = 50
        mapa[10][13] = 50
        mapa[11][12] = 20
        mapa[12][13] = 45
        mapa[12][15] = 20
        mapa[13][14] = 25
        mapa[14][15] = 15
        return mapa
    
    def traduccion(self):
        mapa = {}
        mapa[0] = "Orodruin"
        mapa[1] = "Minas Morgul"
        mapa[2] = "Minas Tirith"
        mapa[3] = "Edoras"
        mapa[4] = "Galadon"
        mapa[5] = "Goblin Town"
        mapa[6] = "Isengard"
        mapa[7] = "Ost-In-Edhil"
        mapa[8] = "Hollin Gate"
        mapa[9] = "Rivendell"
        mapa[10] = "Nin-In-Eilf"
        mapa[11] = "Fornost"
        mapa[12] = "Bree"
        mapa[13] = "Sarn Ford"
        mapa[14] = "Tuckburow"
        mapa[15] = "Hobbiton"
        return mapa
    
    def esValida(self,sol,k):
        i = 0
        valida = True
        while i < k and valida == True:
            if(sol[k] == sol[i]):
                valida = False
            i = i+1
        return valida
    
    def esSolucion(self,final,destino):
        if final == destino:
            return True
        else:
            return False
    
        
    
    def vueltaAtras(self, sol, n, k, mapaDistancias, coste,destino):
        i = 0
        while i < n:
            sol[k] = i
            if(sol[k] in mapaDistancias[sol[k-1]]):
                coste = coste + mapaDistancias[sol[k-1]][sol[k]]
                if(self.esValida(sol,k)):
                    if(self.esSolucion(sol[k],destino)):
                        if(coste < self.costeMejor):
                            self.costeMejor = coste
							#copia de sol a solMejor
                            self.solMejor = sol[:]
                    else:
                        self.vueltaAtras(sol,n,k+1,mapaDistancias,coste,destino);
                coste = coste - mapaDistancias[sol[k-1]][sol[k]]
    
            i += 1
        
    def main(self):
        print ("Calculando el camino más corto...")
        print ("Pasos a seguir: ")
        mapaTraduccionLugares = self.traduccion()
        N = len(mapaTraduccionLugares)
        mapaDistancias = self.cargarDatos(N)
        solucion = []
        i = 0
		#inicializacion de la solucion
        while i < N:
            solucion.append(-1)
            i += 1
        inicio = 0
        destino = N-1
        solucion[0] = inicio
		#se establece como coste mas largo posible 10000
        self.costeMejor = 10000
        self.solMejor = []
        self.vueltaAtras(solucion, N, 1, mapaDistancias, 0 ,destino)
        llegado = False;
        for step in self.solMejor:
            if step != -1 and llegado == False:
                if(step == destino):
                    llegado = True
                print(mapaTraduccionLugares[step])
        

if __name__ == '__main__':
    CaminoCorto().main()
    
    
    