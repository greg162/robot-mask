class Settings:

    #Initiate the eye, set the image used for the eye, as well as if it's a left or right eye
  def __init__(self):

    self.SCREEN_WIDTH      = 800
    self.SCREEN_HEIGHT     = 480
    self.DEADZONE_LIMIT    = 0.20
    self.REVERSE_X_EYES    = True #When wearing, you'll want to reverse the X axis of the eyes.
    self.SCREEN_MIDPOINT_X = self.SCREEN_WIDTH / 2
    self.SCREEN_MIDPOINT_Y = self.SCREEN_HEIGHT / 2
    self.SCREEN_THIRD_X    = int(150)
    self.APP_DIRECTORY     = "home/greg/face"
    self.BUTTONS_TO_EYES   = {
      1: "red_eye.png",
      2: "blue_eye.png",
      3: "green_eye.png"
    }
    self.COLORS_TO_EYES   = {
      1: 0XFF0000, #red
      2: 0x0000FF, #blue
      3: 0x00FF00, #Green
    }

