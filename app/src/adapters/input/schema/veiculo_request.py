from dataclasses import dataclass, field
from typing import List


@dataclass
class VeiculoRequest:
    marca: str = field(default=None)
    modelo: str = field(default=None)
    ano: int = field(default=None)
    cor: str = field(default=None)
    preco: float = field(default=0.00)
