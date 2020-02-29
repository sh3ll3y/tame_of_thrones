from collections import OrderedDict

test_config_data = OrderedDict([('std_input_format', '^([A-Z]+\\s?) ([A-Z]+\\s?)+$'),
             ('home_kingdom',
              OrderedDict([('name', 'EMBLEMONE'), ('num_of_kingdoms_to_win', 2)])),
             ('emblems',
              OrderedDict([('EMBLEMONE', 'AnimalOne'),
                           ('EMBLEMTWO', 'AnimalTwo'),
                           ('EMBLEMTHREE', 'AnimalThree')]))])