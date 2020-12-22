from auditpol.policy import AuditPolicy


def dump(policy, stream):
    for row in policy.to_csv():
        stream.write(row)


def load(stream):
    return AuditPolicy.from_csv(stream.readlines())
