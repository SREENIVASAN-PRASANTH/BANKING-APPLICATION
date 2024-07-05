class Admin:
    username = "Admin"
    password = "1234"
    customer_details = {}

    def login(self):
        user_name = input("Enter the Admin's Username: ")
        pass_word = input("Enter the Password: ")

        if user_name == self.username and self.password == pass_word:
            print("\nYou have succesfully logged in.")
            while(True):
                operation = int(input('''
1.Add User
2.Delete User
3.Modify User
4.View Customer details
5.Exit

Enter your option:'''))
                if operation == 1:
                    self.add_user()
                elif operation == 2:
                    self.delete_user()
                elif operation == 3:
                    self.modify_user()
                elif operation == 4:
                    self.view_customer_details()
                elif operation == 5:
                    print("Logging out")
                    break
        else:
            print("\nIncorrect username or password\n")
            self.login()

    def add_user(self):
        full_name = input("\nEnter Customer name: ")
        address = input("Enter Customer address: ")
        balance = 1000
        account_number = input("Create a account number:")
        if account_number in self.customer_details.keys():
            print("\nAccount number already exist!!!\n")
            self.add_user()
        else:
            self.customer_details[account_number] = {"full_name":full_name,"address":address,"balance":balance}
            print("\n----------User Created Succesfully---------\n")

    def view_customer_details(self):

        customer_accnt_no = input("\nEnter customer account number: ")
        if customer_accnt_no in self.customer_details.keys():
            print(f"""
customer name : {self.customer_details[customer_accnt_no]["full_name"]}
Customer address : {self.customer_details[customer_accnt_no]["address"]}
Balance : {self.customer_details[customer_accnt_no]["balance"]}
            """)
        else:
            print("\nInvalid customer id!!!!\n")
            self.view_customer_details()

    def modify_user(self):
        customer_accnt_no = input("\nEnter customer account number: ")
        if customer_accnt_no in self.customer_details.keys():
            field_toUpdate = input("Enter the field to update(full_name -1 /address - 2 /For both - 3): ")
            if field_toUpdate == "1":
                new_name = input("Enter new name: ")
                self.customer_details[customer_accnt_no]["full_name"] = new_name
                print("\nSuccessfully updated name\n")

            elif field_toUpdate == "2":
                new_address = input("Enter new address: ")
                self.customer_details[customer_accnt_no]["address"] = new_address
                print("\nSuccessfully updated address\n")

            elif field_toUpdate == "3":
                new_name = input("Enter new name: ")
                new_address = input("Enter new address: ")
                self.customer_details[customer_accnt_no]["full_name"] = new_name
                self.customer_details[customer_accnt_no]["address"] = new_address
                print("\nSuccessfully updates both name and address\n")

            else:
                print("\nInvalid Field")
                self.modify_user()
        else:
            print("\nInavlid account number")
            self.modify_user()

    def delete_user(self):
        customer_accnt_no = input("\nEnter customer accnt number: ")
        if customer_accnt_no in self.customer_details.keys():
            del self.customer_details[customer_accnt_no]
            print("\nCustomer was removed!!")
        else:
            print("\nInvalid account number")
            self.delete_user()

admin = Admin()
admin.login()




