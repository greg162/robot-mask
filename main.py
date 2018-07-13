import sys, pygame, os, game
import screenobjects


pygame.init()
pygame.joystick.init()

game = game.Settings()


# Used to manage how fast the screen updates
clock     = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

# Get count of joysticks
joystick_count = pygame.joystick.get_count()
print("Number of joysticks: {}".format(joystick_count))


#Check the joystick is plugged in and initute it
try:
  pygame.joystick.Joystick(0)
except NameError:
  print("Could not find a joystick!")
  sys.exit()
else:
  print("Joystick found!")

joystick = pygame.joystick.Joystick(0)
joystick.init()

axes = joystick.get_numaxes()
print("Number of axes: {}".format(axes) )
buttons = joystick.get_numbuttons()
print("Number of buttons: {}".format(buttons) )


size   = width, height = game.SCREEN_WIDTH, game.SCREEN_HEIGHT
black  = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#Initiate the left and right eye
leftEye  = screenobjects.Eye("eyes/"+ game.BUTTONS_TO_EYES[1], True, game)
rightEye = screenobjects.Eye("eyes/"+ game.BUTTONS_TO_EYES[1], False, game)

#The game loop!
while 1:

  exitButton = joystick.get_button( 8 )
  if exitButton == 1:
    sys.exit()
    os.system('reboot')

  for button in game.BUTTONS_TO_EYES:
    buttonPress = joystick.get_button( button )
    if buttonPress == 1:
      leftEye  = screenobjects.Eye("eyes/"+ game.BUTTONS_TO_EYES[button], True, game)
      rightEye = screenobjects.Eye("eyes/"+ game.BUTTONS_TO_EYES[button], False, game)


  #If the quit event has been triggered, exit the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  #Update the location of the left and right eye
  leftEye.updateLocation(joystick, game)
  rightEye.updateLocation(joystick, game)

  #Update the items location
  screen.fill(black)
  screen.blit(leftEye.eye, leftEye.ballrect)
  screen.blit(rightEye.eye, rightEye.ballrect)
  pygame.display.flip()
