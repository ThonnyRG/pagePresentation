from view.widgets.button import button


class blueButton(button):
    def __init__(self, frame, message: str, action, x: int, y: int):
        super().__init__(frame)
        self.message = message
        self.x = x
        self.y = y
        self._setupButton()
        self.setAction(action)
       
    def _setupButton(self):
        (self.setText(self.message).
         setBackGround("#4285F4","#315b9e").
         setForeGround("#ffffff","#ffffff").
         setPlace(self.x, self.y)
         )
        