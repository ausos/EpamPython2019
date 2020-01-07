class Building:
    def __init__(self, name, **kwargs):
        self.name = name
        self.storage = list()


class Warehouse(Building):
    def __init__(self, distance, **kwargs):
        super().__init__(**kwargs)
        self.distance = distance

    def delivery(self, containers):
        return len(self.storage) == containers

    def add_container(self, container):
        self.storage.append(container)
        return None


class Transport:
    def __init__(self, name):
        self.name = name
        self.container = None
        self.target = None
        self.start = True
        self.time = 0

    def movement(self, target, container):
        self.target = target
        self.container = container
        self.time = 2 * target.distance
        self.start = False

    def loc(self):
        if self.start:
            return None
        self.time -= 1
        if self.time == self.target.distance:
            self.target.add_container(self.container)
        if self.time == 0:
            self.start = True


class Factory(Building):
    def __init__(self, containers, transport, warehouses, **kwargs):
        super().__init__(**kwargs)
        self.storage = list(containers)

        self.transport = transport
        self.warehouses = warehouses

    def assign_delivery(self):
        for transport in self.transport:
            if transport.start:
                if self.storage:
                    conteiner = self.storage.pop(0)
                    transport.movement(self.warehouses[conteiner], conteiner)


class Port(Factory, Warehouse):
    pass

orders = ['A',
          'AB',
          'BB',
          'ABB',
          'AABABBAB',
          'ABBBABAAABBB']

if __name__ == '__main__':

    for order in orders:
        truck1 = Transport('Truck 1')
        truck2 = Transport('Truck 2')
        ship = Transport('Ship')
        whA = Warehouse(name='A', distance=4)
        whB = Warehouse(name='B', distance=5)
        port = Port(name='Port', transport=[ship], warehouses={'A': whA},
                    distance=1, containers=list())
        time = 1
        factory = Factory(name='Factory', transport=[truck1, truck2],
                          warehouses={'A': port, 'B': whB},
                          containers=order)
        while True:
            factory.assign_delivery()
            port.assign_delivery()
            truck1.loc()
            truck2.loc()
            ship.loc()
            if whA.delivery(order.count('A')) and whB.delivery(order.count('B')):
                break
            time += 1
        print(f'Delivery time for {i}: {time}')
