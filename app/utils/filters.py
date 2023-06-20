# Formats a date object as MM/DD/YY
def format_date(date):
    return date.strftime('%m/%d/%y')

# Only includes domain name using replace and split 
def format_url(url): 
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word): 
    if amount != 1: 
        return word + 's'
    
    return word 