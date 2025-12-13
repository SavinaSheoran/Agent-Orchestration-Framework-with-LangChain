# memory.py
import json
import os

class Memory:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.data = self.load_memory()

    # Load memory from JSON file

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            return {}

        try:
            with open(self.memory_file, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    # Save memory to JSON file

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.data, f, indent=4)

    # Add new memory under a specific key
    # Example: memory.add("user_name", "Savina")
    
    def add(self, key, value):
        self.data[key] = value
        self.save_memory()

    # Retrieve memory value
    # Example: memory.get("user_name")

    def get(self, key, default=None):
        return self.data.get(key, default)

    # Delete a memory key
    # Example: memory.delete("user_name")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_memory()

    
    # Clear all memory entirely

    def clear(self):
        self.data = {}
        self.save_memory()
