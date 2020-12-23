# AuditPol

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/LiamSennitt/auditpol/build/main)](https://github.com/LiamSennitt/auditpol/actions?query=workflow%3Abuild+branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/auditpol)](https://pypi.org/project/auditpol/)
[![GitHub](https://img.shields.io/github/license/LiamSennitt/auditpol)](LICENSE)

The `auditpol` module allows you to easily parse and create Windows Audit Policy CSV files in Python.

## Installation

To install the `auditpol` module via pip, run the command:

```console
$ pip install auditpol
```

## Usage

Start by importing the `auditpol` module.

```python
>>> import auditpol
```

The function `auditpol.load`, loads an audit policy CSV file.

```python
>>> with open('example.csv', 'r') as file:
...     auditpol.load(file)
```

In addition to loading an existing audit policy, policies created using the relevant subcategory settings, audit options or global object access audit settings can be dumped to a CSV file using the `auditpol.dump` function.

```python
>>> with open('example.csv', 'w') as file:
...     auditpol.dump(policy, file)
```

### SubcategorySetting

To create a system subcategory setting as part of an audit policy, a `auditpol.subcategories.Subcategory` and a `auditpol.settings.SettingValue` must be created.

This can then be used to create a `auditpol.settings.SubcategorySetting`.

```python
>>> from auditpol.subcategories import Subcategory
>>> from auditpol.settings import SettingValue, SubcategorySetting

>>> subcategory = Subcategory(
...     id='{0CCE922B-69AE-11D9-BED3-505054503030}',
...     name='Process Creation'
... )

>>> inclusion_setting = SettingValue(
...     success=True,
...     failure=True
... )

>>> subcategory_setting = SubcategorySetting(
...     subcategory=subcategory,
...     inclusion_setting=inclusion_setting
... )
```

### AuditOption

To create an audit option as part of an audit policy, a `auditpol.settings.OptionValue` must be created.

This can then be used to create a `auditpol.settings.AuditOption`.

```python
>>> from auditpol.settings import OptionValue, AuditOption

>>> value = OptionValue(
...     enabled=True
... )

>>> audit_option = AuditOption(
...     type='CrashOnAuditFail'
...     value=value
... )
```

### GlobalObjectAccessAuditSetting

To create a global object access audit setting, a `auditpol.settings.GlobalObjectAccessAuditSetting` must be created.

```python
>>> from auditpol.settings import GlobalObjectAccessAuditSetting

>>> global_object_access_audit_setting = GlobalObjectAccessAuditSetting(
...     type='RegistryGlobalSacl'
...     sacl='S:(AU;SA;FA;;;WD)'
... )
```

### AuditPolicy

To create an audit policy one or more subcategory settings, audit options or global object access audit settings must be created as described above.

These settings can then be used to create an `auditpol.policy.AuditPolicy`.

```python
>>> from auditpol.policy import AuditPolicy

>>> policy = AppLockerPolicy(
...     settings=[
...         subcategory_setting,
...         audit_option,
...         global_object_access_audit_setting
...     ]
... )
```
