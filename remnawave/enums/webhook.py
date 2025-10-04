from typing import Literal

# ---------------- ENUMS / CONSTANTS ---------------- #

TNodeEvents = Literal[
    "node.created",
    "node.modified",
    "node.disabled",
    "node.enabled",
    "node.deleted",
    "node.connection_lost",
    "node.connection_restored",
    "node.traffic_notify",
]

TUserEvents = Literal[
    "user.created",
    "user.modified",
    "user.deleted",
    "user.revoked",
    "user.disabled",
    "user.enabled",
    "user.limited",
    "user.expired",
    "user.traffic_reset",
    "user.expires_in_72_hours",
    "user.expires_in_48_hours",
    "user.expires_in_24_hours",
    "user.expired_24_hours_ago",
    "user.first_connected",
    "user.bandwidth_usage_threshold_reached",
]

TServiceEvents = Literal[
    "service.panel_started",
    "service.login_attempt_failed",
    "service.login_attempt_success",
]

TErrorsEvents = Literal[
    "errors.bandwidth_usage_threshold_reached_max_notifications",
]

TCRMEvents = Literal[
    "crm.infra_billing_node_payment_in_7_days",
    "crm.infra_billing_node_payment_in_48hrs",
    "crm.infra_billing_node_payment_in_24hrs",
    "crm.infra_billing_node_payment_due_today",
    "crm.infra_billing_node_payment_overdue_24hrs",
    "crm.infra_billing_node_payment_overdue_48hrs",
    "crm.infra_billing_node_payment_overdue_7_days",
]

TUserHwidDevicesEvents = Literal[
    "user_hwid_devices.added",
    "user_hwid_devices.deleted",
]

TResetPeriods = Literal["NO_RESET", "DAY", "WEEK", "MONTH"]
TUsersStatus = Literal["DISABLED", "LIMITED", "EXPIRED", "ACTIVE"]
