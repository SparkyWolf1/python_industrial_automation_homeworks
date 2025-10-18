from dataclasses import dataclass


@dataclass
class CurrentWeather:
    name: str
    longtitude: float
    latitude: float
    temperature: float
    humidity: float
    wind_speed: float
    description: str

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "longtitude": self.longtitude,
            "latitude": self.latitude,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CurrentWeather':
        return cls(
            temperature=data["temperature"],
            humidity=data["humidity"],
            wind_speed=data["wind_speed"],
            description=data["description"]
        )
