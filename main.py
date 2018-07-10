import sys, pygame, os
from math import sin, cos, radians, pi

pygame.init()
pygame.joystick.init()

# Set Constants
SCREEN_WIDTH      = 800
SCREEN_HEIGHT     = 480
DEADZONE_LIMIT    = 0.25
SCREEN_MIDPOINT_X = SCREEN_WIDTH / 2
SCREEN_MIDPOINT_Y = SCREEN_HEIGHT / 2
SCREEN_THIRD_X    = int(230)
APP_DIRECTORY     = "home/greg/face"
BUTTONS_TO_EYES   = {
  1: "ball.gif",
  2: "blue_eye.png",
  3: "green_eye.png"
}


class Eye:

  #Initiate the eye, set the image used for the eye, as well as if it's a left or right eye
  def __init__(self, imagePath, leftEye):
    self.leftEye         = leftEye
    self.eye             = pygame.image.load(imagePath)
    self.ballrect        = self.eye.get_rect()
    self.eyeWidth        = self.ballrect.width
    self.eyeHeight       = self.ballrect.height
    self.centerPointX    = int(self.eyeWidth / 2)
    self.centerPointY    = int(self.eyeWidth / 2)
    self.ballrect.center = [self.centerPointX, self.centerPointY]
    self.rotateX         = 0
    self.rotateY         = 0

  #This function is used to update the location of the eyes as the angle changes
  def levelEyes(self, theta):
    d  = SCREEN_MIDPOINT_X - SCREEN_THIRD_X
    x0 = 0
    y0 = 0
    theta_rad = pi/2 - radians(theta)
    self.rotateY = int(x0 + d*cos(theta_rad))
    self.rotateX = int(d - int(y0 + d*sin(theta_rad)))

  #This function is used to update the location of the eye on the screen.
  def updateLocation(self, joystick):

    self.levelEyes( 6 )


    #calulate the X position of an Eye
    #=================================
    rawXAxisValue = float(joystick.get_axis(0))
    #Calculate position of eye in the deadzone
    if (rawXAxisValue >= (DEADZONE_LIMIT * -1) ) and (rawXAxisValue <= DEADZONE_LIMIT):
      if(self.leftEye):
        self.ballrect.x = SCREEN_THIRD_X - self.centerPointX - self.rotateX
      else:
        self.ballrect.x = (SCREEN_WIDTH - SCREEN_THIRD_X) - self.centerPointX + self.rotateX
    #Calculate the position of the eye when the joystick is outside the deadzone
    else:
      pixelDifference = rawXAxisValue * SCREEN_THIRD_X

      if(self.leftEye):
        eyelocation_x   = SCREEN_THIRD_X + pixelDifference - self.centerPointX - self.rotateX
      else:
        eyelocation_x = (SCREEN_WIDTH - SCREEN_THIRD_X) + pixelDifference - self.centerPointX + self.rotateX

      self.ballrect.x = eyelocation_x

    #Calculate the Y position of an eye
    #==================================
    rawYAxisValue = joystick.get_axis(1)
    #Calculate position of eye in the deadzone
    if(self.leftEye):
      rotatePixels = self.rotateY * -1  
    else:
      rotatePixels = self.rotateY 


    if rawYAxisValue >= (DEADZONE_LIMIT * -1 ) and rawYAxisValue <= DEADZONE_LIMIT:
      self.ballrect.y = SCREEN_MIDPOINT_Y - self.centerPointY + rotatePixels
    #Calculate hte position of the eye when the joystick is outside the deadzone
    else:
      joy_stick_y   = ( rawYAxisValue + 1) / 2
      eyelocation_y = int( joy_stick_y * SCREEN_HEIGHT ) - self.centerPointY + rotatePixels
      self.ballrect.y = eyelocation_y   


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


size   = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
black  = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#Initiate the left and right eye
leftEye  = Eye("eyes/"+ BUTTONS_TO_EYES[1], True)
rightEye = Eye("eyes/"+ BUTTONS_TO_EYES[1], False)

#The game loop!
while 1:

  exitButton = joystick.get_button( 8 )
  if exitButton == 1:
    sys.exit()
    os.system('reboot')

  for button in BUTTONS_TO_EYES:
    buttonPress = joystick.get_button( button )
    if buttonPress == 1:
      leftEye  = Eye("eyes/"+ BUTTONS_TO_EYES[button], True)
      rightEye = Eye("eyes/"+ BUTTONS_TO_EYES[button], False)


  #If the quit event has been triggered, exit the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  #Update the location of the left and right eye
  leftEye.updateLocation(joystick)
  rightEye.updateLocation(joystick)

  #Update the items location
  screen.fill(black)
  screen.blit(leftEye.eye, leftEye.ballrect)
  screen.blit(rightEye.eye, rightEye.ballrect)
  pygame.display.flip()
