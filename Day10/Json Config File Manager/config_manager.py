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