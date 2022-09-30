# 8.13
def build_profile(first,  last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

axel_profile = build_profile('axel', 'zublena', location='anderson, SC', nationality='french', languages=["french", "english", "dutch"])
print(axel_profile)
