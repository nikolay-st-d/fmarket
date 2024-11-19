def user_profile_completed(self) -> bool:
    user = self.object
    if (user.first_name == ''
            or user.last_name == ''
            or user.phone_number == ''):
        return False
    return True
