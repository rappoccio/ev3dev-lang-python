#!/usr/bin/env python3

import time, random
import ev3dev.ev3 as ev3

random.seed( time.time() )


class FireInRange:
    def __init__(self):
        # Connect the required equipement
        self.lm = ev3.LargeMotor('outB')
        self.rm = ev3.LargeMotor('outC')
        self.mm = ev3.MediumMotor()

        self.ir = ev3.InfraredSensor()
        self.ts = ev3.TouchSensor()
        self.cs = ev3.ColorSensor()

        # Check if everything is attached
        assert(self.lm.connected)
        assert(self.rm.connected)
        assert(self.mm.connected)

        assert(self.ir.connected)
        assert(self.ts.connected)
        assert(self.cs.connected)

        self.ir.mode = 'IR-PROX'

        # Reset the motors
        for m in (self.lm, self.rm, self.mm):
            m.reset()
            m.position = 0
            m.stop_action = 'brake'


    # Robot will check range to nearest object. If not in range, it will move forward.
    # When in range, it will speak. 
    def get_in_range(self):    
        distance = self.ir.value()

        while distance < 500 : 
            self.lm.run_forever(speed_sp=speed)
            self.rm.run_forever(speed_sp=speed)

        ev3.Sound.speak('I am now in range')
        return True
        

    def shoot(self, direction='up'):
        """
        Shot a ball in the specified direction (valid choices are 'up' and 'down')
        """
        distance = self.ir.value()
        if distance < 500 :
            self.mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
            while 'running' in self.mm.state:
                time.sleep(0.1)
        else :
            ev3.Sound.speak('I cannot attack that target.')


if __name__ == '__main__':
    terky = FireInRange()
    terky.shoot()
    terky.get_in_range()
    terky.shoot()
    
