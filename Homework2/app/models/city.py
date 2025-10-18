"""City model definition.
Defines the City dataclass with attributes, string representation,
dictionary conversion methods, and a class method for instantiation
from a dictionary."""

# import dataclass decorator
from dataclasses import dataclass, field


@dataclass
class City:
    name: str
    region: str
    position: tuple[float, float] = field(default_factory=tuple)

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.region} "
            f"({self.position[0]}, {self.position[1]})"
        )

    def __repr__(self) -> str:
        return (
            f"City(name={self.name}, region={self.region}, "
            f"position={self.position}"
            )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "region": self.region,
            "position": {
                "latitude": self.position[0],
                "longitude": self.position[1]
            }
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'City':
        return cls(
            name=data["name"],
            region=data["region"],
            position=(
                data["position"]["latitude"],
                data["position"]["longitude"])
        )
