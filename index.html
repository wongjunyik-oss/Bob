import pygame
import pymunk
import pymunk.pygame_util
import random

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
FPS = 60
COLLISION_PLAYER = 1
COLLISION_AI = 2

class Ragdoll:
    def __init__(self, space, pos, color, collision_type, is_player=True):
        self.space = space
        self.color = color
        self.is_player = is_player
        self.health = 100
        
        # 1. Create Core Body (Torso)
        self.torso = self._add_box(pos, (25, 50), 1.0, collision_type)
        # 2. Create Head
        self.head = self._add_circle((pos[0], pos[1]-45), 12, 0.5, collision_type)
        self._connect(self.torso, self.head, (0, -25), (0, 15))
        # 3. Create Arms
        self.r_arm = self._add_box((pos[0]+30, pos[1]-15), (30, 12), 0.5, collision_type)
        self._connect(self.torso, self.r_arm, (15, -20), (-15, 0))
        self.l_arm = self._add_box((pos[0]-30, pos[1]-15), (30, 12), 0.5, collision_type)
        self._connect(self.torso, self.l_arm, (-15, -20), (15, 0))

    def _add_box(self, pos, size, mass, col_type):
        body = pymunk.Body(mass, pymunk.moment_for_box(mass, size))
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.friction = 0.5
        shape.collision_type = col_type
        shape.color = self.color
        self.space.add(body, shape)
        return body

    def _add_circle(self, pos, radius, mass, col_type):
        body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.friction = 0.5
        shape.collision_type = col_type
        shape.color = self.color
        self.space.add(body, shape)
        return body

    def _connect(self, b1, b2, a1, a2):
        joint = pymunk.PivotJoint(b1, b2, b1.local_to_world(a1))
        joint.collide_bodies = False # Prevents self-collision glitches
        self.space.add(joint, pymunk.RotaryLimitJoint(b1, b2, -0.8, 0.8))

    def move(self, direction):
        self.torso.apply_impulse_at_local_point((direction * 500, 0))
    
    def jump(self):
        if abs(self.torso.velocity.y) < 10: # Ground check
            self.torso.apply_impulse_at_local_point((0, -800))

    def punch(self):
        arm = random.choice([self.r_arm, self.l_arm])
        force = 800 if self.is_player else -800
        arm.apply_impulse_at_local_point((force, -200))

def handle_collision(arbiter, space, data):
    # Damage based on the force of the impact
    impulse = arbiter.total_impulse.length
    if impulse > 500:
        target = data['player'] if arbiter.shapes[0].collision_type == COLLISION_PLAYER else data['ai']
        damage = int(impulse / 150)
        target.health -= damage
    return True

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("Arial", 24)
    clock = pygame.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    
    space = pymunk.Space()
    space.gravity = (0, 1000)
    
    floor = pymunk.Segment(space.static_body, (0, HEIGHT-50), (WIDTH, HEIGHT-50), 10)
    floor.friction, floor.collision_type = 1.0, 3
    space.add(floor)
    
    player = Ragdoll(space, (200, 400), (0, 0, 255), COLLISION_PLAYER, True)
    ai = Ragdoll(space, (600, 400), (255, 0, 0), COLLISION_AI, False)
    
    # Collision Handler
    h = space.add_collision_handler(COLLISION_PLAYER, COLLISION_AI)
    h.post_solve = handle_collision
    h.data = {'player': player, 'ai': ai}

    ai_intel = 1.0
    running = True
    
    while running:
        screen.fill((220, 220, 220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f: player.punch() # Combat Key
                if event.key in [pygame.K_w, pygame.K_UP]: player.jump()

        # Input Handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: player.move(-1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player.move(1)

        # AI Behavior (Smarter Scaling)
        dist_x = player.torso.position.x - ai.torso.position.x
        if abs(dist_x) > 70:
            ai.move( (1 if dist_x > 0 else -1) * (0.8 * ai_intel) )
        if abs(dist_x) < 100 and random.random() < (0.03 * ai_intel):
            ai.punch()
        
        # Difficulty scales every second
        ai_intel += 0.0005

        # Physics Step
        space.step(1/FPS)
        space.debug_draw(draw_options)

        # UI Overlay
        p_txt = font.render(f"PLAYER HP: {max(0, player.health)}", True, (0,0,255))
        a_txt = font.render(f"AI INTEL: {ai_intel:.2f} | AI HP: {max(0, ai.health)}", True, (255,0,0))
        screen.blit(p_txt, (20, 20))
        screen.blit(a_txt, (WIDTH - 350, 20))

        if player.health <= 0 or ai.health <= 0:
            msg = "YOU WIN!" if ai.health <= 0 else "YOU LOST..."
            screen.blit(font.render(msg, True, (0,0,0)), (WIDTH//2-50, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run_game()
