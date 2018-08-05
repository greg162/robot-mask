import pygame
from math import sin, cos, radians, pi

class Eye:

  #Initiate the eye, set the image used for the eye, as well as if it's a left or right eye
  def __init__(self, imagePath, leftEye, game):
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
    self.eyeAngle        = 10

  #This function is used to update the location of the eyes as the angle changes
  def setEyeAngle(self, angle):
    self.eyeAngle = angle
  
  def levelEyes(self, game):
    d  = game.SCREEN_MIDPOINT_X - game.SCREEN_THIRD_X
    x0 = 0
    y0 = 0
    print self.eyeAngle
    theta_rad = pi/2 - radians(self.eyeAngle)
    self.rotateY = int(x0 + d*cos(theta_rad))
    self.rotateX = int(d - int(y0 + d*sin(theta_rad)))

  #This function is used to update the location of the eye on the screen.
  def updateLocation(self, joystick, game):

    self.levelEyes(game )


    #calulate the X position of an Eye
    #=================================
    rawXAxisValue = float(joystick.get_axis(0))
    #Calculate position of eye in the deadzone
    if (rawXAxisValue >= (game.DEADZONE_LIMIT * -1) ) and (rawXAxisValue <= game.DEADZONE_LIMIT):
      if(self.leftEye):
        self.ballrect.x = game.SCREEN_THIRD_X - self.centerPointX - self.rotateX
      else:
        self.ballrect.x = (game.SCREEN_WIDTH - game.SCREEN_THIRD_X) - self.centerPointX + self.rotateX
    #Calculate the position of the eye when the joystick is outside the deadzone
    else:
      pixelDifference = rawXAxisValue * game.SCREEN_THIRD_X

      if(self.leftEye):
        eyelocation_x   = game.SCREEN_THIRD_X + pixelDifference - self.centerPointX - self.rotateX
      else:
        eyelocation_x = (game.SCREEN_WIDTH - game.SCREEN_THIRD_X) + pixelDifference - self.centerPointX + self.rotateX

      self.ballrect.x = eyelocation_x

    #Calculate the Y position of an eye
    #==================================
    rawYAxisValue = joystick.get_axis(1)
    #Calculate position of eye in the deadzone
    if(self.leftEye):
      rotatePixels = self.rotateY * -1  
    else:
      rotatePixels = self.rotateY 


    if rawYAxisValue >= (game.DEADZONE_LIMIT * -1 ) and rawYAxisValue <= game.DEADZONE_LIMIT:
      self.ballrect.y = game.SCREEN_MIDPOINT_Y - self.centerPointY + rotatePixels
    #Calculate hte position of the eye when the joystick is outside the deadzone
    else:
      joy_stick_y   = ( rawYAxisValue + 1) / 2
      eyelocation_y = int( joy_stick_y * game.SCREEN_HEIGHT ) - self.centerPointY + rotatePixels
      self.ballrect.y = eyelocation_y   
