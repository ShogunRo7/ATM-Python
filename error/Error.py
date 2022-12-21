# List of errors in the program
class Error :
    @staticmethod
    def dataTypeChecker() :
        print ("\n         Prompt: This ATM only accepts numbers")

    @staticmethod
    def invalidNumberOfPin():
        print("\n          Prompt: Number of pin should be six numbers. Please try again.")

    @staticmethod
    def cardNotFound():
        print("\n         Prompt: Card not found. Please try again.")

    @staticmethod
    def optionVerifier() :
        print("\n         Prompt: Enter [1, 2, 3, 4, or 5] only! Please try again.")

    @staticmethod
    def yesNoVerifier() :
        print("\n         Prompt: Enter '1' for yes and '2' for NO.")

    @staticmethod
    def cardIdAndPinNotMatch() :
        print("\n         Prompt: Card Id and Pin is not match. Please try again.")

    @staticmethod
    def notEnoughBalance() :
        print("\n         Prompt: Not enough balance. Please try again.")

    @staticmethod
    def negativeNumberNotAllowed() :
        print("\n         Prompt: Negative number is not allowed. Please try again.")