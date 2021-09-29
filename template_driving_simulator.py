import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=780
height=360
screen = pygame.display.set_mode((width,height))
  
# Creating a dictionary 'images' and loading the images into the dictionary
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["car"] = pygame.image.load("car1.png").convert_alpha()
groundx=0

class Vehicle:
    rect= pygame.Rect(100,200,30,30)
   
    def display(self):
        screen.blit(images["car"],self.rect) 
        
    def moveLeft(self):
        self.rect.y=self.rect.y-100
        
    # Create a function 'moveRight' to increment the y-coordinate of the rect by 10
        
    
# Create an object for 'Vehicle' class and name it as 'car'


while True:    
    screen.fill((50,150,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.moveLeft()
            if event.key == pygame.K_RIGHT:
                car.moveRight()
                        
    
    groundx=groundx-5
    if(groundx < -190):
        groundx=0
   
    
    screen.blit(images["bg"],[groundx,0]) 
    # Call the 'display' function using the 'car' object
    
    
    
    pygame.display.update()
    clock.tick(30)
