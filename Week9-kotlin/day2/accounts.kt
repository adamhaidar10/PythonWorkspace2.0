enum class AccountType{
    CURRENT,
    SAVINGS
    }
class Account (var name: String, var acc_type: AccountType)
{
    private var balance: Double
    var acc_num : Int = (100000..200000).random()

    init{
        this.balance = 0.00
        println("Account is created")
        displayBalance()
    }
    fun deposit(n: Double){
        if (n>0)this.balance+=n else println("Cannot perform negative deposit")
        displayBalance()
    }
    fun withdraw(n: Double){
        if ((n>0)&& (n<this.balance)) this.balance-=n else println("Insufficient funds")
        displayBalance()
    }
    fun displayBalance(){
        println("Current balance: $${this.balance}")
    }
}
fun main()
{
    
    var alice = Account("Alice Jefferson", AccountType.SAVINGS)
    alice.deposit(353535.55)
    alice.withdraw(250.0)
    alice.displayBalance()
    alice.deposit(-200.00)
    alice.withdraw(100000000000.0)
    
    
}