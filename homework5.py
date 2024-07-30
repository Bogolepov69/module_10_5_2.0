import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product = request[0]
        action = request[1]
        quantity = request[2]

        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity

    def run(self, requests):
        for request in requests:
            self.process_request(request)


if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(manager.data)