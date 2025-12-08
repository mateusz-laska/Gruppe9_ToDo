from datetime import datetime

class Task:

    def __init__(self, id, title, desc, prio, cat, done=False, created=None):
        self.id = id
        self.title = title
        self.desc = desc
        self.prio = prio
        self.cat = cat
        self.done = done
        self.created = created or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.desc,
            "priority": self.prio,
            "category": self.cat,
            "done": self.done,
            "created": self.created
        }

    @staticmethod
    def from_dict(d):
        return Task(
            id=d["id"],
            title=d["title"],
            desc=d.get("description", ""),
            prio=d.get("priority", "medium"),
            cat = d.get("category"),
            done=d.get("done", False),
            created=d.get("created")
        )
