class Settings:
    """ Uma classe para armazenar as configurações do jogo """
    
    def __init__(self):
        """ Inicializar as nossas configurações """
       
        # Configurações da janela do jogo
        self.screen_width = 1600
        self.screen_height = 1000
        self.screen_background_img = "images/background.jpeg"
        self.bg_color = (230, 230, 230)

        #Cofigurações do passaro
        self.bird_width = 20
        self.gravity = 0.5
        self.bird_jump = 8

        # definições dos obstáculos
        self.obs_width = 100
        self.obs_gap = 250
        self.obs_distance = 500  
        self.bird_speed_x = 5        
