from sympy import sympify, SympifyError

def validate_expression(expr):
    """التحقق من صحة التعبير الرياضي."""
    if not expr or expr.strip() == "":
        return False
    try:
        sympify(expr)
        return True
    except SympifyError:
        return False

def evaluate_expression(expr):
    """تقييم التعبير وإرجاع النتيجة."""
    try:
        result = sympify(expr)
        # إذا كان الناتج عدداً، نحوله إلى float أو int حسب الحاجة
        if result.is_number:
            return float(result) if result.is_real else result
        return result
    except SympifyError as e:
        raise ValueError(f"خطأ في التعبير: {e}")