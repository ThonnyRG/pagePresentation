from pathlib import Path


class settings:
    ASSETS_DIR = Path("Model/src")
    UV_LOGO_PATH = ASSETS_DIR / "uvLogo.jpg"
    UV_FLAG_PATH = ASSETS_DIR / "uvFlag.png"
   
    
    PDF_FORMAT = "Letter"
    DEFAULT_FONT = "Arial"
   
    LOGO_POSITION = {"x": 160,"y": 10,"w": 45,"h": 39}
    FLAG_POSITION = {"x": 0,"y": 178,"w": 130,"h": 100}