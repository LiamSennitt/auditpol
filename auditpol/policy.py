from auditpol.settings import SubcategorySetting, AuditOption, GlobalObjectAccessAuditSetting


class AuditPolicy():
    def __init__(self, *, settings=[]):
        self.settings = settings

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings):
        if isinstance(settings, list):
            for setting in settings:
                if isinstance(setting, (SubcategorySetting, AuditOption, GlobalObjectAccessAuditSetting)):
                    pass
                else:
                    raise TypeError(f'invalid type for settings element: {type(setting)}')
            self._settings = settings
        else:
            raise TypeError(f'invalid type for settings: {type(settings)}')

    @classmethod
    def from_csv(cls, rows):
        _ = rows.pop(0)

        settings = []

        for row in rows:
            _, subcategory, _, _, audit_option, _, _ = row.split(',')

            if subcategory:
                settings.append(SubcategorySetting.from_csv(row))
            elif audit_option:
                settings.append(AuditOption.from_csv(row))
            else:
                settings.append(GlobalObjectAccessAuditSetting.from_csv(row))

        return cls(settings=settings)

    def to_csv(self):
        yield 'Machine Name,Policy Target,Subcategory,Subcategory GUID,Inclusion Setting,Exclusion Setting,Setting Value\n'

        for setting in self.settings:
            yield setting.to_csv()
