JSON Config File Manager
json load dump pathlib
Real-world App
VS Code / Django settings
Overview
ConfigManager reads/writes a JSON file using json.load / json.dump with indent=2. Auto-creates 
config.json with DEFAULTS if missing. set() immediately persists to disk. delete() returns True if the 
key existed. reset() replaces the file entirely with DEFAULTS. This is how VS Code, Chrome, and 
Django manage their settings files.
Problem
Config manager with get/set/delete/reset. Auto-creates config.json with defaults if file does not 
exist.
Starter Code
import json
from pathlib import Path
DEFAULTS={"theme":"light","language":"en","font_size":14,"auto_save":True}
class ConfigManager:
    def __init__(self, path="config.json"):
        self.path=Path(path); self.config=self._load()
    def _load(self):
        if not self.path.exists():
            self._save(DEFAULTS); return DEFAULTS.copy()
        with open(self.path) as f: return json.load(f)
    def _save(self, data):
        with open(self.path,"w") as f: json.dump(data,f,indent=2)
    def get(self,key,default=None): ...
    def set(self,key,value): ...
    def delete(self,key)->bool: ...
    def reset(self): ...
Constraints
•  set() calls _save() immediately
•  delete() returns True if key existed
•  reset() restores to DEFAULTS
•  json.dump with indent=2