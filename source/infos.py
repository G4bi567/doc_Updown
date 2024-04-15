class DocumentInfos:

    title = u'UpDown'
    first_name = 'Gabriel'
    last_name = 'Teixeira Dias'
    author = f'{first_name} {last_name}'
    year = u'2024'
    month = u'Avril'
    seminary_title = u'Projet OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/G4bi567/UpDown"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()