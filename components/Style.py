import os


class Style:
    @staticmethod
    def header() :
        print("""
        +----------------------------------------------------------+
        +                                                          +
        +                 WELCOME TO OLFU PYBANK                   +
        +                                                          +
        +----------------------------------------------------------+ 
        """)

    @staticmethod
    def endProgram() :
        os.system('cls')
        print("""
        +----------------------------------------------------------+
        +             THANK YOU FOR USING OLFU PYBANK              +
        +             SEE YOU ON YOUR NEXT TRANSACTION             +
        +                        GOOD BYE                          +
        +----------------------------------------------------------+ 
        """)
        stopProgram = input("\n     Press any [enter] to exit...")
        if stopProgram :
            exit(0)

    @staticmethod
    def menu() :
        print("""
        +----------------------------------------------------------+
        +                   WELCOME TO OLFU PYBANK                 + 
        +----------------------------------------------------------+ 
        +                           MENU                           +
        +----------------------------------------------------------+ 
        +       [1] ACCOUNT DETAILS       [3] DEPOSIT              +
        +       [2] CHECK BALANCE         [4] WITHDRAW             +
        +                        [5] EXIT                          +
        +----------------------------------------------------------+ 
        """)

    @staticmethod
    def accountDetailsHeader() :
        print("""
        +----------------------------------------------------------+
        +                                                          +
        +                     ACCOUNT DETAILS                      +
        +                                                          +
        +----------------------------------------------------------+ 
        """)

    @staticmethod
    def checkBalanceHeader() :
        print("""
        +----------------------------------------------------------+
        +                                                          +
        +                      CHECK BALANCE                       +
        +                                                          +
        +----------------------------------------------------------+ 
        """)

    @staticmethod
    def depositHeader() :
        print("""
        +----------------------------------------------------------+
        +                                                          +
        +                          DEPOSIT                         +
        +                                                          +
        +----------------------------------------------------------+ 
        """)

    @staticmethod
    def withdrawHeader() :
        print("""
        +----------------------------------------------------------+
        +                                                          +
        +                         WITHDRAW                         +
        +                                                          +
        +----------------------------------------------------------+ 
        """)


