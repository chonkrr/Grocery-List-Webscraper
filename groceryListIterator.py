
import urlwebscraper

class GroceryListIterator:
    def __init__(self, groceryList):
        self.groceryList = groceryList
        self.current = 0    # Start at the beginning of the list

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.groceryList):
            self.current += 1
            return self.groceryList[self.current - 1]
        else:
            raise StopIteration
        
def main():
    # Get the list of products
    with open("grocerylist.txt", "r") as file:
        groceryList = file.readlines()
        for line in file:
            groceryList.append(line.strip())
    

    
    # Create the iterator
    groceryListIterator = GroceryListIterator(groceryList)
    
    # Iterate through the list
    for product in groceryListIterator:
        urlwebscraper.extract_urls(product)
        

if __name__ == "__main__":
    main()
