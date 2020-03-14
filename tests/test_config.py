from collections import OrderedDict

test_config_data = OrderedDict([("std_input_format",
                                 "^(?P<name>[A-Z]+) (?P<msg>([A-Z]+\\s?)+)$"),
                                ("home_kingdom",
                                 "KINGDOMONE"),
                                ("num_of_allies_to_win",
                                 2),
                                ("emblems",
                                 OrderedDict([("KINGDOMONE",
                                               "EmblemOne"),
                                              ("KINGDOMTWO",
                                               "EmblemTwo"),
                                              ("KINGDOMTHREE",
                                               "EmblemThree"),
                                              ]))])
