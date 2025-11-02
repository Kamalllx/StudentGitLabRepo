"""
Personal Finance Tracker
A simple application to manage personal finances
"""

def main():
    print("=" * 50)
    print("   Welcome to Personal Finance Tracker")
    print("=" * 50)
    
    balance = 0.0
    transactions = []
    
    print(f"\nCurrent Balance: ${balance:.2f}")
    print("\nFeatures coming soon:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")
    
    # New functionality added
    print("\n💡 Tip: Track your expenses daily for better financial health!")

if __name__ == "__main__":
    main()
