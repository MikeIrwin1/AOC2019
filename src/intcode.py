class Intcode:
    def __init__(self, program, input):
        self.ptr = 0
        self.input = input
        self.program = program
        self.output = 0
    
    def get_param(self, mode, rel):
        if mode == 0:
            return self.program[self.ptr + rel]
        elif mode == 1:
            return self.ptr + rel

    def compute(self):
        while True:
            instruction = int("%05d" % self.program[self.ptr])
            op = instruction % 100
            mode1 = instruction // 100 % 10
            mode2 = instruction // 1000 % 10
            mode3 = instruction // 10000 % 10
            if op == 1:
                self.program[self.get_param(mode3, 3)] = self.program[self.get_param(mode2, 2)] + self.program[self.get_param(mode1, 1)]
                self.ptr += 4
            elif op == 2:
                self.program[self.get_param(mode3, 3)] = self.program[self.get_param(mode2, 2)] * self.program[self.get_param(mode1, 1)]
                self.ptr += 4
            elif op == 3:
                self.program[self.get_param(mode1, 1)] = self.input
                self.ptr += 2
            elif op == 4:
                self.output = self.program[self.get_param(mode1, 1)]
                self.ptr += 2
            elif op == 5:
                if self.program[self.get_param(mode1, 1)] != 0:
                    self.ptr = self.program[self.get_param(mode2, 2)]
                else: 
                    self.ptr += 3
            elif op == 6:
                if self.program[self.get_param(mode1, 1)] == 0:
                    self.ptr = self.program[self.get_param(mode2, 2)]
                else:
                    self.ptr +=3
            elif op == 7:
                if self.program[self.get_param(mode1, 1)] < self.program[self.get_param(mode2, 2)]:
                    self.program[self.get_param(mode3, 3)] = 1
                    self.ptr += 4
                else:
                    self.program[self.get_param(mode3, 3)] = 0
                    self.ptr += 4
            elif op == 8:
                if self.program[self.get_param(mode1, 1)] == self.program[self.get_param(mode2, 2)]:
                    self.program[self.get_param(mode3, 3)] = 1
                    self.ptr += 4
                else:
                    self.program[self.get_param(mode3, 3)] = 0
                    self.ptr += 4
            elif op == 99:
                break
    
    def get_output(self):
        print(self.output)