from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=50)

class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)


class Location(models.Model):
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)

class Test_Standard(models.Model):
   sequence_name = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    cell_technology = models.CharField(max_length=200)
    cell_manufacturer = models.CharField(max_length=200)
    num_of_cells = models.IntegerField(default=0)
    num_of_cells_in_series = models.IntegerField(default=0)
    num_of_series_strings = models.IntegerField(default=0)
    num_of_diodes = models.IntegerField(default=0)
    product_length = models.CharField(max_length=200)
    product_width = models.CharField(max_length=200)
    superstate_manufacturer = models.CharField(max_length=200)
    substrate_type = models.CharField(max_length=200)
    substrate_manufacturer = models.CharField(max_length=200)
    frame_type = models.CharField(max_length=200)
    frame_adhesive = models.CharField(max_length=200)
    encapsulate_type = models.CharField(max_length=200)
    encapsulate_manufacturer = models.CharField(max_length=200)
    junction_box_type = models.CharField(max_length=200)
    junction_box_manufacturer = models.CharField(max_length=200)

class Certificate(models.Model):
    cert_id = models.CharField(max_length=50)
    report_number = models.CharField(max_length=50)
    issue_date = models.CharField(max_length=50)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
    location_ID = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_num = models.ForeignKey(Product, on_delete=models.CASCADE)

class Performance_Data(models.Model):
    model_number = models.CharField(max_length=200)
    sequence_ID = models.CharField(max_length=200)
    max_system_voltage = models.CharField(max_length=200)
    voc = models.CharField(max_length=200)
    isc = models.CharField(max_length=200)
    vmp = models.CharField(max_length=200)
    imp = models.CharField(max_length=200)
    pmp = models.CharField(max_length=200)
    ff = models.CharField(max_length=200)


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_FI_required = models.CharField(max_length=50)
    FI_freqeuncy = models.CharField(max_length=50)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)

class Test_Sequence(models.Model):
    sequence_name = models.CharField(max_length=200)
