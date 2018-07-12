class Settings:

    #Initiate the eye, set the image used for the eye, as well as if it's a left or right eye
  def __init__(self):

    self.SCREEN_WIDTH      = 800
    self.SCREEN_HEIGHT     = 480
    self.DEADZONE_LIMIT    = 0.25
    self.SCREEN_MIDPOINT_X = self.SCREEN_WIDTH / 2
    self.SCREEN_MIDPOINT_Y = self.SCREEN_HEIGHT / 2
    self.SCREEN_THIRD_X    = int(230)
    self.APP_DIRECTORY     = "home/greg/face"
    self.BUTTONS_TO_EYES   = {
      1: "ball.gif",
      2: "blue_eye.png",
      3: "green_eye.png"
    }
