from sympy import sympify, SympifyError  # استيراد دوال تحويل وتقييم التعبيرات الرياضية من مكتبة sympy

def validate_expression(expr):
    """التحقق من صحة التعبير الرياضي."""
    if not expr or expr.strip() == "":  # إذا كان التعبير فارغًا أو يتكون من مسافات فقط
        return False  # يُعتبر غير صحيح
    try:
        sympify(expr)  # محاولة تحويل النص إلى تعبير رياضي (سيُطرح خطأ إن كان غير صحيح)
        return True  # إذا نجحت المحاولة فالتعبير صحيح
    except SympifyError:  # في حال حدوث خطأ أثناء التحويل
        return False  # التعبير غير صحيح

def evaluate_expression(expr):
    """تقييم التعبير وإرجاع النتيجة."""
    try:
        result = sympify(expr)  # تحويل النص إلى كائن رياضي (رقم أو تعبير)
        # إذا كان الناتج عدداً، نحوله إلى float أو int حسب الحاجة
        if result.is_number:  # التحقق مما إذا كانت النتيجة عددًا (وليست تعبيرًا رمزيًا)
            return float(result) if result.is_real else result  # إرجاع float إذا كان حقيقيًا، وإلا نعيده كما هو
        return result  # إرجاع النتيجة كما هي (قد تكون تعبيرًا رمزيًا مثل sqrt(2))
    except SympifyError as e:  # في حال حدوث خطأ في التحويل أو التقييم
        raise ValueError(f"خطأ في التعبير: {e}")  # رفع استثناء مخصص مع رسالة الخطأ
