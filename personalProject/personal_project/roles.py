from rolepermissions.roles import AbstractUserRole

class RaidLeader(AbstractUserRole):
    available_permissions = {
        'create_strat': True,
        'edit_strat': True,

    }

class RaidAssist(AbstractUserRole):
    available_permissions = {
        'edit_strat': True,
        'create_strat': False,
    }