# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GardenMarket
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name):
        if not any(t['name'] == name for t in self.db.get('tags', [])):
            self.db.setdefault('tags', []).append({'id': len(self.db.get('tags', [])) + 1, 'name': name})
    
    def remove_tag(self, tag_name):
        tags = [t for t in self.db.get('tags', []) if t['name'] != tag_name]
        return len(tags) < len(self.db.get('tags', []))
    
    def assign_tags_to_item(self, item_id, tag_names):
        items = self.db.setdefault('items', [])
        tags = {t['name']: t for t in self.db.get('tags', [])}
        if not all(t in tags for t in tag_names): return False
        for item in items:
            if item['id'] == item_id and 'assigned_tags' not in item:
                item['assigned_tags'] = []
            if item['id'] == item_id:
                existing_ids = {t['name']: t['id'] for t in tags.values()}
                current_names = [item.get('assigned_tags', [])] + tag_names
                new_names = list(set(current_names))
                item['assigned_tags'] = [{'tag': n, 'id': existing_ids[n]} for n in new_names if n in existing_ids]
        return True
    
    def remove_tag_from_item(self, item_id, tag_name):
        items = self.db.setdefault('items', [])
        tags = {t['name']: t for t in self.db.get('tags', [])}
        if tag_name not in tags: return False
        for item in items:
            if item['id'] == item_id and 'assigned_tags' in item:
                item['assigned_tags'] = [t for t in item['assigned_tags'] if t['tag'] != tag_name]
                if not item['assigned_tags']:
                    del item['assigned_tags']
        return True
