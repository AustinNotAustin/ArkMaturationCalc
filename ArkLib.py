quetzal = "5 and 1/2 days"

maturation_a = ["mosasaur", "yutyrannus", "tusoteuthis"]

maturation_b = ["basilosaurus", "gacha", "plesiosaur"]

maturation_c = ["equus", "procoptodon"]

maturation_d = ["phiomia", "ovis"]

maturation_e = ["ichthyosaurus", "roll rat"]

maturation_f = ["compy", "otter", "jerboa"]

maturation_g = ["rhino", "doedicurus", "gasbag"]

maturation_h = ["dunkleosteus", "mammoth"]

all_dinos = {

    'Allosaurus': {'Name': 'Allosaurus', 'Min_Temp_C': '26', 'Max_Temp_C': '32', 'Min_Temp_F': '79',
                   'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '4:37',
                   'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                   'Total_Maturation_Time': '1:22:17'},
    'Anglerfish': {'Name': 'Anglerfish', 'Min_Temp_C': '-75', 'Max_Temp_C': '75', 'Min_Temp_F': '-103',
                   'Max_Temp_F': '167', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '3:42',
                   'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                   'Total_Maturation_Time': '1:13:02'},
    'Ankylosaurus': {'Name': 'Ankylosaurus', 'Min_Temp_C': '16', 'Max_Temp_C': '20', 'Min_Temp_F': '61',
                     'Max_Temp_F': '68', 'Egg_Incubation_Time': '2:37', 'Baby_Maturation_Time': '4:52',
                     'Juvenile_Maturation_Time': '19:29', 'Adolescent_Maturation_Time': '1:00:21',
                     'Total_Maturation_Time': '2:00:43'},
    'Archaeopteryx': {'Name': 'Archaeopteryx', 'Min_Temp_C': '16', 'Max_Temp_C': '20', 'Min_Temp_F': '61',
                      'Max_Temp_F': '68', 'Egg_Incubation_Time': '2:37', 'Baby_Maturation_Time': '1:32',
                      'Juvenile_Maturation_Time': '6:10', 'Adolescent_Maturation_Time': '7:42',
                      'Total_Maturation_Time': '15:25'},
    'Argentavis': {'Name': 'Argentavis', 'Min_Temp_C': '12', 'Max_Temp_C': '13.5', 'Min_Temp_F': '54',
                   'Max_Temp_F': '56', 'Egg_Incubation_Time': '2:56', 'Baby_Maturation_Time': '5:26',
                   'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                   'Total_Maturation_Time': '2:06:27'},
    'Baryonyx': {'Name': 'Baryonyx', 'Min_Temp_C': '29', 'Max_Temp_C': '35', 'Min_Temp_F': '84',
                 'Max_Temp_F': '95', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '4:37',
                 'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                 'Total_Maturation_Time': '1:22:17'},
    'Beelzebufo': {'Name': 'Beelzebufo', 'Min_Temp_C': '0', 'Max_Temp_C': '50', 'Min_Temp_F': '32',
                   'Max_Temp_F': '122', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '3:42',
                   'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                   'Total_Maturation_Time': '1:13:02'},
    'Bloodstalker': {'Name': 'Bloodstalker', 'Min_Temp_C': '27', 'Max_Temp_C': '30', 'Min_Temp_F': '81',
                     'Max_Temp_F': '86', 'Egg_Incubation_Time': '2:56', 'Baby_Maturation_Time': '5:26',
                     'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                     'Total_Maturation_Time': '2:06:27'},
    'Brontosaurus': {'Name': 'Brontosaurus', 'Min_Temp_C': '28', 'Max_Temp_C': '31', 'Min_Temp_F': '82',
                     'Max_Temp_F': '88', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
                     'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                     'Total_Maturation_Time': '3:20:35'},
    'Carbonemys': {'Name': 'Carbonemys', 'Min_Temp_C': '30', 'Max_Temp_C': '34', 'Min_Temp_F': '86',
                   'Max_Temp_F': '93', 'Egg_Incubation_Time': '1:14', 'Baby_Maturation_Time': '2:18',
                   'Juvenile_Maturation_Time': '9:15', 'Adolescent_Maturation_Time': '11:34',
                   'Total_Maturation_Time': '23:08'},
    'Carnotaurus': {'Name': 'Carnotaurus', 'Min_Temp_C': '26', 'Max_Temp_C': '32', 'Min_Temp_F': '79',
                    'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '4:37',
                    'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                    'Total_Maturation_Time': '1:22:17'},
    'Compy': {'Name': 'Compy', 'Min_Temp_C': '24', 'Max_Temp_C': '32', 'Min_Temp_F': '75',
                    'Max_Temp_F': '90', 'Egg_Incubation_Time': '0:49', 'Baby_Maturation_Time': '2:06',
                    'Juvenile_Maturation_Time': '8:25', 'Adolescent_Maturation_Time': '10:31',
                    'Total_Maturation_Time': '21:02'},
    'Crystal Wyvern': {'Name': 'Crystal Wyvern', 'Min_Temp_C': '75', 'Max_Temp_C': '85', 'Min_Temp_F': '167',
                       'Max_Temp_F': '185', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
                       'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                       'Total_Maturation_Time': '3:20:35'},
    'Deinonychus': {'Name': 'Deinonychus', 'Min_Temp_C': '80', 'Max_Temp_C': '90', 'Min_Temp_F': '176',
                    'Max_Temp_F': '194', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '3:42',
                    'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                    'Total_Maturation_Time': '1:13:02'},
    'Dilophosaur': {'Name': 'Dilophosaur', 'Min_Temp_C': '28', 'Max_Temp_C': '32', 'Min_Temp_F': '82',
                    'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:08', 'Baby_Maturation_Time': '2:06',
                    'Juvenile_Maturation_Time': '8:25', 'Adolescent_Maturation_Time': '10:31',
                    'Total_Maturation_Time': '21:02'},
    'Dimetrodon': {'Name': 'Dimetrodon', 'Min_Temp_C': '30', 'Max_Temp_C': '34', 'Min_Temp_F': '86',
                   'Max_Temp_F': '93', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:37',
                   'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                   'Total_Maturation_Time': '1:22:17'},
    'Dimorphodon': {'Name': 'Dimorphodon', 'Min_Temp_C': '35', 'Max_Temp_C': '38', 'Min_Temp_F': '95',
                    'Max_Temp_F': '100', 'Egg_Incubation_Time': '1:21', 'Baby_Maturation_Time': '2:30',
                    'Juvenile_Maturation_Time': '10:00', 'Adolescent_Maturation_Time': '12:30',
                    'Total_Maturation_Time': '1:01:01'},
    'Diplocaulus': {'Name': 'Diplocaulus', 'Min_Temp_C': '0', 'Max_Temp_C': '50', 'Min_Temp_F': '32',
                    'Max_Temp_F': '122', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '3:42',
                    'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                    'Total_Maturation_Time': '1:13:02'},
    'Diplodocus': {'Name': 'Diplodocus', 'Min_Temp_C': '26', 'Max_Temp_C': '29', 'Min_Temp_F': '79',
                   'Max_Temp_F': '84', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
                   'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                   'Total_Maturation_Time': '3:20:35'},
    'Dodo': {'Name': 'Dodo', 'Min_Temp_C': '22', 'Max_Temp_C': '30', 'Min_Temp_F': '72',
                    'Max_Temp_F': '86', 'Egg_Incubation_Time': '0:49', 'Baby_Maturation_Time': '1:32',
                    'Juvenile_Maturation_Time': '6:10', 'Adolescent_Maturation_Time': '7:42',
                    'Total_Maturation_Time': '15:25'},
    'Electrophorus': {'Name': 'Electrophorus', 'Min_Temp_C': '0', 'Max_Temp_C': '50', 'Min_Temp_F': '32',
                      'Max_Temp_F': '122', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '4:37',
                      'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                      'Total_Maturation_Time': '1:22:17'},
    'Featherlight': {'Name': 'Featherlight', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                     'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '4:52',
                     'Juvenile_Maturation_Time': '19:29', 'Adolescent_Maturation_Time': '1:00:21',
                     'Total_Maturation_Time': '2:00:43'},
    'Gallimimus': {'Name': 'Gallimimus', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                   'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '2:38',
                   'Juvenile_Maturation_Time': '10:34', 'Adolescent_Maturation_Time': '13:13',
                   'Total_Maturation_Time': '1:02:27'},
    'Giganotosaurus': {'Name': 'Giganotosaurus', 'Min_Temp_C': '43', 'Max_Temp_C': '44', 'Min_Temp_F': '109',
                       'Max_Temp_F': '111', 'Egg_Incubation_Time': '2:01:59', 'Baby_Maturation_Time': '1:04:03',
                       'Juvenile_Maturation_Time': '4:16:14', 'Adolescent_Maturation_Time': '5:20:17',
                       'Total_Maturation_Time': '11:16:35'},
    'Glowtail': {'Name': 'Glowtail', 'Min_Temp_C': '30', 'Max_Temp_C': '34', 'Min_Temp_F': '86',
                 'Max_Temp_F': '93', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:52',
                 'Juvenile_Maturation_Time': '19:29', 'Adolescent_Maturation_Time': '1:00:21',
                 'Total_Maturation_Time': '2:00:43'},
    'Hesperornis': {'Name': 'Hesperornis', 'Min_Temp_C': '22', 'Max_Temp_C': '30', 'Min_Temp_F': '72',
                    'Max_Temp_F': '86', 'Egg_Incubation_Time': '1:30', 'Baby_Maturation_Time': '2:48',
                    'Juvenile_Maturation_Time': '11:13', 'Adolescent_Maturation_Time': '14:01',
                    'Total_Maturation_Time': '1:04:03'},
    'Ichthyornis': {'Name': 'Ichthyornis', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                    'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '3:42',
                    'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                    'Total_Maturation_Time': '1:13:02'},
    'Iguanodon': {'Name': 'Iguanodon', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                  'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '4:37',
                  'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                  'Total_Maturation_Time': '1:22:17'},
    'Kairuku': {'Name': 'Kairuku', 'Min_Temp_C': '22', 'Max_Temp_C': '30', 'Min_Temp_F': '72',
                'Max_Temp_F': '86', 'Egg_Incubation_Time': '1:30', 'Baby_Maturation_Time': '2:48',
                'Juvenile_Maturation_Time': '11:13', 'Adolescent_Maturation_Time': '14:01',
                'Total_Maturation_Time': '1:04:03'},
    'Kaprosuchus': {'Name': 'Kaprosuchus', 'Min_Temp_C': '29', 'Max_Temp_C': '35', 'Min_Temp_F': '84',
                    'Max_Temp_F': '95', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '3:42',
                    'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                    'Total_Maturation_Time': '1:13:02'},
    'Kentrosaurus': {'Name': 'Kentrosaurus', 'Min_Temp_C': '24', 'Max_Temp_C': '30', 'Min_Temp_F': '75',
                     'Max_Temp_F': '86', 'Egg_Incubation_Time': '2:46', 'Baby_Maturation_Time': '5:08',
                     'Juvenile_Maturation_Time': '20:34', 'Adolescent_Maturation_Time': '1:01:43',
                     'Total_Maturation_Time': '2:03:26'},
    'Lystrosaurus': {'Name': 'Lystrosaurus', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                     'Max_Temp_F': '82', 'Egg_Incubation_Time': '0:49', 'Baby_Maturation_Time': '1:32',
                     'Juvenile_Maturation_Time': '6:10', 'Adolescent_Maturation_Time': '7:42',
                     'Total_Maturation_Time': '15:25'},
    'Magmasaur': {'Name': 'Magmasaur', 'Min_Temp_C': '90', 'Max_Temp_C': '110', 'Min_Temp_F': '194',
                  'Max_Temp_F': '230', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '18:31',
                  'Juvenile_Maturation_Time': '3:02:04', 'Adolescent_Maturation_Time': '3:20:35',
                  'Total_Maturation_Time': '7:17:11'},
    'Megachelon': {'Name': 'Megachelon', 'Min_Temp_C': '-75', 'Max_Temp_C': '75', 'Min_Temp_F': '-103',
                   'Max_Temp_F': '167', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
                   'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                   'Total_Maturation_Time': '3:20:35'},
    'Megalania': {'Name': 'Megalania', 'Min_Temp_C': '29', 'Max_Temp_C': '35', 'Min_Temp_F': '84',
                  'Max_Temp_F': '95', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '3:42',
                  'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                  'Total_Maturation_Time': '1:13:02'},
    'Megalosaurus': {'Name': 'Megalosaurus', 'Min_Temp_C': '26', 'Max_Temp_C': '32', 'Min_Temp_F': '79',
                     'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '9:15',
                     'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                     'Total_Maturation_Time': '3:20:35'},
    'Microraptor': {'Name': 'Microraptor', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                    'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '5:26',
                    'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                    'Total_Maturation_Time': '2:06:27'},
    'Morellatops': {'Name': 'Morellatops', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                    'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '3:05',
                    'Juvenile_Maturation_Time': '12:20', 'Adolescent_Maturation_Time': '15:25',
                    'Total_Maturation_Time': '1:06:51'},
    'Moschops': {'Name': 'Moschops', 'Min_Temp_C': '16', 'Max_Temp_C': '20', 'Min_Temp_F': '61',
                 'Max_Temp_F': '68', 'Egg_Incubation_Time': '2:37', 'Baby_Maturation_Time': '4:52',
                 'Juvenile_Maturation_Time': '19:29', 'Adolescent_Maturation_Time': '1:00:21',
                 'Total_Maturation_Time': '2:00:43'},
    'Oviraptor': {'Name': 'Oviraptor', 'Min_Temp_C': '26', 'Max_Temp_C': '30', 'Min_Temp_F': '79',
                  'Max_Temp_F': '86', 'Egg_Incubation_Time': '1:08', 'Baby_Maturation_Time': '2:06',
                  'Juvenile_Maturation_Time': '8:25', 'Adolescent_Maturation_Time': '10:31',
                  'Total_Maturation_Time': '21:02'},
    'Pachy': {'Name': 'Pachy', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
              'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '2:38',
              'Juvenile_Maturation_Time': '10:34', 'Adolescent_Maturation_Time': '13:13',
              'Total_Maturation_Time': '1:02:27'},
    'Pachyrhinosaurus': {'Name': 'Pachyrhinosaurus', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                         'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:37',
                         'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                         'Total_Maturation_Time': '1:22:17'},
    'Parasaur': {'Name': 'Parasaur', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                 'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '2:38',
                 'Juvenile_Maturation_Time': '10:34', 'Adolescent_Maturation_Time': '13:13',
                 'Total_Maturation_Time': '1:02:27'},
    'Pegomastax': {'Name': 'Pegomastax', 'Min_Temp_C': '28', 'Max_Temp_C': '32', 'Min_Temp_F': '82',
                   'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:08', 'Baby_Maturation_Time': '3:05',
                   'Juvenile_Maturation_Time': '12:20', 'Adolescent_Maturation_Time': '15:25',
                   'Total_Maturation_Time': '1:06:51'},
    'Pelagornis': {'Name': 'Pelagornis', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                   'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '3:42',
                   'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                   'Total_Maturation_Time': '1:13:02'},
    'Pteranodon': {'Name': 'Pteranodon', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                   'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '3:42',
                   'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                   'Total_Maturation_Time': '1:13:02'},
    'Quetzal': {'Name': 'Quetzal', 'Min_Temp_C': '5', 'Max_Temp_C': '6', 'Min_Temp_F': '41',
                'Max_Temp_F': '43', 'Egg_Incubation_Time': '16:39', 'Baby_Maturation_Time': '13:13',
                'Juvenile_Maturation_Time': '2:04:54', 'Adolescent_Maturation_Time': '2:18:08',
                'Total_Maturation_Time': '5:12:16'},
    'Raptor': {'Name': 'Raptor', 'Min_Temp_C': '20', 'Max_Temp_C': '28', 'Min_Temp_F': '68',
               'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '3:42',
               'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
               'Total_Maturation_Time': '1:13:02'},
    'Rex': {'Name': 'Rex', 'Min_Temp_C': '32', 'Max_Temp_C': '34', 'Min_Temp_F': '90',
            'Max_Temp_F': '93', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
            'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
            'Total_Maturation_Time': '3:20:35'},
    'Rock Drake': {'Name': 'Rock Drake', 'Min_Temp_C': '-90', 'Max_Temp_C': '-80', 'Min_Temp_F': '-130',
                   'Max_Temp_F': '-112', 'Egg_Incubation_Time': '6:14', 'Baby_Maturation_Time': '9:15',
                   'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                   'Total_Maturation_Time': '3:20:35'},
    'Sarco': {'Name': 'Sarco', 'Min_Temp_C': '30', 'Max_Temp_C': '34', 'Min_Temp_F': '86',
              'Max_Temp_F': '93', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:37',
              'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
              'Total_Maturation_Time': '1:22:17'},
    'Snow Owl': {'Name': 'Snow Owl', 'Min_Temp_C': '12', 'Max_Temp_C': '13.5', 'Min_Temp_F': '54',
                 'Max_Temp_F': '56', 'Egg_Incubation_Time': '2:56', 'Baby_Maturation_Time': '5:26',
                 'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                 'Total_Maturation_Time': '2:06:27'},
    'Spino': {'Name': 'Spino', 'Min_Temp_C': '30', 'Max_Temp_C': '32', 'Min_Temp_F': '86',
              'Max_Temp_F': '90', 'Egg_Incubation_Time': '3:50', 'Baby_Maturation_Time': '7:07',
              'Juvenile_Maturation_Time': '1:04:29', 'Adolescent_Maturation_Time': '1:11:36',
              'Total_Maturation_Time': '2:23:13'},
    'Stegosaurus': {'Name': 'Stegosaurus', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                    'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:46', 'Baby_Maturation_Time': '5:08',
                    'Juvenile_Maturation_Time': '20:34', 'Adolescent_Maturation_Time': '1:01:43',
                    'Total_Maturation_Time': '2:03:26'},
    'Tapejara': {'Name': 'Tapejara', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                 'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '5:26',
                 'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                 'Total_Maturation_Time': '2:06:27'},
    'Tek Parasaur': {'Name': 'Tek Parasaur', 'Min_Temp_C': '24', 'Max_Temp_C': '28', 'Min_Temp_F': '75',
                     'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:25', 'Baby_Maturation_Time': '2:38',
                     'Juvenile_Maturation_Time': '10:34', 'Adolescent_Maturation_Time': '13:13',
                     'Total_Maturation_Time': '1:02:27'},
    'Tek Quetzal': {'Name': 'Tek Quetzal', 'Min_Temp_C': '5', 'Max_Temp_C': '6', 'Min_Temp_F': '41',
                    'Max_Temp_F': '43', 'Egg_Incubation_Time': '16:39', 'Baby_Maturation_Time': '13:13',
                    'Juvenile_Maturation_Time': '2:04:54', 'Adolescent_Maturation_Time': '2:18:08',
                    'Total_Maturation_Time': '5:12:16'},
    'Tek Raptor': {'Name': 'Tek Raptor', 'Min_Temp_C': '20', 'Max_Temp_C': '28', 'Min_Temp_F': '68',
                   'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '3:42',
                   'Juvenile_Maturation_Time': '14:48', 'Adolescent_Maturation_Time': '18:31',
                   'Total_Maturation_Time': '1:13:02'},
    'Tek Rex': {'Name': 'Tek Rex', 'Min_Temp_C': '32', 'Max_Temp_C': '34', 'Min_Temp_F': '90',
                'Max_Temp_F': '93', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
                'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
                'Total_Maturation_Time': '3:20:35'},
    'Tek Stegosaurus': {'Name': 'Tek Stegosaurus', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                        'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:46', 'Baby_Maturation_Time': '5:08',
                        'Juvenile_Maturation_Time': '20:34', 'Adolescent_Maturation_Time': '1:01:43',
                        'Total_Maturation_Time': '2:03:26'},
    'Terror Bird': {'Name': 'Terror Bird', 'Min_Temp_C': '20', 'Max_Temp_C': '28', 'Min_Temp_F': '68',
                    'Max_Temp_F': '82', 'Egg_Incubation_Time': '1:59', 'Baby_Maturation_Time': '4:37',
                    'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                    'Total_Maturation_Time': '1:22:17'},
    'Therizinosaur': {'Name': 'Therizinosaur', 'Min_Temp_C': '26', 'Max_Temp_C': '32', 'Min_Temp_F': '79',
                      'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '11:34',
                      'Juvenile_Maturation_Time': '1:22:17', 'Adolescent_Maturation_Time': '2:09:52',
                      'Total_Maturation_Time': '4:19:44'},
    'Thorny Dragon': {'Name': 'Thorny Dragon', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                      'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:52',
                      'Juvenile_Maturation_Time': '19:29', 'Adolescent_Maturation_Time': '1:00:21',
                      'Total_Maturation_Time': '2:00:43'},
    'Triceratops': {'Name': 'Triceratops', 'Min_Temp_C': '22', 'Max_Temp_C': '28', 'Min_Temp_F': '72',
                    'Max_Temp_F': '82', 'Egg_Incubation_Time': '2:29', 'Baby_Maturation_Time': '4:37',
                    'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                    'Total_Maturation_Time': '1:22:17'},
    'Troodon': {'Name': 'Troodon', 'Min_Temp_C': '28', 'Max_Temp_C': '32', 'Min_Temp_F': '82',
                'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:08', 'Baby_Maturation_Time': '2:06',
                'Juvenile_Maturation_Time': '8:25', 'Adolescent_Maturation_Time': '10:31',
                'Total_Maturation_Time': '21:02'},
    'Tropeognathus': {'Name': 'Tropeognathus', 'Min_Temp_C': '29', 'Max_Temp_C': '32', 'Min_Temp_F': '84',
                      'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:39', 'Baby_Maturation_Time': '5:26',
                      'Juvenile_Maturation_Time': '21:47', 'Adolescent_Maturation_Time': '1:03:13',
                      'Total_Maturation_Time': '2:06:27'},
    'Tusoteuthis': {'Name': 'Tusoteuthis', 'Min_Temp_C': '0', 'Max_Temp_C': '50', 'Min_Temp_F': '32',
                    'Max_Temp_F': '122', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '18:31',
                    'Juvenile_Maturation_Time': '3:02:04', 'Adolescent_Maturation_Time': '3:20:35',
                    'Total_Maturation_Time': '7:17:11'},
    'Velonasaur': {'Name': 'Velonasaur', 'Min_Temp_C': '28', 'Max_Temp_C': '32', 'Min_Temp_F': '82',
                   'Max_Temp_F': '90', 'Egg_Incubation_Time': '1:08', 'Baby_Maturation_Time': '4:37',
                   'Juvenile_Maturation_Time': '18:31', 'Adolescent_Maturation_Time': '23:08',
                   'Total_Maturation_Time': '1:22:17'},
    'Vulture': {'Name': 'Vulture', 'Min_Temp_C': '35', 'Max_Temp_C': '38', 'Min_Temp_F': '95',
                'Max_Temp_F': '100', 'Egg_Incubation_Time': '1:21', 'Baby_Maturation_Time': '2:30',
                'Juvenile_Maturation_Time': '10:00', 'Adolescent_Maturation_Time': '12:30',
                'Total_Maturation_Time': '1:01:01'},
    'Wyvern': {'Name': 'Wyvern', 'Min_Temp_C': '80', 'Max_Temp_C': '90', 'Min_Temp_F': '176',
               'Max_Temp_F': '194', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '9:15',
               'Juvenile_Maturation_Time': '1:13:02', 'Adolescent_Maturation_Time': '1:22:17',
               'Total_Maturation_Time': '3:20:35'},
    'Yutyrannus': {'Name': 'Yutyrannus', 'Min_Temp_C': '32', 'Max_Temp_C': '34', 'Min_Temp_F': '90',
                   'Max_Temp_F': '93', 'Egg_Incubation_Time': '4:59', 'Baby_Maturation_Time': '18:31',
                   'Juvenile_Maturation_Time': '3:02:04', 'Adolescent_Maturation_Time': '3:20:35',
                   'Total_Maturation_Time': '7:17:11'}
}


all_dino_names = ['Allosaurus', 'Anglerfish', 'Ankylosaurus', 'Archaeopteryx', 'Argentavis', 'Baryonyx', 'Beelzebufo',
                  'Bloodstalker', 'Brontosaurus', 'Carbonemys', 'Carnotaurus', 'Compy', 'Crystal Wyvern', 'Deinonychus',
                  'Dilophosaur', 'Dimetrodon', 'Dimorphodon', 'Diplocaulus', 'Diplodocus', 'Dodo', 'Electrophorus',
                  'Featherlight', 'Gallimimus', 'Giganotosaurus', 'Glowtail', 'Hesperornis', 'Ichthyornis', 'Iguanodon',
                  'Kairuku', 'Kaprosuchus', 'Kentrosaurus', 'Lystrosaurus', 'Magmasaur', 'Megachelon', 'Megalania',
                  'Megalosaurus', 'Microraptor', 'Morellatops', 'Moschops', 'Oviraptor', 'Pachy', 'Pachyrhinosaurus',
                  'Parasaur', 'Pegomastax', 'Pelagornis', 'Pteranodon', 'Quetzal', 'Raptor', 'Rex', 'Rock Drake',
                  'Sarco', 'Snow Owl', 'Spino', 'Stegosaurus', 'Tapejara', 'Tek Parasaur', 'Tek Quetzal', 'Tek Raptor',
                  'Tek Rex', 'Tek Stegosaurus', 'Terror Bird', 'Therizinosaur', 'Thorny Dragon', 'Triceratops',
                  'Troodon', 'Tropeognathus', 'Tusoteuthis', 'Velonasaur', 'Vulture', 'Wyvern', 'Yutyrannus'
                  ]


def seconds_to_time(total_seconds):
    """Send time in secodn here to convert it into a time list"""
    total_minutes = int(total_seconds / 60)
    total_hours = int(total_minutes / 60)
    total_days = int(total_hours / 24)
    remaining_minutes = int(total_minutes - (total_hours * 60))
    remaining_hours = int(total_hours - (total_days * 24))
    new_list = [total_days, remaining_hours, remaining_minutes]
    return new_list


def time_to_seconds(time_list):
    """Enter a string of time in the format dd:hh:mm or hh:mm and it will return the total seconds"""
    if len(time_list) == 3:
        days = time_list[0]
        hours = time_list[1]
        mins = time_list[2]
        seconds = (days * 86400) + (hours * 3600) + (mins * 60)
        return seconds
    elif len(time_list) == 2:
        hours = time_list[0]
        mins = time_list[1]
        seconds = (hours * 3600) + (mins * 60)
        return seconds
    else:
        print("error in list size")


def conv_str_to_time(str_time):
    """Enter a string of time in the format dd:hh:mm or hh:mm and it will return the time in list format"""
    split_text = str_time.split(':')
    new_list = []
    for x in split_text:
        new = int(x)
        new_list.append(new)
    if len(new_list) == 3:
        return new_list
    elif len(new_list) == 2:
        new_list.insert(0, 0)
        return new_list
    else:
        print("error in the len of list: conv_str_time func")


def display_time(name, time_list, goal):
    if int(time_list[0]) == 0:
        return f"{name} will take {time_list[1]}h and {time_list[2]}m until {goal}"
    elif int(time_list[0]) >= 1:
        return f"{name} will take {time_list[0]}d, {time_list[1]}h, and {time_list[2]}m until {goal}"


def get_total_maturation_str(name):
    return all_dinos[name]["Total_Maturation_Time"]
