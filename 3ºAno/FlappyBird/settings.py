class Settings:
    """ Uma classe para armazenar as configurações do jogo """
    
    def __init__(self):
        """ Inicializar as nossas configurações """
       
        # Configurações da janela do jogo
        self.screen_width = 1600
        self.screen_height = 1000
        self.screen_background_img = "images/background.jpeg"
        self.bg_color = (230, 230, 230)

        self.bird_width = 20