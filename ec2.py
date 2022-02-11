class ec2:
    def __init__(self, name, ami, model, dns):
        self.name = name 
        self.ami = ami
        self.model = model
        self.dns = dns
        # getter and setter methods

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_ami(self):
        return self.ami
    def set_ami(self, ami):
        self.ami = ami

    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model

    def get_dns(self):
        return self.dns
    def set_dns(self, dns):
        self.dns = dns
    def __str__(self):
        return "EC2 me emrin" + self.name + " ka AMI " + self.ami