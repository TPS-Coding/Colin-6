from settings import *
from sprites import Player, Ball, Opponent
import sys 



class Game():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player_score = 0
        self.cpu_score = 0
        self.font = pygame.font.Font(None,160)




        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()

        self.player = Player((self.all_sprites,self.paddle_sprites))
        #self.ball = Ball(self.all_sprites, self.paddle_sprites)
        
        self.ball = Ball(self.all_sprites, self.paddle_sprites)
            
        self.opponent = Opponent((self.all_sprites,self.paddle_sprites),self.ball)

    
    def score(self):

        if self.ball.rect.right <= 0:
            self.player_score += 1
            self.ball.rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        if self.ball.rect.left >= WINDOW_WIDTH:
            self.cpu_score += 1
            self.ball.rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    def display_score(self):
        player_surf = self.font.render(str(self.player_score),True,'white')
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH*0.6, WINDOW_HEIGHT/2))    
        self.display_surface.blit(player_surf, player_rect)

        cpu_surf = self.font.render(str(self.cpu_score), True, 'white')
        cpu_rect = cpu_surf.get_frect(center = (WINDOW_WIDTH*0.4, WINDOW_HEIGHT/2))
        self.display_surface.blit(cpu_surf, cpu_rect)

        start = (WINDOW_WIDTH/2, 0)
        end = (WINDOW_WIDTH/2, WINDOW_HEIGHT)
        pygame.draw.line(self.display_surface, 'white', start, end, 10)
    
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()


            # update
            self.all_sprites.update(dt)
            self.score()

            # draw
            self.display_surface.fill(COLORS["bg"])
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            pygame.display.update()
        pygame.quit()
if __name__ == "__main__":
    game = Game()       
    game.run()
