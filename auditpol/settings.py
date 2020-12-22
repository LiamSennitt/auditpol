from auditpol.subcategories import Subcategory


class _Setting():
    def __init__(self, *, machine_name):
        self.machine_name = machine_name

    @property
    def machine_name(self):
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        if isinstance(machine_name, str):
            self._machine_name = machine_name
        else:
            raise TypeError(f'invalid type for machine_name: {type(machine_name)}')


class SettingValue():
    _value = ((None, None), (True, False), (False, True), (True, True), (False, False))
    _value_text = ('', 'Success', 'Failure', 'Success and Failure', 'No Auditing')

    def __init__(self, *, success=None, failure=None):
        self.success = success
        self.failure = failure

    def __int__(self):
        return self._value.index((self.success, self.failure))

    def __str__(self):
        return self._value_text[int(self)]

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, success):
        if success is None or isinstance(success, bool):
            self._success = success
        else:
            raise TypeError(f'invalid type for success: {type(success)}')

    @property
    def failure(self):
        return self._failure

    @failure.setter
    def failure(self, failure):
        if failure is None or isinstance(failure, bool):
            self._failure = failure
        else:
            raise TypeError(f'invalid type for failure: {type(failure)}')

    @classmethod
    def from_value(cls, value):
        success, failure = cls._value[value]
        return cls(success=success, failure=failure)

    @classmethod
    def from_value_text(cls, value_text):
        value = cls._value_text.index(value_text)
        return cls.from_value(value)


class SubcategorySetting(_Setting):
    def __init__(self, *, machine_name='', policy_target='System', subcategory, inclusion_setting, exclusion_setting):
        super(SubcategorySetting, self).__init__(machine_name=machine_name)
        self.policy_target = policy_target
        self.subcategory = subcategory
        self.inclusion_setting = inclusion_setting
        self.exclusion_setting = exclusion_setting

    @property
    def policy_target(self):
        return self._policy_target

    @policy_target.setter
    def policy_target(self, policy_target):
        if isinstance(policy_target, str):
            self._policy_target = policy_target
        else:
            raise TypeError(f'invalid type for policy_target: {type(policy_target)}')

    @property
    def subcategory(self):
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        if isinstance(subcategory, Subcategory):
            self._subcategory = subcategory
        else:
            raise TypeError(f'invalid type for subcategory: {type(subcategory)}')

    @property
    def inclusion_setting(self):
        return self._inclusion_setting

    @inclusion_setting.setter
    def inclusion_setting(self, inclusion_setting):
        if isinstance(inclusion_setting, SettingValue):
            self._inclusion_setting = inclusion_setting
        else:
            raise TypeError(f'invalid type for inclusion_setting: {type(inclusion_setting)}')

    @property
    def exclusion_setting(self):
        return self._exclusion_setting

    @exclusion_setting.setter
    def exclusion_setting(self, exclusion_setting):
        if isinstance(exclusion_setting, SettingValue):
            self._exclusion_setting = exclusion_setting
        else:
            raise TypeError(f'invalid type for exclusion_setting: {type(exclusion_setting)}')

    @property
    def value(self):
        return int(self.inclusion_setting)

    @classmethod
    def from_csv(cls, row):
        machine_name, policy_target, name, id, inclusion_value_text, exclusion_value_text, _ = row.split(',')

        inclusion_setting = SettingValue.from_value_text(inclusion_value_text)
        exclusion_setting = SettingValue.from_value_text(exclusion_value_text)

        return cls(
            machine_name=machine_name,
            policy_target=policy_target,
            subcategory=Subcategory(
                id=id,
                name=name
            ),
            inclusion_setting=inclusion_setting,
            exclusion_setting=exclusion_setting
        )


    def to_csv(self):
        return (
            f'{self.machine_name},{self.policy_target},{self.subcategory.name},{self.subcategory.id},'
            f'{str(self.inclusion_setting)},{str(self.exclusion_setting)},{self.value}\n'
        )


class OptionValue():
    def __init__(self, *, enabled):
        self.enabled = enabled

    def __int__(self):
        return self._value

    def __str__(self):
        return ('Disabled', 'Enabled')[int(self)]

    @property
    def enabled(self):
        return bool(self._value)

    @enabled.setter
    def enabled(self, enabled):
        if isinstance(enabled, bool):
            self._value = int(enabled)
        else:
            raise TypeError(f'invalid type for enabled: {type(enabled)}')

    @classmethod
    def from_value(cls, value):
        return cls(enabled=int(value))


class AuditOption(_Setting):
    def __init__(self, *, machine_name='', type, value):
        super(AuditOption, self).__init__(machine_name=machine_name)
        self.type = type
        self.value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError(f'invalid type for type: {type(type)}')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, OptionValue):
            self._value = value
        else:
            raise TypeError(f'invalid type for value: {type(value)}')

    @classmethod
    def from_csv(cls, row):
        machine_name, _, option, _, _, _, value = row.split(',')
        _, type = option.split(':')

        return cls(
            machine_name=machine_name,
            type=type,
            value=OptionValue.from_value(value)
        )

    def to_csv(self):
        return f'{self.machine_name},,Option:{self.type},,{str(self.value)},,{int(self.value)}\n'


class GlobalObjectAccessAuditSetting(_Setting):
    def __init__(self, *, machine_name='', type, sacl):
        super(GlobalObjectAccessAuditSetting, self).__init__(machine_name=machine_name)
        self.type = type
        self.sacl = sacl

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError(f'invalid type for type: {type(type)}')

    @property
    def sacl(self):
        return self._sacl

    @sacl.setter
    def sacl(self, sacl):
        if isinstance(sacl, str):
            self._sacl = sacl
        else:
            raise TypeError(f'invalid type for sacl: {type(sacl)}')

    @classmethod
    def from_csv(cls, row):
        machine_name, _, type, _, _, _, sacl = row.split(',')

        return cls(
            machine_name=machine_name,
            type=type,
            sacl=sacl
        )

    def to_csv(self):
        return f'{self.machine_name},,{self.type},,,,{int(self.sacl)}\n'
