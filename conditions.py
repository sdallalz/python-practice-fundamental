# Conditions and boolean logic examples

def has_passed(age, has_certificate):
    return age > 18 and has_certificate


def has_passed_advanced(age, has_certificate, passed_exam, errors=0):
    if age < 18:
        return False
    if not has_certificate:
        return False
    if not passed_exam:
        return False
    if errors >= 2:
        return False
    return True


def can_drive(age, has_license, had_accident=False):
    if age < 18:
        return False
    if not has_license:
        return False
    if had_accident:
        return False
    return True


def is_eligible_for_discount(age, is_student, has_coupon=False):
    if age > 60 or is_student or has_coupon:
        return True
    return False


def can_register_course(passed_prerequisite, has_debt, gpa):
    if not passed_prerequisite:
        return False
    if has_debt:
        return False
    if gpa < 2.0:
        return False
    return True


def can_travel(has_passport, has_criminal_record, visa_valid=True):
    if not has_passport:
        return False
    if not visa_valid:
        return False
    if has_criminal_record:
        return False
    return True


def is_healthy(temperature, cough, covid_test_positive=False):
    if temperature > 38:
        return False
    if cough:
        return False
    if covid_test_positive:
        return False
    return True


# Test examples
print("Has passed:", has_passed(20, True))
print("Advanced passed:", has_passed_advanced(22, True, True, 1))
print("Can drive:", can_drive(19, True))
print("Discount eligible:", is_eligible_for_discount(25, True))
print("Can register course:", can_register_course(True, False, 3.1))
print("Can travel:", can_travel(True, False))
print("Is healthy:", is_healthy(36.8, False))
