import sys

# A SOLUÇÃO PROPOSTA É BUSCAR A QUINA DO ANEL EM QUE ESTÁ O VALOR EM QUESTÃO E APARTIR DAI FAZER UMA BUSCA SEQUÊNCIAL

def main():
    lin = input().split(' ')
    while lin[0] != '0':
        tam = int(lin[0])
        val = int(lin[1])
        canto = int(val ** 0.5)
        if canto%2 == 0:
            canto -=1
        
        lin = col = ((tam//2) + 1) + (canto -2)//2 + 1

        atual = canto **2

        if val > atual + canto*2 + 2:
            atual += canto*2 + 2
            col -= canto
            lin -= canto

            if val < atual + canto + 1:
                for k in range(0,canto+1):
                    if atual != val:
                        col +=1
                        atual +=1
                    else:
                        break
            else:
                col += canto + 1
                atual += canto + 1
                for l in range(0,canto):
                    if atual != val:
                        lin +=1
                        atual +=1
                    else:
                        break

        elif atual != val:
            lin +=1
            atual+=1
            if val < atual + canto:
                for i in range(0,canto):
                    if atual != val:
                        col -=1
                        atual +=1
                    else:
                        break
            else:
                col -= canto
                atual += canto
                for j in range(0,canto+1):
                    if atual != val:
                        lin -=1
                        atual +=1
                    else:
                        break
            
        print ("Line = %d, column = %d."%(lin,col))
            


        

        lin = input().split(' ')
        

if __name__ == "__main__":
    main()