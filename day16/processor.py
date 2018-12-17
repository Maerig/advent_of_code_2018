class Processor:
    def __init__(self, registers=None):
        if registers is not None:
            self.registers = registers
        else:
            self.registers = [0, 0, 0, 0]
        self.configuration = {
            i: self._configuration_not_loaded
            for i in range(len(self.commands_by_name.keys()))
        }

    @property
    def commands_by_name(self):
        return {
            "addr": self.addr,
            "addi": self.addi,
            "mulr": self.mulr,
            "muli": self.muli,
            "banr": self.banr,
            "bani": self.bani,
            "borr": self.borr,
            "bori": self.bori,
            "setr": self.setr,
            "seti": self.seti,
            "gtir": self.gtir,
            "gtri": self.gtri,
            "gtrr": self.gtrr,
            "eqir": self.eqir,
            "eqri": self.eqri,
            "eqrr": self.eqrr
        }

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        self.registers[c] = 1 if a > self.registers[b] else 0

    def gtri(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] > b else 0

    def gtrr(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0

    def eqir(self, a, b, c):
        self.registers[c] = 1 if a == self.registers[b] else 0

    def eqri(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] == b else 0

    def eqrr(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0

    def load_configuration(self, path):
        with open(path, "r") as configuration_file:
            for entry in configuration_file.readlines():
                opcode, command_name = entry.strip().split("=")
                self.configuration[int(opcode)] = self.commands_by_name[command_name]

    def run_command(self, opcode, a, b, c):
        self.configuration[opcode](a, b, c)

    @staticmethod
    def _configuration_not_loaded(*args, **kwargs):
        raise RuntimeError("Configuration not loaded")
