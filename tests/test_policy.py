from unittest import TestCase
from auditpol.subcategories import Subcategory
from auditpol.settings import SettingValue, SubcategorySetting, OptionValue, AuditOption, GlobalObjectAccessAuditSetting
from auditpol.policy import AuditPolicy


class TestAuditPolicy(TestCase):
    def test_default_settings(self):
        policy = AuditPolicy()
        self.assertEqual(policy.settings, [])

    def test_valid_settings(self):
        policy = AuditPolicy(settings=[])
        self.assertEqual(policy.settings, [])

    def test_invalid_settings_type(self):
        with self.assertRaises(TypeError):
            AuditPolicy(settings=None)

    def test_valid_settings_element(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        inclusion_setting = SettingValue()
        subcategory_setting = SubcategorySetting(subcategory=subcategory, inclusion_setting=inclusion_setting)
        policy = AuditPolicy(settings=[subcategory_setting])
        self.assertEqual(policy.settings[0].subcategory.id, '{00000000-0000-0000-0000-000000000000}')

    def test_invalid_settings_element_type(self):
        with self.assertRaises(TypeError):
            AuditPolicy(settings=[None])

    def test_from_csv_subcategory_setting(self):
        header = 'Machine Name,Policy Target,Subcategory,Subcategory GUID,Inclusion Setting,Exclusion Setting,Setting Value'
        policy = AuditPolicy.from_csv([header, ',System,Example,{00000000-0000-0000-0000-000000000000},No Auditing,,0'])
        self.assertIsInstance(policy.settings[0], SubcategorySetting)

    def test_from_csv_audit_option(self):
        header = 'Machine Name,Policy Target,Subcategory,Subcategory GUID,Inclusion Setting,Exclusion Setting,Setting Value'
        policy = AuditPolicy.from_csv([header, ',,Option:CrashOnAuditFail,,Disabled,,0'])
        self.assertIsInstance(policy.settings[0], AuditOption)

    def test_from_csv_subcategory_setting(self):
        header = 'Machine Name,Policy Target,Subcategory,Subcategory GUID,Inclusion Setting,Exclusion Setting,Setting Value'
        policy = AuditPolicy.from_csv([header, ',,RegistryGlobalSacl,,,,S:(AU;SA;FA;;;WD)'])
        self.assertIsInstance(policy.settings[0], GlobalObjectAccessAuditSetting)
