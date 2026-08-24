import json  # استيراد وحدة json للتعامل مع ملفات JSON
import os  # استيراد وحدة os للتحقق من وجود الملفات

HISTORY_FILE = "history.json"  # تحديد اسم ملف السجل الثابت

def load_history():
    """تحميل السجل من ملف JSON، وإنشاء ملف فارغ إذا لم يكن موجوداً."""
    if os.path.exists(HISTORY_FILE):  # التحقق مما إذا كان ملف السجل موجودًا بالفعل
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:  # فتح الملف للقراءة مع ترميز utf-8
            try:
                return json.load(f)  # محاولة تحميل المحتوى كقائمة (أو قاموس) من JSON
            except json.JSONDecodeError:  # إذا كان الملف تالفًا أو فارغًا ولا يمكن تحليله
                return []  # إرجاع قائمة فارغة
    return []  # إذا لم يكن الملف موجودًا، إرجاع قائمة فارغة

def save_history(history):
    """حفظ قائمة السجل في ملف JSON."""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:  # فتح الملف للكتابة (سيتم استبدال المحتوى القديم)
        json.dump(history, f, indent=2, ensure_ascii=False)  # كتابة القائمة إلى الملف بتنسيق JSON جميل (مسافة بادئة 2) ودعم اللغة العربية

def add_to_history(operation, result):
    """إضافة عملية جديدة إلى السجل."""
    history = load_history()  # تحميل السجل الحالي
    history.append({"operation": operation, "result": str(result)})  # إضافة عملية جديدة كقاموس يحتوي على العملية والنتيجة (محولة لنص)
    save_history(history)  # حفظ القائمة المحدثة في الملف

def display_history():
    """عرض السجل بالصيغة المطلوبة."""
    history = load_history()  # تحميل السجل
    if not history:  # إذا كانت القائمة فارغة
        print("لا يوجد سجل.")  # إعلام المستخدم
        return  # الخروج من الدالة
    for entry in history:  # التكرار على كل عملية مسجلة
        print("============")  # فاصل أعلى
        print(f"operation: {entry.get('operation', '')}")  # طباعة العملية (مع قيمة افتراضية فارغة إذا كان المفتاح غير موجود)
        print(f"result: {entry.get('result', '')}")  # طباعة النتيجة

def clear_history():
    """حذف السجل بالكامل (تفريغ الملف)."""
    save_history([])  # حفظ قائمة فارغة مكان السجل القديم
