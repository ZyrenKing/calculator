import sys  # استيراد وحدة sys للتحكم في الخروج من البرنامج
from utils.history import display_history, clear_history, load_history, save_history, add_to_history  # استيراد دوال إدارة السجل
from utils.calculation import validate_expression, evaluate_expression  # استيراد دوال التحقق والتقييم

def run():
    """الحلقة الرئيسية لواجهة سطر الأوامر."""
    while True:  # حلقة لا نهائية لعرض القائمة باستمرار حتى يختار المستخدم الخروج
        print("\n--- آلة حاسبة ---")  # طباعة عنوان القائمة
        print("1. عملية حسابية")  # خيار إجراء عملية
        print("2. عرض السجل")  # خيار عرض العمليات السابقة
        print("3. حذف السجل")  # خيار مسح السجل
        print("4. اغلاق التطبيق")  # خيار الخروج
        choice = input("اختر خيارًا: ").strip()  # قراءة اختيار المستخدم وإزالة المسافات الزائدة

        if choice == '1':  # إذا اختار إجراء عملية
            expr = input("أدخل العملية الرياضية: ")  # طلب إدخال التعبير
            if not validate_expression(expr):  # التحقق من صحة التعبير
                print("تعبير غير صحيح، يرجى المحاولة مرة أخرى.")  # رسالة خطأ
                continue  # العودة إلى بداية الحلقة دون متابعة
            try:
                result = evaluate_expression(expr)  # تقييم التعبير للحصول على النتيجة
                print(f"الناتج: {result}")  # عرض النتيجة للمستخدم
                add_to_history(expr, result)  # حفظ العملية والنتيجة في سجل العمليات
            except Exception as e:  # في حال أي خطأ غير متوقع أثناء التقييم
                print(f"حدث خطأ: {e}")  # عرض رسالة الخطأ

        elif choice == '2':  # إذا اختار عرض السجل
            display_history()  # استدعاء دالة عرض السجل

        elif choice == '3':  # إذا اختار حذف السجل
            confirm = input("هل أنت متأكد من حذف السجل؟ (y/n): ").strip().lower()  # طلب تأكيد المستخدم
            if confirm == 'y':  # إذا أكد بالضغط على y
                clear_history()  # استدعاء دالة مسح السجل
                print("تم حذف السجل.")  # إعلام المستخدم بالنجاح

        elif choice == '4':  # إذا اختار الخروج
            print("تم اغلاق التطبيق.")  # رسالة وداع
            sys.exit(0)  # إنهاء البرنامج برمز خروج 0 (طبيعي)

        else:  # إذا أدخل خيارًا غير موجود في القائمة
            print("خيار غير صحيح، يرجى المحاولة مرة أخرى.")  # تنبيه المستخدم
