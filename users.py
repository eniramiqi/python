class users:
    def __init__(self, arn, name):
     self.arn =arn
     self.name = name

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_arn(self):
        return self.arn    
    def set_arn(self, arn):
        self.name = arn
    def __str__(self):
        return "Useri me emrin " + self.name + " ka arn " + self.arn