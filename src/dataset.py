class EmptyColumnError(ValueError): pass

class Dataset:
    #TODO
    # iterator ekle tek tek sonuc verebilsin
    column_types = {'human': ['name', 'email', 'date', 'company', 'bank_acc', 'phone'],
                    'geo': ['street_addr', 'city', 'postal_zip','region', 'country','latitude_longitude'],
                    'credit_card': ['pan', 'pin','cvv', 'track1', 'track2'],
                    'numeric': ['alphanumeric', 'auto_increment', 'number_range','currency'],
                                    }

    def __init__(self, collist=None, csvfile=None):
        if collist == None and csvfile == None:
            raise EmptyColumnError('Either csv file or column list should be existed, both of them can not be empty...')

        self.columns = collist if None else []
        self.file = csvfile
        
        if csvfile:
            with open(csvfile, encoding="utf-8") as file:
                for line in file:
                    vals = line.rstrip().split(',')
                    self.columns.append( (vals[0].strip(), vals[1].strip(), vals[2].strip()))

    def coltype(self, category, coltype, name):
        #check valid type
        try:
            if coltype in self.column_types[category]:
                print('oo yeaah')
            else: print('not sooo fast!')
        except KeyError as exc:
            print('This is not a valid key: "%s"' % exc.args[0])
