"""
Particle System
Filename: ParticleSystems.py
Author: Anh Tran
Date: March 15, 2024
Collaborator: Lisette Real Rico
Resources: https://stackoverflow.com/questions/3068619/draw-lines-over-a-circle 
"""
import dudraw 
import math
import random

class Vector:
    def __init__(self, some_x=0, some_y=0):
        """
        Project given code support calculating vector
        """
        self.x = some_x
        self.y = some_y

    def limit(self, l):
        if(self.length() >= l):
            self.resize(l)

    def resize(self, l):
        length = math.sqrt(self.x ** 2 + self.y**2)
        self.x *= (l/length)
        self.y *= (l/length)

    def __add__(self, other_vector):
        return Vector(self.x+other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        return Vector(self.x-other_vector.x, self.y - other_vector.y)

    def __isub__(self, other_vector):
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def divide(self, s):
        self.x /= s
        self.y /= s

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_in_radians(self):
        return math.tan((self.y/self.x))

class Time:
    """
    Class given in project assignment
    """
    frame = 0

    def tick():
        Time.frame += 1
    
    def time():
        return Time.frame


class Particle():
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        """
        Initializes instance variables for all Particle childrens objects
        parameter: (x, y, x velocity, y velocity, size = radius, lifetime).
        return: whether time of the partical has expired.
        """
        self.pos = Vector(x_pos, y_pos)
        self.vel= Vector(x_vel, y_vel)
        self.size = size
        self.color = dudraw.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.lifetime = lifetime

    def has_expired(self) -> bool:
        """
        Check whether a particle has expired depend on lifetime.
        Return: bool
        """
        expired = False
        #checks if the lifetime has reach 0
        if self.lifetime == 0:
            #sets expired to True if time reaches limit
            expired = True
        return expired

    def move(self):
        """
        Adds the velocity vector to position vector if the shape has not expired.
        Return: none
        """
        if self.lifetime > 0:
            #adds velocity to pos vector when particle not expired
            self.pos += self.vel


class SparkParticle(Particle):
    #initialize particle from parents
    """
    Function takes in parameters of parents function and set new color.
    Draw line follow position of x and y vector, and velocity vector which apply trig function.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        Particle.__init__(self,x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.color = dudraw.Color(255,128,13)
    
    def draw(self):
        #sets the color of the line and draws the line
        dudraw.set_pen_color(self.color)
        #check if particle has reach limit time
        if self.has_expired() == False:
            self.lifetime -=1
            dudraw.set_pen_color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            #draw line in direction of vel with sparkle assign color
            dudraw.line((self.pos.x), (self.pos.y), (self.pos.x+self.vel.x), (self.pos.y + self.vel.y))

class FireParticle (Particle):
    """
    Function take in same parameter as parents function.
    Parameter: (x, y, x velocity, y velocity, size = radius, lifetime).
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        Particle.__init__(self,x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.green_value = 255
        self.color = dudraw.Color(255,self.green_value,0)

    def draw(self):
        """
        Draw circles start with yellow, and changes color towards red by decreases green value.
        """
        dudraw.set_pen_color(self.color)
        if self.has_expired() == False:
            self.lifetime -= 1
            dudraw.filled_circle(self.pos.x, self.pos.y, self.size)

        #decreases the green value, and only continue when value greater or equal to 0.
        if self.green_value - 10 >= 0:
            self.green_value -= 5
        self.color = dudraw.Color(255,int(self.green_value),0)


    def move(self):
        #move like parents, but decrease in size forming little circle movement built fire.
        Particle.move(self)
        #decreases the size of the fire particle
        self.size -= 0.0005

   
class AcceleratingParticle(Particle):
    """
    Function take in similar parameter as parents, create new acceleration vector.
    Parameter: (x, y, x velocity, y velocity, size = radius, lifetime).
    return: increase velocity vector and increase position vector.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        Particle.__init__(self,x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.acc = Vector(x_acc, y_acc)

    def move(self):
        #moves the accelerating particle using the parent class's move function
        Particle.move(self)
        #adds the acceleration vector to velocity vector
        #this is instruction giving
        self.vel += self.acc
        self.pos += self.vel


class FireworkParticle(AcceleratingParticle):
    """
    Function draws squares and have parameter same as AcceleratingParticle parents.
    Parameter: (x, y, x velocity, y velocity, size = radius, lifetime) + self.acc (x_acc, y_acc) #vector accerleration.
    return: draw tiny square giving parameter.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        AcceleratingParticle.__init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime)

    def draw(self):
        # draw fire works particles with random color and filled square
        dudraw.set_pen_color(self.color)
        dudraw.filled_square(self.pos.x, self.pos.y, self.size)

class MarbleParticle(AcceleratingParticle):
    """
    Function takes is same parameter as parents class.
    Parameter: (x, y, x velocity, y velocity, size = radius, lifetime) + self.acc (x_acc, y_acc) #vector accerleration.
    return: draw circles one outline, one random color.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        AcceleratingParticle.__init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime)

    def draw(self):
        #draw marbles with random color as circle shape
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.pos.x, self.pos.y, self.size)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.pos.x, self.pos.y, self.size)
    def move(self):
        #continue update the position
        super().move()

"""
Particle container with different particles append.
"""
class ParticleContainer():
    """
    Function creates an empty list and allows Animate function to behave the particle append.
    Parameter: x_pos and y_pos
    Return: paticles in the list will be draw, and move
    """
    def __init__(self, x_pos, y_pos):
        self.pos = Vector(x_pos, y_pos)
        self.particles = [] #await for particle to be append.

    def animate(self):
        #checking all the particles, and remove expired one
        for particle in self.particles:
            particle.draw() #class instruction
            particle.move()

        
class Firework(ParticleContainer):
    def __init__(self, x_pos, y_pos):
        ParticleContainer.__init__(self, x_pos, y_pos)
        for particle in range(500):
            self.particles.append(FireworkParticle(x_pos, y_pos, random.uniform(-0.04, 0.04), random.uniform(-0.04, 0.04), 0, random.uniform(-0.008, -0.012), 0.004, 50))

    
class Marbles(ParticleContainer):
    """
    Function append MarblesPArticle which creates circles, and append the amount into parent function containers.
    Parent class pass down function animate, activate and add boundaries movement for the circle
    The marble balls bounce of each other, and not move surpassed canvas boundaries.
    Parameter: x_pos, y_pos, values x and y in appending is random base on canvas parameter.
    Return: create new particle container values, draw circles.
    """
    def __init__(self, x_pos, y_pos):
        #vector is an automation 
        ParticleContainer.__init__(self, x_pos, y_pos)
        
        for particle in range (10):
            self.particles.append(MarbleParticle(random.uniform(0.05, 1-0.05), random.uniform(0.05, 1-0.05),random.uniform(-0.04, 0.04), random.uniform(-0.04, 0.04), 0, random.uniform(-0.001, -0.002), 0.05, 500))


    def animate(self):
        #same as parents, but marble bounce off of each other
        ParticleContainer.animate(self)

        for marble1 in range(len(self.particles)):
            for marble2 in range(len(self.particles)):
                #check video start at 6:00min on Albow video
                #only check when marble are not the same
                if marble1 != marble2:
                    #using the position between comparison marbles to get marble vector
                    marble_vector = self.particles[marble1].pos - self.particles[marble2].pos
                    #vector class have length function to calculate the length of comprison marble
                    marble_distance = marble_vector.length()
                    #calculate sum distance where they are next to each other, radius = size * 2
                    sum_of_radius = self.particles[marble1].size + self.particles[marble2].size
                    #if marble one on top of another, or 0 distance from each other
                    if marble_distance <= sum_of_radius:
                        #Then move the marble away with velocity add by different in (x,y)
                        self.particles[marble1].vel += marble_vector
                        self.particles[marble1].vel.limit(0.02) #slow marble down
                        self.particles[marble2].vel -= marble_vector #move marble opposite direction
                        self.particles[marble2].vel.limit(0.02)
        
        #checking marble movement out of bound
        for i in range(len(self.particles)) :
            if self.particles[i].pos.x + self.particles[i].size >= 1: #right wall bound (x)
                self.particles[i].vel.x *= -1
            if self.particles[i].pos.x - self.particles[i].size <= 0: #left wall bound (x)
                self.particles[i].vel.x *= -1
            if self.particles[i].pos.y + self.particles[i].size >= 1: #up wall bound (y)
                self.particles[i].vel.y *= -1
            if self.particles[i].pos.y - self.particles[i].size <= 0: #lower wall bound (y)
                self.particles[i].vel.y *= -1
    

class Emitter(ParticleContainer):
    """
    Function is parents class for others particle, allows childrens particle access to the container.
    Parameter: x_pos, y_pos, fire_rate (amount to draw)
    Return: None
    """
    def __init__(self, x_pos, y_pos, fire_rate):
        ParticleContainer.__init__(self,x_pos, y_pos)
        self.fire_rate = fire_rate

class Fire(Emitter):
    """
    Function take in same parameter as parents, and add fire particle into the container.
    Parameter: x_pos, y_pos, fire_rate (amount of balls of fire)
    Return: new particle list with fire particle.
    """
    def __init__(self, x_pos, y_pos, fire_rate):
        Emitter.__init__(self, x_pos, y_pos, fire_rate)

    def animate(self):
        #add fire_rate as new FireParticles
        #pos = vector(x_pos, y_pos)
        #velocity: random(-0.002, 0.002)
        #size: random(0.01, 0.03)
        #life_time
        Emitter.animate(self)
        for rate in range(self.fire_rate):
            self.particles.append(FireParticle(self.pos.x, self.pos.y, random.uniform(-0.002, 0.002), random.uniform(0.002, 0.005), random.uniform(0.01, 0.03), 50))

class Sparkler (Emitter):
    #emitter keep adding particles to keep running
    """
    Function takes in same parameter as Emitter parents class(that childrens of Particle container).
    Draws line in a circle with animate function from parents class.
    Parameter: x_pos, y_pos, fire_rate (amount of line to creates fireworks strike)
    Return: particle containers contains sparkparticles.
    """
    def __init__(self, x_pos, y_pos, fire_rate):
        Emitter.__init__(self, x_pos, y_pos, fire_rate)

    def animate(self):
        #animate like parent, add fire_rate new Sparks to the list. 
        #have ability to change x and y position
        #vel: random(-0.07, 0.07)
        #life_time: 5
        dudraw.set_pen_color_rgb(88, 57, 39)
        dudraw.set_pen_width(0.0005)
        #draw spark stick, constant draw no movement
        dudraw.line(self.pos.x, self.pos.y, (self.pos.x), (self.pos.y-0.3))

        #activate parents animate function.
        Emitter.animate(self)
        for spark in range(self.fire_rate):
            #choose angle and turn value, though it isn't as effective
            angle = random.uniform(0, 2*math.pi)
            distance = random.uniform(0, 0.05)
            #turning the way line draw in a unit circle, rounded boundaries
            #TODO: review
            x_vel = distance * math.cos(angle)
            y_vel = distance * math.sin(angle)
            self.particles.append(SparkParticle(self.pos.x, self.pos.y, x_vel, y_vel, 0.05, 5))
            if self.particles[spark].has_expired():
                #if lifetime is up, particle expire remove particle from parent list.
                self.particles.pop(spark)

def main():
    dudraw.set_canvas_size(600,600)
    dudraw.clear(dudraw.LIGHT_GRAY)
    containers = []
    containers.append(Sparkler(0.75, 0.75, 200))
    containers.append(Fire(0.2, 0.1, 200))

    quit = True
    while quit:
        Time.tick() #activate time class with expire lifetime.
        dudraw.clear(dudraw.LIGHT_GRAY)
        # goes through each particle in containers which are starters.
        for container in containers:
            #animates the particles 
            container.animate()
            #add more particle containers with different function requirements
            if dudraw.has_next_key_typed():
                key = dudraw.next_key_typed()
                #if user type 'f' firework draw with square appear
                if key == 'f':
                    containers.append(Firework(dudraw.mouse_x(), dudraw.mouse_y()))
                if key == 'q':
                    quit = False
        #if mouse clicked on screen marbles in length of 10 use mouse(x,y) as parameter pass in
        if dudraw.mouse_clicked():
            containers.append(Marbles(dudraw.mouse_x(), dudraw.mouse_y()))

        dudraw.show(40)

if __name__ == '__main__':
    main()
