#ceci est un commentaire
ballX = 0
ballY = 0
ballSpeedX = 5
ballSpeedY = 2
ballRadius = 5

racketwidth = 50
racketheight = 10
racketX = 0
racketY = 0

#ici on définit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    global ballX, ballY, racketX, racketY, racketwidth
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on définit la taille de la fenêtre
    size(400, 400)
    clear()
    #on définie la couleur avec laquelle on va remplir les formes suivantes
    #dessiner une ellipse permet de définir les coordonnés x et y, la largeur et l'hauteur de l'ellipse
    frameRate(50)
    ballX = width/2
    ballY = width/2
    
    racketX = mouseX - 25 - (racketwidth/2)
    racketY = height - 20

   
def draw():
    clear()
    drawRacket()
    drawBall()
   


def drawRacket():
     global racketX, racketY, racketwidth
     print("testfunction")
     fill(255)
     rect(racketX, racketY, racketwidth, 10)
     racketX =  mouseX - (racketwidth/2)
     

    
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius, racketX, racketY, racketwidth, racketheight
    global racketX, racketY, racketwidth, racketheight
    #circle(ballX, ballY, 2+ballRadius)
    
    ballX += ballSpeedX
    ballY += ballSpeedY
     
    if(ballY-ballRadius < 0):
         ballSpeedY *= -1
         ballY = ballRadius
    elif(ballY+ballRadius > height):
         ballSpeedY *= -1
         ballY = height-ballRadius
     
    if(ballX+ballRadius > width):
         ballSpeedX *= -1
         ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
         ballSpeedX *= -1
         ballX = ballRadius
     

    if(racketY < ballY+ballRadius < racketY+racketheight and ballSpeedY > 0):
        if(racketX < ballX < racketX + racketwidth):
            ballSpeedY *= -1
            ballY = racketY-ballRadius

    circle(ballX, ballY, 6+ballRadius)
