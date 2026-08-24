import json
import os

HISTORY_FILE = "history.json"

def load_history():
    """تحميل السجل من ملف JSON، وإنشاء ملف فارغ إذا لم يكن موجوداً."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_history(history):
    """حفظ قائمة السجل في ملف JSON."""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def display_history():
    """عرض السجل بالصيغة المطلوبة."""
    history = load_history()
    if not history:
        print("لا يوجد سجل.")
        return
    for entry in history:
        print("============")
        print(f"operation: {entry.get('operation', '')}")
        print(f"result: {entry.get('result', '')}")
        print("============")

def clear_history():
    """حذف السجل بالكامل (تفريغ الملف)."""
    save_history([])