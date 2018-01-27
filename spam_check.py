from spam.surbl import SurblChecker

checker = SurblChecker()
print(checker.is_spam("https://www.swagbucks.com"))