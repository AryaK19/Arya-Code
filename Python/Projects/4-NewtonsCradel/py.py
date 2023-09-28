import pymunk
import pymunk.pygame_util
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True

    # create a space
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    # create a ball body and a circle shape
    ball_mass = 1
    ball_radius = 30
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = (300, 300)
    ball_shape = pymunk.Circle(ball_body, ball_radius)

    # create a spring joint
    damping = 0.1
    stiffness = 100.0
    rest_length = 200.0
    spring = pymunk.DampedSpring(space.static_body, ball_body, (300, 500), (0,0), rest_length, stiffness, damping)

    # add the ball and the spring to the space
    space.add(ball_body, ball_shape, spring)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((255,255,255))

        # step the simulation
        dt = 1.0/60.0
        space.step(dt)

        # draw the ball
        ball_position = ball_body.position
        ball_x = int(ball_position.x)
        ball_y = int(ball_position.y)
        pygame.draw.circle(screen, (0,0,255), (ball_x, ball_y), ball_radius)

        # update the display
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
