from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

class QuizForm(forms.Form):

    CHOICES_Q1 = [
        (False, "A type of farmers market where people buy and sell food"),
        (True, "A place where parts of businesses are bought and sold"),
        (False, "A special type of grocery store that sells stocks"),
        (False, "A type of bank that gives out loans to new businesses"),
    ]
    CHOICES_Q2 = [
        (False, "Part"),
        (False, "Marker"),
        (False, "Stocker"),
        (True, "Share"),
    ]
    CHOICES_Q3 = [
        (False, "A share of ownership in a company"),
        (True, "Lending money to a company for a fixed interest payment"),
        (False, "A building on wall street"),
        (False, "An investment that cannot be traded"),
    ]
    CHOICES_Q4 = [
        (False, "Itemized Public Organization"),
        (False, "Initial Primary Offering"),
        (True, "Initial Public Offering"),
        (False, "Imminent Profitable Option"),
    ]
    CHOICES_Q5 = [
        (True, "Private company"),
        (False, "Public company"),
        (False, "Industry"),
        (False, "Portfolio"),
    ]
    CHOICES_Q6 = [
        (False, "Index"),
        (False, "Investment"),
        (False, "Profit"),
        (True, "Dividend"),
    ]
    CHOICES_Q7 = [
        (False, "When one or two stocks drop significantly"),
        (False, "Slow decrease in stock prices over a year"),
        (False, "Rapid but anticipated drop in stock prices."),
        (True, "rapid and unanticipated drop in stock prices"),
    ]
    CHOICES_Q8 = [
        (True, "NASDAQ & NYSE"),
        (False, "Dow Jones Industrial Average & S&P 500"),
        (False, "NYSE & American"),
        (False, "NASDAQ & DJIA"),
    ]
    CHOICES_Q9 = [
        (True, "Yes"),
        (False, "No"),
    ]
    CHOICES_Q10 = [
        (False, "DOW JONES"),
        (False, "S & P 500"),
        (False, "NASDAQ COMPOSITE"),
        (True, "P/E RATIO"),
    ]

    q1 = forms.ChoiceField(label = "What is the stock market?", choices = CHOICES_Q1, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q2 = forms.ChoiceField(label = "The name for a part of a business that is bought and sold on the stock market is", choices = CHOICES_Q2, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q3 = forms.ChoiceField(label = "What is a bond?", choices = CHOICES_Q3, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q4 = forms.ChoiceField(label = "IPO stands for", choices = CHOICES_Q4, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q5 = forms.ChoiceField(label = "A company owned by families or a small number of investors and do not issue stock to the public is called", choices = CHOICES_Q5, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q6 = forms.ChoiceField(label = "A sum of money paid to shareholders of a corporation out of its earnings", choices = CHOICES_Q6, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q7 = forms.ChoiceField(label = "What is a stock market crash?", choices = CHOICES_Q7, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q8 = forms.ChoiceField(label = "The two major stock exchanges are", choices = CHOICES_Q8, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q9 = forms.ChoiceField(label = "Can interest rates affect the stock market?", choices = CHOICES_Q9, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })
    q10 = forms.ChoiceField(label = "Which of the following is NOT a stock index?", choices = CHOICES_Q10, widget=forms.RadioSelect, error_messages = {
                 'required':"Please choose an option"
                 })