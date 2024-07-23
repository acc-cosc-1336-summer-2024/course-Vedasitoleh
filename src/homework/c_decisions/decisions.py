#average rating function
def get_options_ratio(options, total):
    rating_num = options/total
    return rating_num

# rating
def get_faculty_rating(get_options_ratio):
    if (get_options_ratio >= 0.9 and get_options_ratio < 1):
        rating_eval = "Excellent"
    elif (get_options_ratio >= 0.8 and get_options_ratio < 0.9):
        rating_eval = "Very Good"
    elif (get_options_ratio >= 0.7 and get_options_ratio < 0.8):
        rating_eval = "Good"
    elif (get_options_ratio >= 0.6 and get_options_ratio < 0.7):
        rating_eval = "Needs Improvement"
    elif (get_options_ratio >= 0 and get_options_ratio <= 0.59):
        rating_eval = "Unacceptable"
    return rating_eval