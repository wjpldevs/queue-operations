from dataclasses import dataclass

@dataclass
class Client:

    name: str
    total: float

    def __init__(self, name="", total=0.0) -> None:
        self.name = name
        self.total = total

    # missing properties

clients = [Client()]

for client in clients:

    display_client = f"""
    =======================
    {client.name}
    {client.total}
    =======================
    """
    print(display_client)
