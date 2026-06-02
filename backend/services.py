import datetime
from dataclasses import dataclass, field
from typing import List

import requests

@dataclass
class Note:
    title: str
    content: str
    id: int = field(default_factory=lambda: Note.next_id())

    @staticmethod
    def next_id() -> int:
        if not hasattr(Note, "_global_id"):
            Note._global_id = 1
        else:
            Note._global_id += 1
        return Note._global_id

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
        }

@dataclass
class Board:
    name: str
    notes: List[Note] = field(default_factory=list)

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def remove_note_by_id(self, note_id: int) -> bool:
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                return True
        return False

    def to_dict(self) -> dict:
        return {
            "title": self.name,
            "notes": [note.to_dict() for note in self.notes],
        }


class DashboardManager:
    """Clase encargada de la lógica interna del sistema (Tiempo y Saludos)."""

    def __init__(self, username: str = "Desarrollador"):
        self.username = username

    def get_current_time_data(self):
        now = datetime.datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            greeting = f"¡Buen día, {self.username}! A darle átomos al código."
        elif 12 <= hour < 18:
            greeting = f"¡Buenas tardes, {self.username}! Mantén el ritmo."
        else:
            greeting = f"¡Buenas noches, {self.username}! No olvides descansar la vista."

        return {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%A, %d de %B"),
            "greeting": greeting,
        }


class AdviceService:
    """Clase encargada exclusivamente de la comunicación con la API externa."""

    def __init__(self):
        self.api_url = "https://api.adviceslip.com/advice"

    def fetch_random_advice(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "id": data["slip"]["id"],
                    "advice": data["slip"]["advice"],
                }
            return {"advice": "Confía en tu proceso, el código compilará.", "id": 0}
        except Exception:
            return {
                "advice": "Sigue adelante, las conexiones fallan pero tu lógica no.",
                "id": 0,
            }
