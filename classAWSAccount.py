class AWSAccount:
  def __init__(self, id):
    self.account_id = id
    self.account_name = ""
    self.ec2_instances = []
    self.iam_users = []

  def get_users(self):
    pass

  def write_user_to_csv_file(self, file):
    pass

  def get_instances(self):
    pass

  def write_instances_to_ddb(self, table):
    pass