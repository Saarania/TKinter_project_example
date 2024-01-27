from transport_ability import TransportAbility

class Animal:
    def __init__(self, name, age, transport):
        self.name = name
        self.age = age
        self.transport = transport
    def __str__(self):
        str_transport = ""
        try:
            c_list = iter(self.transport)
            if TransportAbility.FLYING in self.transport:
                str_transport += "Fly, "
            if TransportAbility.WALKING in self.transport:
                str_transport += "Walk, "
            if TransportAbility.SWIMMING in self.transport:
                str_transport += "Swim, "

        except TypeError as te:
            if TransportAbility.FLYING == self.transport:
                str_transport += "Fly, "
            if TransportAbility.WALKING == self.transport:
                str_transport += "Walk, "
            if TransportAbility.SWIMMING == self.transport:
                str_transport += "Swim, "
        return f"animal = {self.name}, age = {self.age} transport = {str_transport}"