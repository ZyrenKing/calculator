import sys
from utils.history import display_history, clear_history, load_history, save_history
from utils.calculation import validate_expression, evaluate_expression

def add_to_history(operation, result):
    """إضافة عملية جديدة إلى السجل."""
    history = load_history()
    history.append({"operation": operation, "result": str(result)})
    save_history(history)

def run():
    """الحلقة الرئيسية لواجهة سطر الأوامر."""
    while True:
        print("\n--- آلة حاسبة ---")
        print("1. عملية حسابية")
        print("2. عرض السجل")
        print("3. حذف السجل")
        print("4. اغلاق التطبيق")
        choice = input("اختر خيارًا: ").strip()

        if choice == '1':
            expr = input("أدخل العملية الرياضية: ")
            if not validate_expression(expr):
                print("تعبير غير صحيح، يرجى المحاولة مرة أخرى.")
                continue
            try:
                result = evaluate_expression(expr)
                print(f"الناتج: {result}")
                add_to_history(expr, result)
            except Exception as e:
                print(f"حدث خطأ: {e}")

        elif choice == '2':
            display_history()

        elif choice == '3':
            confirm = input("هل أنت متأكد من حذف السجل؟ (y/n): ").strip().lower()
            if confirm == 'y':
                clear_history()
                print("تم حذف السجل.")

        elif choice == '4':
            print("تم اغلاق التطبيق.")
            sys.exit(0)

        else:
            print("خيار غير صحيح، يرجى المحاولة مرة أخرى.")