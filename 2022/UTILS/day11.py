class monkey:
    def __init__(self, number, items, operation, test_val, test_true, test_false, show_print):
        self.number = number
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.test_true = test_true
        self.test_false = test_false
        self.show_print = show_print
        self.n_inspections = 0
    
    def inspect(self):
        old = self.items[0]
        if self.show_print:
            print('Monkey ' + str(self.number) + ' inspects item wl ' + str(old))
        new = eval(self.operation)
        if self.show_print:
            print(' Wl ' + self.operation + ' to ' + str(new))
        self.items[0] = new
        self.n_inspections += 1

    def test(self):
        if (self.items[0] % self.test_val) == 0:
            if self.show_print:
                print('     Current worry level is divisible by' + str(self.test_val))
            throw_to_monkey = self.test_true
        else:
            if self.show_print:
                print('     Current worry level is not divisible by' + str(self.test_val))
            throw_to_monkey = self.test_false
        if self.show_print:
            print('     Item with worry level ' + str(self.items[0]) + ' is thrown to monkey ' + str(throw_to_monkey))
        return throw_to_monkey
    
    def done_inspection(self, wl_level_mgmt):
        if self.show_print:
            print('     Monkey gets bored with item. Worry level is divided by 3 to ' + str(int(self.items[0] / wl_level_mgmt)))
        self.items[0] = int(self.items[0] / wl_level_mgmt)

    def done_inspection_B(self, wl_level_mgmt):
        if self.show_print:
            print('     Monkey gets bored with item. Worry level is divided by 3 to ' + str(int(self.items[0] % wl_level_mgmt)))
        self.items[0] = int(self.items[0] % wl_level_mgmt)

    def throw_item(self):
        return self.items.pop(0)
    
    def grab_item(self, item):
        return self.items.append(item)
    
    def show_items(self):
        print('Monkey ' + str(self.number) + ': ' + str(self.items)[1:-1])
    
    def show_inspections(self):
        print('Monkey ' + str(self.number) + ' inspected items ' + str(self.n_inspections) + ' times')
        return self.n_inspections
    
    def get_inspections(self):
        return self.n_inspections