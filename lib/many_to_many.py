class Author:
   
    all_authors = []

    def __init__(self, name):
        
        self.name = name
        self.contracts_list = []
        
        self.add_to_all_authors()

    def contracts(self):
        
        return self.contracts_list

    def books(self):
        
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        
        if not isinstance(book, Book):
            
            raise Exception("Invalid book object")
        
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        
        total = sum(contract.royalties for contract in self.contracts_list)
        return total

    def add_to_all_authors(self):
        
        self.all_authors.append(self)




class Book:
     all_books = []

     def __init__(self, title):
         
        self.title = title
        self.add_to_all_books()

     def add_to_all_books(self):
         
        self.all_books.append(self)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        
        if not isinstance(author, Author):
            raise Exception("Invalid author object")
        
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        
        if not isinstance(date, str): 
            raise Exception("Date must be of type string")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        self.add_to_all_contracts()

  
    def contracts_by_date(cls, date):
        
        return [contract for contract in cls.all_contracts if contract.date == date]

    def add_to_all_contracts(self):
        
        self.all_contracts.append(self)