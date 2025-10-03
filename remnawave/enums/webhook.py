
from enum import StrEnum

class UserEvent(StrEnum):
    CREATED = "user.created"
    MODIFIED = "user.modified"
    DELETED = "user.deleted"
    REVOKED = "user.revoked"
    DISABLED = "user.disabled"
    ENABLED = "user.enabled"
    LIMITED = "user.limited"
    EXPIRED = "user.expired"
    TRAFFIC_RESET = "user.traffic_reset"
    EXPIRES_IN_72_HOURS = "user.expires_in_72_hours"
    EXPIRES_IN_48_HOURS = "user.expires_in_48_hours"
    EXPIRES_IN_24_HOURS = "user.expires_in_24_hours"
    EXPIRED_24_HOURS_AGO = "user.expired_24_hours_ago"
    FIRST_CONNECTED = "user.first_connected"
    BANDWIDTH_USAGE_THRESHOLD_REACHED = "user.bandwidth_usage_threshold_reached"


class NodeEvent(StrEnum):
    CREATED = "node.created"
    MODIFIED = "node.modified"
    DISABLED = "node.disabled"
    ENABLED = "node.enabled"
    DELETED = "node.deleted"
    CONNECTION_LOST = "node.connection_lost"
    CONNECTION_RESTORED = "node.connection_restored"
    TRAFFIC_NOTIFY = "node.traffic_notify"


class InfraBillingEvent(StrEnum):
    PAYMENT_IN_7_DAYS = "crm.infra_billing_node_payment_in_7_days"
    PAYMENT_IN_48HRS = "crm.infra_billing_node_payment_in_48hrs"
    PAYMENT_IN_24HRS = "crm.infra_billing_node_payment_in_24hrs"
    PAYMENT_DUE_TODAY = "crm.infra_billing_node_payment_due_today"
    PAYMENT_OVERDUE_24HRS = "crm.infra_billing_node_payment_overdue_24hrs"
    PAYMENT_OVERDUE_48HRS = "crm.infra_billing_node_payment_overdue_48hrs"
    PAYMENT_OVERDUE_7_DAYS = "crm.infra_billing_node_payment_overdue_7_days"


class ServiceEvent(StrEnum):
    PANEL_STARTED = "service.panel_started"
    LOGIN_ATTEMPT_FAILED = "service.login_attempt_failed"
    LOGIN_ATTEMPT_SUCCESS = "service.login_attempt_success"
