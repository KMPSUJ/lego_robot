from ev3.ev3dev import Motor


class m_over(Motor):
    def set_rel_position(self, position_sp=720, speed_sp=500, **kwargs):
        self.run_mode = 'position'
        self.position_mode = 'relative'
        self.regulation_mode = True
        for k in kwargs:
            v = kwargs[k]
            if (v is not None):
                setattr(self, k, v)
        self.pulses_per_second_sp = speed_sp
        self.position = 0
        self.position_sp = position_sp

    def add_rel_position(self, position_sp):
        self.position_sp += position_sp
