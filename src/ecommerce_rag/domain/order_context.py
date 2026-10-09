from dataclasses import dataclass

@dataclass
class OrderContext:
    order_id: str|None=None
    status: str|None=None
    carrier: str|None=None
    tracking_number: str|None=None
