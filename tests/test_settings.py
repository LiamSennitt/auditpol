from unittest import TestCase
from auditpol.subcategories import Subcategory
from auditpol.settings import _Setting, SettingValue, SubcategorySetting, OptionValue, AuditOption, \
    GlobalObjectAccessAuditSetting


class TestSetting(TestCase):
    def test_valid_machine_name(self):
        setting = _Setting(machine_name='TEST-MACHINE')
        self.assertEqual(setting.machine_name, 'TEST-MACHINE')

    def test_invalid_machine_name_type(self):
        with self.assertRaises(TypeError):
            _Setting(machine_name=None)


class TestSettingValue(TestCase):
    def test_default_success(self):
        settin_value = SettingValue()
        self.assertEqual(settin_value.success, False)

    def test_valid_success(self):
        settin_value = SettingValue(success=True)
        self.assertEqual(settin_value.success, True)

    def test_invalid_success_type(self):
        with self.assertRaises(TypeError):
            SettingValue(success=None)

    def test_default_failure(self):
        settin_value = SettingValue()
        self.assertEqual(settin_value.failure, False)

    def test_valid_failure(self):
        settin_value = SettingValue(failure=True)
        self.assertEqual(settin_value.failure, True)

    def test_invalid_failure_type(self):
        with self.assertRaises(TypeError):
            SettingValue(failure=None)

    def test_int_no_auditing(self):
        settin_value = SettingValue()
        self.assertEqual(int(settin_value), 0)

    def test_int_success(self):
        settin_value = SettingValue(success=True)
        self.assertEqual(int(settin_value), 1)

    def test_int_failure(self):
        settin_value = SettingValue(failure=True)
        self.assertEqual(int(settin_value), 2)

    def test_int_success_and_failure(self):
        settin_value = SettingValue(success=True, failure=True)
        self.assertEqual(int(settin_value), 3)

    def test_str_no_auditing(self):
        settin_value = SettingValue()
        self.assertEqual(str(settin_value), 'No Auditing')

    def test_str_success(self):
        settin_value = SettingValue(success=True)
        self.assertEqual(str(settin_value), 'Success')

    def test_str_failure(self):
        settin_value = SettingValue(failure=True)
        self.assertEqual(str(settin_value), 'Failure')

    def test_str_success_and_failure(self):
        settin_value = SettingValue(success=True, failure=True)
        self.assertEqual(str(settin_value), 'Success and Failure')

    def test_from_value_no_auditing(self):
        settin_value = SettingValue.from_value(0)
        self.assertEqual((settin_value.success, settin_value.failure), (False, False))

    def test_from_value_success(self):
        settin_value = SettingValue.from_value(1)
        self.assertEqual((settin_value.success, settin_value.failure), (True, False))

    def test_from_value_failure(self):
        settin_value = SettingValue.from_value(2)
        self.assertEqual((settin_value.success, settin_value.failure), (False, True))

    def test_from_value_success_and_failure(self):
        settin_value = SettingValue.from_value(3)
        self.assertEqual((settin_value.success, settin_value.failure), (True, True))

    def test_from_value_text_no_auditing(self):
        settin_value = SettingValue.from_value_text('No Auditing')
        self.assertEqual((settin_value.success, settin_value.failure), (False, False))

    def test_from_value_text_success(self):
        settin_value = SettingValue.from_value_text('Success')
        self.assertEqual((settin_value.success, settin_value.failure), (True, False))

    def test_from_value_text_failure(self):
        settin_value = SettingValue.from_value_text('Failure')
        self.assertEqual((settin_value.success, settin_value.failure), (False, True))

    def test_from_value_text_success_and_failure(self):
        settin_value = SettingValue.from_value_text('Success and Failure')
        self.assertEqual((settin_value.success, settin_value.failure), (True, True))


class TestSubcategorySetting(TestCase):
    def test_valid_subcategory(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue()
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.subcategory.id, '{00000000-0000-0000-0000-000000000000}')

    def test_invalid_subcategory_type(self):
        inclusion_setting = SettingValue()

        with self.assertRaises(TypeError):
            SubcategorySetting(subcategory=None, inclusion_setting=inclusion_setting)


    def test_valid_inclusion_setting(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue()
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.inclusion_setting.success, False)

    def test_invalid_inclusion_setting_type(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')

        with self.assertRaises(TypeError):
            SubcategorySetting(subcategory=subcategory, inclusion_setting=None)

    def test_value_include_no_auditing(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue()
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.value, 0)

    def test_value_include_success(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue(success=True)
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.value, 1)

    def test_value_include_failure(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue(failure=True)
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.value, 2)

    def test_value_include_success_and_failure(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue(success=True, failure=True)
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(subcategory_setting.value, 3)

    def test_from_csv(self):
        subcategory_setting = SubcategorySetting.from_csv(
            ',System,Example,{00000000-0000-0000-0000-000000000000},No Auditing,,0\n'
        )
        self.assertIsInstance(subcategory_setting, SubcategorySetting)

    def test_to_csv(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue()
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        self.assertEqual(
            subcategory_setting.to_csv(), 
            ',System,Example,{00000000-0000-0000-0000-000000000000},No Auditing,,0\n'
        )


class TestOptionValue(TestCase):
    def test_default_enabled(self):
        option_value = OptionValue()
        self.assertEqual(option_value.enabled, False)

    def test_valid_enabled(self):
        option_value = OptionValue(enabled=True)
        self.assertEqual(option_value.enabled, True)

    def test_invalid_enabled_type(self):
        with self.assertRaises(TypeError):
            OptionValue(enabled=None)

    def test_int_enabled(self):
        option_value = OptionValue(enabled=True)
        self.assertEqual(int(option_value), 1)

    def test_int_disabled(self):
        option_value = OptionValue(enabled=False)
        self.assertEqual(int(option_value), 0)

    def test_str_enabled(self):
        option_value = OptionValue(enabled=True)
        self.assertEqual(str(option_value), 'Enabled')

    def test_str_disabled(self):
        option_value = OptionValue(enabled=False)
        self.assertEqual(str(option_value), 'Disabled')

    def test_from_value_enabled(self):
        option_value = OptionValue.from_value(1)
        self.assertEqual(option_value.enabled, True)

    def test_from_value_disabled(self):
        option_value = OptionValue.from_value(0)
        self.assertEqual(option_value.enabled, False)


class TestAuditOption(TestCase):
    def test_valid_type(self):
        option_value = OptionValue()
        audit_option = AuditOption(type='CrashOnAuditFail', value=option_value)
        self.assertEqual(audit_option.type, 'CrashOnAuditFail')

    def test_invalid_type_type(self):
        option_value = OptionValue()

        with self.assertRaises(TypeError):
            AuditOption(type=None, value=option_value)

    def test_valid_value(self):
        option_value = OptionValue()
        audit_option = AuditOption(type='CrashOnAuditFail', value=option_value)
        self.assertEqual(audit_option.value.enabled, False)

    def test_invalid_value_type(self):
        with self.assertRaises(TypeError):
            AuditOption(type='CrashOnAuditFail', value=None)

    def test_from_csv(self):
        audit_option = AuditOption.from_csv(',,Option:CrashOnAuditFail,,Disabled,,0\n')
        self.assertIsInstance(audit_option, AuditOption)

    def test_to_csv(self):
        option_value = OptionValue()
        audit_option = AuditOption(type='CrashOnAuditFail', value=option_value)
        self.assertEqual(audit_option.to_csv(), ',,Option:CrashOnAuditFail,,Disabled,,0\n')


class TestGlobalObjectAccessAuditSetting(TestCase):
    def test_valid_type(self):
        global_object_access_audit_setting = GlobalObjectAccessAuditSetting(
            type='RegistryGlobalSacl',
            sacl='S:(AU;SA;FA;;;WD)'
        )
        self.assertEqual(global_object_access_audit_setting.type, 'RegistryGlobalSacl')


    def test_invalid_type_type(self):
        with self.assertRaises(TypeError):
            GlobalObjectAccessAuditSetting(type=None, sacl='S:(AU;SA;FA;;;WD)')

    def test_valid_sacl(self):
        global_object_access_audit_setting = GlobalObjectAccessAuditSetting(
            type='RegistryGlobalSacl',
            sacl='S:(AU;SA;FA;;;WD)'
        )
        self.assertEqual(global_object_access_audit_setting.sacl, 'S:(AU;SA;FA;;;WD)')

    def test_invalid_sacl_type(self):
        with self.assertRaises(TypeError):
            GlobalObjectAccessAuditSetting(type='RegistryGlobalSacl', sacl=None)

    def test_from_csv(self):
        global_object_access_audit_setting = GlobalObjectAccessAuditSetting.from_csv(
            ',,RegistryGlobalSacl,,,,S:(AU;SA;FA;;;WD)\n'
        )
        self.assertIsInstance(global_object_access_audit_setting, GlobalObjectAccessAuditSetting)

    def test_to_csv(self):
        global_object_access_audit_setting = GlobalObjectAccessAuditSetting(
            type='RegistryGlobalSacl',
            sacl='S:(AU;SA;FA;;;WD)'
        )
        self.assertEqual(global_object_access_audit_setting.to_csv(), ',,RegistryGlobalSacl,,,,S:(AU;SA;FA;;;WD)\n')
